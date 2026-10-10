from datetime import date

import pytest

from fitness_utils import calculate_bmi, membership_status


def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == 22.86


def test_calculate_bmi_rejects_invalid_weight():
    with pytest.raises(ValueError):
        calculate_bmi(0, 1.75)


def test_calculate_bmi_rejects_invalid_height():
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)


def test_membership_status_active():
    assert membership_status(date(2026, 12, 31), date(2026, 10, 11)) == "Active"


def test_membership_status_expired():
    assert membership_status(date(2026, 10, 10), date(2026, 10, 11)) == "Expired"


def test_membership_expiring_today_is_active():
    assert membership_status(date(2026, 10, 11), date(2026, 10, 11)) == "Active"