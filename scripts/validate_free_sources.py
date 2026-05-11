import json
import os
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

checks = []


def add_check(name, path, required_columns=None, file_type='parquet', allow_empty=False):
    path = Path(path)
    result = {
        'name': name,
        'path': str(path),
        'exists': path.exists(),
        'ok': False,
        'rows': None,
        'columns': [],
        'missing_columns': [],
        'error': None,
        'allow_empty': allow_empty,
    }

    if not path.exists():
        result['error'] = 'File not found'
        checks.append(result)
        return

    try:
        if file_type == 'md':
            text = path.read_text(encoding='utf-8')
            result['rows'] = len([line for line in text.splitlines() if line.strip()])
            result['columns'] = ['markdown_text']
            result['ok'] = bool(text.strip())
        elif file_type == 'csv':
            df = pd.read_csv(path)
            result['rows'] = int(len(df))
            result['columns'] = list(df.columns)
            if required_columns:
                result['missing_columns'] = [c for c in required_columns if c not in df.columns]
            result['ok'] = (allow_empty or result['rows'] > 0) and not result['missing_columns']
        else:
            df = pd.read_parquet(path)
            result['rows'] = int(len(df))
            result['columns'] = list(df.columns)
            if required_columns:
                result['missing_columns'] = [c for c in required_columns if c not in df.columns]
            result['ok'] = (allow_empty or result['rows'] > 0) and not result['missing_columns']
    except Exception as exc:
        result['error'] = repr(exc)

    checks.append(result)


add_check('football-data.co.uk Premier League 24/25', 'data/raw/premier_league_2425.parquet', required_columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])
add_check('Upcoming fixtures', 'data/raw/upcoming/upcoming_fixtures.parquet', required_columns=['fixture_id', 'match_date', 'home_team', 'away_team'], allow_empty=True)
add_check('Forward fixture results', 'output/latest/forward_fixture_results.csv', required_columns=['fixture_id', 'home_team', 'away_team', 'home_score', 'away_score', 'result_status'], file_type='csv', allow_empty=True)
add_check('Forward fixture result status', 'output/latest/forward_fixture_result_status.csv', required_columns=['fixture_rows_checked', 'result_rows', 'settled_result_rows', 'errors'], file_type='csv', allow_empty=False)
add_check('Forward probability calibration report', 'output/latest/forward_probability_calibration_report.csv', required_columns=['prediction_id', 'fixture_id', 'predicted_selection', 'predicted_probability', 'settlement_status'], file_type='csv', allow_empty=True)
add_check('Forward probability calibration summary', 'output/latest/forward_probability_calibration_summary.csv', required_columns=['forward_probability_rows', 'settled_rows', 'unsettled_rows', 'accuracy', 'avg_brier_score'], file_type='csv', allow_empty=False)
add_check('Automatic forward source report', 'output/latest/automatic_forward_source_report.csv', required_columns=['upcoming_fixture_rows', 'has_automatic_forward_odds', 'automatic_forward_status', 'blocker'], file_type='csv', allow_empty=False)
add_check('Automatic forward prices', 'output/latest/automatic_forward_prices.csv', required_columns=['fixture_id', 'home_team', 'away_team', 'market_home_odds', 'market_draw_odds', 'market_away_odds', 'source_quality'], file_type='csv', allow_empty=True)
add_check('Forward price source adapter', 'output/latest/forward_price_source_adapter.csv', required_columns=['fixture_rows', 'configured_sources', 'enabled_sources', 'automatic_price_rows', 'adapter_status'], file_type='csv', allow_empty=False)
add_check('Fixture model match report', 'output/latest/fixture_model_match_report.csv', required_columns=['fixture_id', 'source_team', 'matched_model_team', 'match_type', 'suggested_model_team'], file_type='csv', allow_empty=True)
add_check('Fixture model match summary', 'output/latest/fixture_model_match_summary.csv', required_columns=['fixture_rows', 'team_rows_checked', 'matched_team_rows', 'unmatched_team_rows', 'ready_for_model_fixture_join'], file_type='csv', allow_empty=False)
add_check('Forward fixture predictions', 'output/latest/forward_fixture_predictions.parquet', required_columns=['prediction_id', 'fixture_id', 'home_win_probability', 'draw_probability', 'away_win_probability', 'sample_phase'], allow_empty=True)
add_check('Forward fixture prediction summary', 'output/latest/forward_fixture_prediction_summary.csv', required_columns=['upcoming_fixture_rows', 'forward_fixture_prediction_rows', 'probability_only', 'has_market_prices', 'ready_for_price_join'], file_type='csv', allow_empty=False)
add_check('Forward fixture prediction log', 'output/latest/forward_fixture_prediction_log_latest.csv', required_columns=['prediction_id', 'fixture_id', 'home_win_probability', 'draw_probability', 'away_win_probability', 'sample_phase'], file_type='csv', allow_empty=True)
add_check('Forward fixture prediction log status', 'output/latest/forward_fixture_prediction_log_status.csv', required_columns=['current_forward_fixture_predictions', 'new_forward_fixture_predictions_logged', 'total_forward_fixture_predictions_logged', 'log_type'], file_type='csv', allow_empty=False)
add_check('Manual odds template', 'output/latest/manual_odds_template.csv', required_columns=['fixture_id', 'home_team', 'away_team', 'market_home_odds', 'market_draw_odds', 'market_away_odds'], file_type='csv', allow_empty=True)
add_check('Manual odds instructions', 'output/latest/manual_odds_instructions.md', file_type='md', allow_empty=False)
add_check('Manual forward snapshots', 'output/latest/manual_forward_snapshots.parquet', required_columns=['prediction_id', 'sample_phase', 'market_odds', 'probability', 'ev'], allow_empty=True)
add_check('ClubElo latest snapshot', 'data/raw/clubelo_latest.parquet', required_columns=['Club', 'Elo'])
add_check('Basic team strength model', 'data/model/team_strengths.parquet', required_columns=['attack_strength', 'defense_strength'])
add_check('Poisson predictions', 'output/latest/poisson_predictions.parquet', required_columns=['home_team', 'away_team', 'fair_home_odds'])
add_check('Probability calibration adjustments', 'output/latest/probability_calibration_adjustments.csv', required_columns=['home_team', 'away_team', 'probability_column', 'probability_band', 'calibration_action', 'multiplier'], file_type='csv', allow_empty=True)
add_check('Probability calibration rules', 'output/latest/probability_calibration_rules.csv', required_columns=['probability_band', 'calibration_action', 'adjustments'], file_type='csv', allow_empty=True)
add_check('Probability calibration impact', 'output/latest/probability_calibration_impact_report.csv', required_columns=['probability_band', 'calibration_action', 'rows', 'avg_raw_probability', 'avg_multiplier'], file_type='csv', allow_empty=True)
add_check('Expected value calculations', 'output/latest/ev_results.parquet', required_columns=['home_ev', 'draw_ev', 'away_ev'])
add_check('Prediction log output', 'output/latest/prediction_log_latest.parquet', required_columns=['prediction_id', 'event_id', 'market', 'selection'])
add_check('Settled predictions output', 'output/latest/settled_predictions.parquet', required_columns=['prediction_id', 'settlement_status'])
add_check('CLV results output', 'output/latest/clv_results.parquet', required_columns=['prediction_id', 'clv_delta', 'beat_closing_line', 'sample_phase'])
add_check('Candidate bets output', 'output/latest/candidate_bets.parquet', required_columns=['prediction_id', 'probability_band', 'suppression_action', 'rejection_reason'], allow_empty=True)
add_check('Paper test picks output', 'output/latest/paper_test_picks.parquet', required_columns=['prediction_id', 'paper_test_tier', 'paper_test_score', 'paper_test_reason'], allow_empty=True)
add_check('Valid forward paper test log', 'output/latest/paper_test_log_latest.csv', required_columns=['prediction_id', 'paper_test_tier', 'paper_test_score', 'paper_test_reason'], file_type='csv', allow_empty=True)
add_check('Invalid paper test log rows', 'output/latest/invalid_paper_test_log_rows.csv', required_columns=['prediction_id', 'sample_phase', 'home_team', 'away_team'], file_type='csv', allow_empty=True)
add_check('Paper test log status', 'output/latest/paper_test_log_status.csv', required_columns=['raw_log_rows', 'valid_forward_log_rows', 'invalid_historical_proxy_log_rows', 'has_valid_forward_log'], file_type='csv', allow_empty=True)
add_check('CLV band diagnostics', 'output/latest/clv_band_report.csv', required_columns=['probability_band', 'rows', 'avg_clv_delta', 'beat_closing_line_rate'], file_type='csv', allow_empty=True)
add_check('Signal suppression rules', 'output/latest/signal_suppression_rules.csv', required_columns=['rule_type', 'target', 'action', 'reason'], file_type='csv', allow_empty=True)
add_check('Rule action summary', 'output/latest/rule_action_summary.csv', required_columns=['action', 'rules', 'targets'], file_type='csv', allow_empty=True)
add_check('Sample phase performance', 'output/latest/phase_performance_report.csv', required_columns=['sample_phase', 'settled_rows', 'clv_rows', 'recommended_usage'], file_type='csv', allow_empty=True)

run_number = os.getenv('GITHUB_RUN_NUMBER', 'local')
run_attempt = os.getenv('GITHUB_RUN_ATTEMPT', 'local')
run_id = os.getenv('GITHUB_RUN_ID', 'local')
sha = os.getenv('GITHUB_SHA', 'local')
ref = os.getenv('GITHUB_REF_NAME', 'local')

status = {
    'generated_at_utc': datetime.now(timezone.utc).isoformat(),
    'github_run_number': run_number,
    'github_run_attempt': run_attempt,
    'github_run_id': run_id,
    'github_sha': sha,
    'github_ref': ref,
    'overall_ok': all(c['ok'] for c in checks),
    'checks': checks,
}

output_dir = Path('output/latest')
history_dir = Path('output/history')
output_dir.mkdir(parents=True, exist_ok=True)
history_dir.mkdir(parents=True, exist_ok=True)

json_text = json.dumps(status, indent=2)
json_path = output_dir / 'free_data_status.json'
md_path = output_dir / 'free_data_status.md'
history_json_path = history_dir / f'free_data_status_run_{run_number}_attempt_{run_attempt}.json'

json_path.write_text(json_text, encoding='utf-8')
history_json_path.write_text(json_text, encoding='utf-8')

lines = [
    '# Free Data Source Status',
    '',
    f"Generated UTC: `{status['generated_at_utc']}`",
    f"GitHub run: `{run_number}` attempt `{run_attempt}`",
    f"GitHub SHA: `{sha}`",
    '',
    f"Overall status: `{'OK' if status['overall_ok'] else 'FAILED'}`",
    '',
    '| Source | OK | Rows | Missing columns | Error |',
    '|---|---:|---:|---|---|',
]

for check in checks:
    lines.append(
        f"| {check['name']} | {check['ok']} | {check['rows']} | "
        f"{', '.join(check['missing_columns']) if check['missing_columns'] else ''} | "
        f"{check['error'] or ''} |"
    )

md_text = '\n'.join(lines) + '\n'
md_path.write_text(md_text, encoding='utf-8')
(history_dir / f'free_data_status_run_{run_number}_attempt_{run_attempt}.md').write_text(md_text, encoding='utf-8')

print(json_text)

if not status['overall_ok']:
    raise SystemExit(1)
