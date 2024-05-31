import re
from .scanner import CodeType
from .result import Result


def decode_tme_barcode(code_type: CodeType, barcode: str):
    if code_type == CodeType.DataMatrix:
        return decode_datamatrix(barcode)
    elif code_type == CodeType.QR:
        return decode_qr(barcode)


def decode_datamatrix(barcode: str):
    tme_regexpr = r"P([\w\.\-\/%]*) 1P([\w\.\-\\/)\(,]*) Q(\d*) (?:4L\w* )?K(\d*)/(\d*)"
    tme_regexpr_compiled = re.compile(tme_regexpr)
    matched = tme_regexpr_compiled.match(barcode)
    if matched:
        result = Result(distributor="TME",
                        mon=matched.group(2),
                        don=matched.group(1),
                        order_number={'number': matched.group(4), 'position': matched.group(5)},
                        quantity=float(matched.group(3)))
        return result


def decode_qr(barcode: str):
    lines = barcode.split(' ')

    result = Result(distributor="TME")
    for line in lines:
        if line.startswith('QTY:'):
            result.quantity = int(line.removeprefix('QTY:'))
        elif line.startswith('PN:'):
            result.don = line.removeprefix('PN:')
        elif line.startswith('PO:'):
            order_number, position = line.removeprefix('PO:').split('/')
            result.order_number['number'] = order_number
            result.order_number['position'] = position
        elif line.startswith('MFR'):
            result.manufacturer = line.removeprefix('MFR:')
        elif line.startswith('MPN:'):
            result.mon = line.removeprefix('MPN:')
    return result
