import unittest
from BIO_2019 import check_pali, pali_gen


class TestPaliGen(unittest.TestCase):
  def setUp(self):
    self.palis = ["1", "121", "45654"]
    self.pali_pairs = [
      ("343", "353"),
      ("17", '22'),
      ("192334", "193391")
    ]
    with open("2019_cases.txt") as cases:
      # Get all the lines from TEST 1 to end or TEST 2
      for line in cases:
        pass #TODO - IM HERRE
  
  def test_pali_check(self):
    for i in self.palis:
      self.assertTrue(check_pali(i))

  def test_pali_gen(self):
    for i in self.pali_pairs:
      self.assertEqual(pali_gen(i[0]), i[1])



if __name__ == '__main__':
    unittest.main()