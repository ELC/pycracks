from pycracks.pycracks import is_breaking_change_expected

from packaging.version import Version

from hypothesis import given, assume
from hypothesis.strategies import composite, integers, booleans


@composite
def versions(draw) -> Version:
    major = draw(integers(min_value=0))
    minor = draw(integers(min_value=0))
    patch = draw(integers(min_value=0))
    return Version(f"{major}.{minor}.{patch}")


@given(new_version=versions(), old_version=versions())
def test_breaking_change_and_test_not_passed(
    new_version: Version, old_version: Version
) -> None:
    assume(new_version.major == old_version.major)
    test_passed = False
    assert not is_breaking_change_expected(new_version, old_version, test_passed)


@given(new_version=versions(), old_version=versions())
def test_breaking_change_and_test_passed(
    new_version: Version, old_version: Version
) -> None:
    assume(new_version.major == old_version.major)
    test_passed = True
    assert is_breaking_change_expected(new_version, old_version, test_passed)


@given(new_version=versions(), old_version=versions(), test_passed=booleans())
def test_not_breaking_change(
    new_version: Version, old_version: Version, test_passed: bool
) -> None:
    assume(new_version.major > old_version.major)
    assert is_breaking_change_expected(new_version, old_version, test_passed)
