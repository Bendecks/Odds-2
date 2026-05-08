import copy
from datetime import datetime, timezone, timedelta

from dedupe import dedupe_observations


def iso(dt):
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def base_obs(odds=1.83, capture_offset_minutes=0, event_offset_minutes=0):
    base_capture = datetime(2026, 5, 8, 10, 0, tzinfo=timezone.utc)
    base_event = datetime(2026, 5, 8, 18, 0, tzinfo=timezone.utc)
    return {
        'record_type': 'market_observation',
        'event_id': 'evt_test_liverpool_chelsea',
        'market_id': 'mkt_test_liverpool_1x2_1',
        'observation_id': f'obs_{str(odds).replace(".", "_")}_{capture_offset_minutes}_{event_offset_minutes}',
        'capture': {'utc': iso(base_capture + timedelta(minutes=capture_offset_minutes))},
        'event_time': {'utc': iso(base_event + timedelta(minutes=event_offset_minutes))},
        'event': {'home': 'Liverpool', 'away': 'Chelsea', 'league': 'Premier League'},
        'market': {'type': '1X2', 'line': '1', 'selection': 'Liverpool', 'odds': odds},
        'parser_confidence': {'total': 0.975, 'status': 'high'},
        'status': 'parsed_candidate'
    }


def run_case(name, previous, new, expected_status):
    rows, report = dedupe_observations(new, previous)
    statuses = [r.get('dedupe_status') for r in rows]
    assert statuses == expected_status, f'{name}: expected {expected_status}, got {statuses}, report={report}'
    return {'name': name, 'statuses': statuses, 'report': report}


def main():
    results = []
    previous = [base_obs(1.83, 0)]

    # 1. Identity Test: same odds within duplicate window -> duplicate_noise.
    results.append(run_case('identity_duplicate_noise', previous, [base_obs(1.80 + 0.03, 2)], ['duplicate_noise']))

    # 2. Tick Test: 1.83 -> 1.82 after 20 minutes -> small_movement (<3%).
    results.append(run_case('tick_small_movement', previous, [base_obs(1.82, 20)], ['small_movement']))

    # 3. Steam Test: 1.83 -> 1.60 after 20 minutes -> significant_odds_change (>10%).
    results.append(run_case('steam_significant_movement', previous, [base_obs(1.60, 20)], ['significant_odds_change']))

    # 4. Conflict Test: same market but event time shifted > tolerance -> parser_conflict.
    results.append(run_case('event_time_parser_conflict', previous, [base_obs(1.83, 20, 25)], ['parser_conflict']))

    print('Phase 1.1 dedupe tests OK')
    for r in results:
        print(r)


if __name__ == '__main__':
    main()
