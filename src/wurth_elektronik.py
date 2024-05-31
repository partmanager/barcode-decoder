import re
from .scanner import CodeType
from .result import Result


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
        manufacturer_order_number = matched.group(1).removeprefix('1P').rstrip(']')
        quantity = int(matched.group(2).removeprefix('Q').rstrip(']'))

        result = Result(distributor='Wurth Elektronik',
                        order_number={'number': None, 'position': None},
                        mon=manufacturer_order_number,
                        don=manufacturer_order_number,
                        quantity=quantity,
                        LOT=matched.group(3).lstrip('1T').rstrip(']'),
                        date_code=matched.group(4).lstrip('16D'),
                        manufacturer='Wurth Elektronik')
        return result
