import pytest

from flight_calculator import calculate_flight_time

"""copilot suggested these test cases, I approved, 
and confirmed the edge cases and typical cases were included"""

def test_calculate_flight_time_zero_weight():
    assert calculate_flight_time(0) == 180.0


def test_calculate_flight_time_positive_weight():
    assert calculate_flight_time(100) == 170.0


def test_calculate_flight_time_at_boundaries():
    assert calculate_flight_time(1800) == 0
    assert calculate_flight_time(1801) == 0


def test_calculate_flight_time_negative_weight_raises_value_error():
    with pytest.raises(ValueError, match="Weight cannot be negative"):
        calculate_flight_time(-1)


def test_calculate_flight_time_float_weight():
    assert calculate_flight_time(250.5) == pytest.approx(154.95)
