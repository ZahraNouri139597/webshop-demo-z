# Test data from the Webshop Demo test data sheet. Do not change this file.
# Money is in cents: 5000 means €50.00.

CODES = {
    "SPRING10": {"percent": 10, "min_cents": 5000,  "expiry": "2026-12-31"},
    "SUMMER20": {"percent": 20, "min_cents": 10000, "expiry": "2026-08-31"},
    "HALF2026": {"percent": 50, "min_cents": 20000, "expiry": "2026-11-30"},
    "WELCOME5": {"percent": 5,  "min_cents": 0,     "expiry": "2027-06-30"},
}

USED_CODES = {
    "anna@test.example": ["WELCOME5"],
    "ben@test.example": [],
}

SHIPPING_CENTS = 495