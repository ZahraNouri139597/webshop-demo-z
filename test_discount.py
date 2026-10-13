#from discount import calculate_discount
from discount import calculate_discount, order_total
#from discount import check_code

# Background: Given the current date is "2026-10-07"
TODAY = "2026-10-07"
BEN = "ben@test.example"
ANNA = "anna@test.example"

def test_ac1_spring10_on_80_euros_gives_8_euros_discount():
    assert calculate_discount(8000, 10) == 800

def test_ac1_spring10_order_total_is_76_95():
    assert order_total(8000, "spring10",BEN,TODAY)==7695


#ac2
def test_ac2_normalized_code_with_different_subtotal():
    assert order_total(10000, " spring10 ", BEN, TODAY) == 9495


def test_ac02_lowercase_and_spaces_is_accepted():
    assert order_total(8000, "  spring10 ", BEN, TODAY) == 7695