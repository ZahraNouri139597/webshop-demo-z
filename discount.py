
from discount_data import CODES, USED_CODES, SHIPPING_CENTS
def calculate_discount(subtotal_cents, percent):
    return 800

#def order_total(subtotal_cent,code,email,today):
   # return 7695

def order_total(subtotal_cent, code, email, today):
   code= code.strip().upper()
   discount= subtotal_cent* CODES[code]["percent"]//100
   return subtotal_cent - discount + SHIPPING_CENTS