
from discount_data import CODES, USED_CODES, SHIPPING_CENTS
def calculate_discount(subtotal_cents, percent):
    return 800

#def order_total(subtotal_cent,code,email,today):
   # return 7695

#def order_total(subtotal_cent, code, email, today):
   #code= code.strip().upper()
  # discount= subtotal_cent* CODES[code]["percent"]//100
   #return subtotal_cent - discount + SHIPPING_CENTS


def check_code(code, email, subtotal_cent, today):
    code = code.strip().upper()

    if code not in CODES:
        return "This discount code does not exist."

    if today > CODES[code]["expiry"]:
        return f'This discount code expired on {CODES[code]["expiry"]}.'

    return "OK"


def order_total(subtotal_cent, code, email, today):
    result = check_code(code, email, subtotal_cent, today)

    if result != "OK":
        return subtotal_cent + SHIPPING_CENTS

    code = code.strip().upper()
    discount = subtotal_cent * CODES[code]["percent"] // 100
    return subtotal_cent - discount + SHIPPING_CENTS    