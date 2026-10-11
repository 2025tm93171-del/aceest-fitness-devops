
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
    expiry = date(2026, 12, 31)
    today = date(2026, 10, 11)
    assert membership_status(expiry, today) == "Active"


def test_membership_status_expired():
    expiry = date(2026, 10, 10)
    today = date(2026, 10, 11)
    assert membership_status(expiry, today) == "Expired"


def test_membership_expiring_today_is_active():
    today = date(2026, 10, 11)
    assert membership_status(today, today) == "Active"
