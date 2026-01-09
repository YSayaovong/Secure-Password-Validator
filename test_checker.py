import pytest
from secure_password_validator import PwnedPasswordChecker, PwnedResult


class MockSession:
    """Mock requests.Session for testing without network calls."""
    def __init__(self, response_text: str, status_code: int = 200):
        self.response_text = response_text
        self.status_code = status_code

    def get(self, url, headers=None, timeout=None):
        return MockResponse(self.response_text, self.status_code)


class MockResponse:
    def __init__(self, text: str, status_code: int):
        self.text = text
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code != 200:
            raise RuntimeError(f"HTTP {self.status_code}")


def test_password_found_in_breach():
    # Tail matches hash suffix, count = 42
    mock_api_text = "ABCDEF1234567890:42\nBBBBBBBBBBBBBBBB:2"
    session = MockSession(mock_api_text)

    checker = PwnedPasswordChecker(session=session)
    result = checker.check_password("password")

    assert isinstance(result, PwnedResult)
    assert result.count == 42


def test_password_not_found_in_breach():
    mock_api_text = "AAAAAAAAAAAAAAAAAAAA:10\nBBBBBBBBBBBBBBBBBBBB:5"
    session = MockSession(mock_api_text)

    checker = PwnedPasswordChecker(session=session)
    result = checker.check_password("uniquepassword123")

    assert result.count == 0


def test_api_failure_raises_error():
    session = MockSession("", status_code=500)
    checker = PwnedPasswordChecker(session=session)

    with pytest.raises(RuntimeError):
        checker.check_password("password123")
