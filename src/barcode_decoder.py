from .mouser import decode_mouser_barcode
from .tme import decode_tme_barcode
from .scanner import detect_code_type

decoders = [decode_mouser_barcode, decode_tme_barcode]


def decode_barcode(barcode: str):
    """Takes a scanned barcode and returns a decoded parameters in form of a list of dictionaries"""
    result = []
    barcode = barcode.upper()
    code_type, code = detect_code_type(barcode)
    for decoder in decoders:
        decoded = decoder(code_type, code)
        result.append(decoded)
    return result
