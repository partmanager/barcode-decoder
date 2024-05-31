from .mouser import decode_mouser_barcode
from .tme import decode_tme_barcode

decoders = [decode_mouser_barcode, decode_tme_barcode]


def decode_barcode(barcode):
    result = []
    for decoder in decoders:
        decoded = decoder(barcode)
        result.append(decoded)
    return result
