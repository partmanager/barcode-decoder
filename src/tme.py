import re
from .scanner import CodeType


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
        result = {'distributor': {'name': 'TME'},
                  'order_number': {'number': matched.group(4), 'position': matched.group(5)},
                  'invoice': None,
                  'manufacturer_order_number': matched.group(2),
                  'distributor_order_number': {'text': matched.group(1), 'don': None},
                  'quantity': matched.group(3),
                  'LOT': None,
                  'Date_Code': None,
                  'manufacturer': {'name': None}}
        return result


def decode_qr(barcode: str):
    lines = barcode.split(' ')

    result = {'distributor': {'name': 'TME'},
              'order_number': {'number': None, 'position': None},
              'invoice': None,
              'manufacturer_order_number': None,
              'distributor_order_number': {'text': None, 'don': None},
              'quantity': None,
              'LOT': None,
              'Date_Code': None,
              'manufacturer': {}}
    for line in lines:
        if line.startswith('QTY:'):
            result['quantity'] = int(line.removeprefix('QTY:'))
        elif line.startswith('PN:'):
            result['distributor_order_number']['text'] = line.removeprefix('PN:')
        elif line.startswith('PO:'):
            order_number, position = line.removeprefix('PO:').split('/')
            result['order_number']['number'] = order_number
            result['order_number']['position'] = position
        elif line.startswith('MFR'):
            result['manufacturer']['name'] = line.removeprefix('MFR:')
        elif line.startswith('MPN:'):
            result['manufacturer_order_number'] = line.removeprefix('MPN:')
    return result
