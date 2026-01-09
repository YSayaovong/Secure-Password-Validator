import hashlib
import sys
from dataclasses import dataclass
from getpass import getpass
from typing import Optional

import requests

HIBP_RANGE_URL = "https://api.pwnedpasswords.com/range/{}"
USER_AGENT = "Secure-Password-Validator/1.0"


@dataclass(frozen=True)
class PwnedResult:
    count: int
    sha1_prefix: str
    sha1_tail: str


class PwnedPasswordChecker:
    def __init__(self, session: Optional[requests.Session] = None, timeout_seconds: int = 10):
        self.session = session or requests.Session()
        self.timeout_seconds = timeout_seconds

    def _request_api_data(self, first5: str) -> str:
        headers = {"User-Agent": USER_AGENT, "Add-Padding": "true"}
        resp = self.session.get(
            HIBP_RANGE_URL.format(first5),
            headers=headers,
            timeout=self.timeout_seconds
        )
        resp.raise_for_status()
        return resp.text

    @staticmethod
    def _sha1_upper(password: str) -> str:
        return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

    @staticmethod
    def _get_leak_count(hashes_text: str, tail_to_check: str) -> int:
        for line in hashes_text.splitlines():
            try:
                suffix, count = line.split(":")
            except ValueError:
                continue
            if suffix == tail_to_check:
                return int(count)
        return 0

    def check_password(self, password: str) -> PwnedResult:
        sha1_hash = self._sha1_upper(password)
        first5, tail = sha1_hash[:5], sha1_hash[5:]
        hashes_text = self._request_api_data(first5)
        count = self._get_leak_count(hashes_text, tail)
        return PwnedResult(count, first5, tail)


def main() -> int:
    pw = getpass("Enter password to check (not stored): ").strip()
    if not pw:
        print("No password entered.")
        return 2

    checker = PwnedPasswordChecker()
    try:
        result = checker.check_password(pw)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if result.count > 0:
        print(f"This password appeared in breaches {result.count:,} times. Choose another.")
        return 3
    else:
        print("Password not found in breach database.")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
