from .scanner import CodeType
from .result import Result


def decode_farnell_barcode(code_type: CodeType, barcode):
    if code_type == CodeType.DataMatrix:
        return decode_datamatrix(barcode)


def decode_datamatrix(barcode):
    data = barcode.removesuffix("^D").split(']')

    result = Result(distributor="Farnell")
    for param in data:
        if param.startswith('K'):
            result.order_number = {"number": param.removeprefix('K')}
        elif param.startswith('1P'):
            result.mon = param.removeprefix('1P')
        elif param.startswith('3P'):
            result.don = param.removeprefix('3P')
        elif param.startswith('Q'):
            result.quantity = float(param.removeprefix('Q'))
        elif param.startswith('16D'):
            result.date_code = param.removeprefix('16D')
        elif param.startswith('4L'):
            result.coo = param.removeprefix('4L')
        elif param.startswith('4K'):
            result.order_number["position"] = param.removeprefix('4K')
    return result
