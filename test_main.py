from main import fetch_rate
from pathlib import Path

def test_fetch_rate_valid():
    rate = fetch_rate("USD", "EUR")
    assert isinstance(rate, float)
    assert rate > 0

def test_fetch_rate_invalid():
    rate = fetch_rate("USD", "FAKE")
    assert rate is None

def test_log_file_created(tmp_path):
    # Use a temp log file for test
    from main import log_result
    test_log = tmp_path / "log.json"
    log_result("USD", "EUR", 1.0)
    assert test_log.exists() or Path("logs/log.json").exists()
