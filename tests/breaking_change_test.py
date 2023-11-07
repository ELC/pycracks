from hypothesis import assume, given
from hypothesis.strategies import booleans, composite, integers
from packaging.version import Version

from pycracks.pycracks import is_breaking_change_expected


@composite
def versions(draw, major: int = 0, minor: int = 0, patch: int = 0) -> Version:
    major = major or draw(integers(min_value=0))
    minor = minor or draw(integers(min_value=0))
    patch = patch or draw(integers(min_value=0))
    return Version(f"{major}.{minor}.{patch}")


@given(new_version=versions(major=1), old_version=versions(major=1))
def test_breaking_change_and_test_not_passed(
    new_version: Version, old_version: Version
) -> None:
    test_passed = False
    assert not is_breaking_change_expected(new_version, old_version, test_passed)


@given(new_version=versions(major=1), old_version=versions(major=1))
def test_breaking_change_and_test_passed(
    new_version: Version, old_version: Version
) -> None:
    test_passed = True
    assert is_breaking_change_expected(new_version, old_version, test_passed)


@given(new_version=versions(), old_version=versions(), test_passed=booleans())
def test_not_breaking_change(
    new_version: Version, old_version: Version, test_passed: bool
) -> None:
    assume(new_version.major > old_version.major)
    assert is_breaking_change_expected(new_version, old_version, test_passed)
