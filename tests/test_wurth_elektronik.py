import unittest
from src.wurth_elektronik import decode_wurth_elektronik
from src.scanner import CodeType


class TestTMEBarcodeDecoder(unittest.TestCase):
    def test_string_decode(self):
        str1 = '[)>^06]1P744912168]Q5]1T329012581410000]16D20140307^d'
        decoded = decode_wurth_elektronik(CodeType.DataMatrix, str1.upper())
        self.assertEqual(decoded['order_number']['number'], None)
        self.assertEqual(decoded['order_number']['position'], None)
        self.assertEqual(decoded['invoice'], None)
        self.assertEqual(decoded['distributor_order_number']['text'], '744912168')
        self.assertEqual(decoded['manufacturer_order_number'], '744912168')
        self.assertEqual(decoded['quantity'], 5)
        self.assertEqual(decoded['LOT'], '329012581410000')
        self.assertEqual(decoded['Date_Code'], '20140307')
        self.assertEqual(decoded['manufacturer'], {'name': 'Wurth Elektronik'})

    def test_string_decode_2(self):
        str1 = '[)>^06]1P744273801]Q3]1T249010431105000]16D20110207^d'
        decoded = decode_wurth_elektronik(CodeType.PDF417, str1.upper())
        self.assertEqual(decoded['order_number']['number'], None)
        self.assertEqual(decoded['order_number']['position'], None)
        self.assertEqual(decoded['invoice'], None)
        self.assertEqual(decoded['distributor_order_number']['text'], '744273801')
        self.assertEqual(decoded['manufacturer_order_number'], '744273801')
        self.assertEqual(decoded['quantity'], 3)
        self.assertEqual(decoded['LOT'], '249010431105000')
        self.assertEqual(decoded['Date_Code'], '20110207')
        self.assertEqual(decoded['manufacturer'], {'name': 'Wurth Elektronik'})


if __name__ == '__main__':
    unittest.main()
