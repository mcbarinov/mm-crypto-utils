from mm_crypto_utils import get_log_prefix


def test_get_log_prefix():
    assert get_log_prefix(None) == ""
    assert get_log_prefix("s") == "s: "
