import unittest
from translator import englishToFrench 
from translator import frenchToEnglish

class TestE2f(unittest.TestCase):
    def test_e2f1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    def test_e2f2(self):
        self.assertEqual(frenchToEnglish('Au Revoir'), 'Goodbye')
    def test_e2f3(self):
        self.assertNotEqual(frenchToEnglish('None'), '')
    

class TestF2e(unittest.TestCase):
    def test_f2e1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    def test_f2e2(self):
        self.assertEqual(englishToFrench('Goodbye'), 'Au Revoir')
    def test_f2e3(self):
        self.assertNotEqual(englishToFrench('None'), '')

unittest.main()