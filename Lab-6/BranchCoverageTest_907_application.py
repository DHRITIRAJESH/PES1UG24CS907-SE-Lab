import pytest
from restaurant_bill import bill_total, split_bill, table_wait


# =====================================
# 1. BRANCH TESTS FOR bill_total()
# =====================================

def test_dine_in_bill():
    assert bill_total("dine_in", 1000, 2, False) == 1155

def test_takeaway_bill():
    assert bill_total("takeaway", 1000, 2, False) == 1050

def test_rooftop_bill():
    assert bill_total("rooftop", 1000, 2, False) == 1207

def test_happy_hour_dine_in():
    assert bill_total("dine_in", 1000, 2, True) == 924

def test_happy_hour_takeaway():
    assert bill_total("takeaway", 1000, 2, True) == 1050

def test_happy_hour_rooftop():
    assert bill_total("rooftop", 1000, 2, True) == 966

def test_large_group_service_charge():
    assert bill_total("dine_in", 1000, 8, False) == 1365

def test_unknown_section():
    with pytest.raises(ValueError, match="unknown section"):
        bill_total("balcony", 1000, 2, False)

def test_negative_food_total():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", -100, 2, False)

def test_zero_guests():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", 1000, 0, False)


# =====================================
# 2. BRANCH TESTS FOR split_bill()
# =====================================

def test_even_split():
    assert split_bill(1000, 4, 10) == 275

def test_split_with_remainder():
    assert split_bill(100, 3, 0) == 34

def test_split_without_tip():
    assert split_bill(1000, 4, 0) == 250

def test_split_with_tip():
    assert split_bill(500, 2, 10) == 275

def test_invalid_people_count():
    with pytest.raises(ValueError, match="invalid people count"):
        split_bill(1000, 0, 10)

def test_negative_tip():
    with pytest.raises(ValueError, match="invalid tip"):
        split_bill(1000, 4, -5)


# =====================================
# 3. BRANCH TESTS FOR table_wait()
# =====================================

def test_large_party_call_ahead():
    assert table_wait(13, 5, False) == "call ahead"

def test_reservation_seat_now():
    assert table_wait(4, 0, True) == "seat now"

def test_no_free_tables_waitlist():
    assert table_wait(4, 0, False) == "waitlist"

def test_large_party_limited_tables():
    assert table_wait(8, 1, False) == "waitlist"

def test_large_party_enough_tables():
    assert table_wait(8, 2, False) == "seat now"

def test_small_party_available_table():
    assert table_wait(4, 1, False) == "seat now"
