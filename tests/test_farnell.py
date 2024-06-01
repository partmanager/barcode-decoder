import unittest
from src.farnell import decode_farnell_barcode
from src.scanner import CodeType


class TestFarnellBarcodeDecoder(unittest.TestCase):
    def test_string_decode(self):
        str1 = ('[)>^06]kPO21000605]P]1PGRM155R71C224KA12D]3P2470468]q80]9D]1T]4LJP]4K9^d')
        decoded = decode_farnell_barcode(CodeType.DataMatrix, str1.upper())
        self.assertEqual(decoded.distributor, "Farnell")
        self.assertEqual(decoded.order_number['number'], 'PO21000605')
        self.assertEqual(decoded.order_number['position'], '9')
        self.assertEqual(decoded.invoice, None)
        self.assertEqual(decoded.don, '2470468')
        self.assertEqual(decoded.mon, 'GRM155R71C224KA12D')
        self.assertEqual(decoded.quantity, 80)
        self.assertEqual(decoded.LOT, None)
        self.assertEqual(decoded.date_code, None)
        self.assertEqual(decoded.manufacturer, None)


if __name__ == '__main__':
    unittest.main()
