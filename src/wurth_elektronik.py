import re
from .scanner import CodeType


def decode_wurth_elektronik(code_type: CodeType, barcode: str):
    if code_type == CodeType.DataMatrix:
        return decode_datamatrix(barcode)
    elif code_type == CodeType.PDF417:
        return decode_datamatrix(barcode)


def decode_datamatrix(barcode):
    we_regexpr = r"\[\)>\^06](1P\d*[A-Z]?])(Q\d*])(1T\d*])(16D\d*)\^D"
    we_regexpr_compiled = re.compile(we_regexpr)
    matched = we_regexpr_compiled.match(barcode)
    if matched:
        manufacturer_order_number = matched.group(1).lstrip('1P').rstrip(']')
        quantity = int(matched.group(2).lstrip('Q').rstrip(']'))
        result = {'distributor': {'name': 'Wurth Elektronik'},
                  'order_number': {'number': None, 'position': None},
                  'invoice': None,
                  'manufacturer_order_number': manufacturer_order_number,
                  'distributor_order_number': {'text': manufacturer_order_number, 'don': None},
                  'quantity': quantity,
                  'LOT': matched.group(3).lstrip('1T').rstrip(']'),
                  'Date_Code': matched.group(4).lstrip('16D'),
                  'manufacturer': {'name': 'Wurth Elektronik'}}
        return result
