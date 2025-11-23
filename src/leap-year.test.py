import unittest

def is_leap_year(year):
    #print("year %s" % year)
    if (year % 4 == 0):
      if (year % 100 == 0):
        if (year % 400 == 0):
          return True
        return False
      return True
    return False

class TestLeapYear(unittest.TestCase):

    def test_is_leap_year(self):
        self.assertFalse(is_leap_year(2025))
        self.assertFalse(is_leap_year(2001))
        self.assertTrue(is_leap_year(1996))
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(1800))
        self.assertTrue(is_leap_year(2000))

if __name__ == '__main__':
    unittest.main()