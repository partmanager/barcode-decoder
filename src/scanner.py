from enum import Enum


class CodeType(Enum):
    Barcode = 1
    DataMatrix = 2
    PDF417 = 3
    QR = 4


def detect_code_type(code):
    """Determine the code type based on the given string beginning. You need to properly configure your scanner
     to successfully detect barcode/QR code type."""
    if code.startswith(']C0'):
        return CodeType.Barcode, code.lstrip(']C0')
    elif code.startswith(']Q0'):
        return CodeType.QR, code.lstrip(']Q0')
    elif code.startswith(']Q6'):
        return CodeType.QR, code.lstrip(']Q6')
    elif code.startswith(']D1'):
        return CodeType.DataMatrix, code.lstrip(']D1')
    else:
        return None, code
