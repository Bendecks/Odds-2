def odds_plausibility(odds):
    if len(odds) != 3:
        return 0.0, 'expected_three_1x2_odds'
    try:
        vals = [float(x) for x in odds]
    except Exception:
        return 0.0, 'odds_not_numeric'
    if not all(1.01 <= v <= 50.0 for v in vals):
        return 0.0, 'odds_outside_plausible_range'
    overround = sum(1 / v for v in vals)
    if not 0.98 <= overround <= 1.35:
        return 0.55, f'overround_suspicious_{overround:.4f}'
    return 1.0, f'overround_ok_{overround:.4f}'


def calculate_parser_confidence(layout_detected, home_match, away_match, odds, event_time, completeness=True):
    breakdown = {}

    layout_score = 1.0 if layout_detected else 0.0
    breakdown['layout'] = {
        'passed': bool(layout_detected),
        'weight': 0.30,
        'subscore': layout_score,
        'score': round(layout_score * 0.30, 4),
        'reason': 'standard_1x2_inline_layout_detected' if layout_detected else 'layout_not_detected'
    }

    home_score = 0.0 if not home_match else float(home_match.get('match_score') or 0)
    away_score = 0.0 if not away_match else float(away_match.get('match_score') or 0)
    canonical_sub = min(home_score, away_score)
    canonical_passed = canonical_sub >= 0.85 and not (home_match or {}).get('requires_review') and not (away_match or {}).get('requires_review')
    breakdown['canonical'] = {
        'passed': canonical_passed,
        'weight': 0.30,
        'subscore': round(canonical_sub, 4),
        'score': round(canonical_sub * 0.30, 4),
        'home_match_score': round(home_score, 4),
        'away_match_score': round(away_score, 4),
        'reason': 'canonical_match_ok' if canonical_passed else 'canonical_match_requires_review'
    }

    odds_sub, odds_reason = odds_plausibility(odds)
    breakdown['odds'] = {
        'passed': odds_sub >= 0.95,
        'weight': 0.20,
        'subscore': odds_sub,
        'score': round(odds_sub * 0.20, 4),
        'reason': odds_reason
    }

    time_sub = float((event_time or {}).get('confidence') or 0)
    time_passed = time_sub >= 0.90 and bool((event_time or {}).get('utc'))
    breakdown['date_time'] = {
        'passed': time_passed,
        'weight': 0.10,
        'subscore': round(time_sub, 4),
        'score': round(time_sub * 0.10, 4),
        'reason': 'event_time_ok' if time_passed else 'event_time_low_confidence'
    }

    complete_sub = 1.0 if completeness else 0.0
    breakdown['completeness'] = {
        'passed': bool(completeness),
        'weight': 0.10,
        'subscore': complete_sub,
        'score': round(complete_sub * 0.10, 4),
        'reason': 'required_fields_present' if completeness else 'missing_required_fields'
    }

    total = sum(v['score'] for v in breakdown.values())
    status = 'high' if total >= 0.90 else 'medium' if total >= 0.75 else 'low'
    return {
        'total': round(total, 4),
        'status': status,
        'breakdown': breakdown,
        'real_bet_allowed': total >= 0.90
    }
