"""Utility functions for the ACEest Fitness application."""


def calculate_bmi(weight_kg, height_m):
    """Calculate BMI from weight in kilograms and height in metres."""
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")

    return round(weight_kg / (height_m * height_m), 2)


def membership_status(expiry_date, today):
    """Return membership status based on expiry and today's date."""
    if expiry_date < today:
        return "Expired"
    return "Active"