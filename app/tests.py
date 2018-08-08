import unittest
from datetime import datetime
from time_range import TimeRange, TimeRangeList

class TestTimeRangeSubtraction(unittest.TestCase):

    def tr(self, start, end):
        return TimeRange(datetime.strptime(start, "%H:%M") , datetime.strptime(end, "%H:%M"))

    def test_a(self):
        #Instantiate lists of time ranges
        a = TimeRangeList()
        b = TimeRangeList()
        #Load the ranges (a + b)
        a.insert(self.tr("9:00", "10:00"))
        b.insert(self.tr("9:30", "10:00"))
        #Sort the lists (a log a + b log b)
        a.sort()
        b.sort()
        #Subtract the arrays (a + b)
        a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        correct.insert(self.tr("9:00", "9:30"))
        #Check
        self.assertTrue(correct.compare(a))

    def test_b(self):
        #Instantiate lists of time ranges
        a = TimeRangeList()
        b = TimeRangeList()
        #Load the ranges (a + b)
        a.insert(self.tr("9:00", "10:00"))
        b.insert(self.tr("9:00", "10:00"))
        #Sort the lists (a log a + b log b)
        a.sort()
        b.sort()
        #Subtract the arrays (a + b)
        a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        #Check
        self.assertTrue(correct.compare(a))

    def test_c(self):
        #Instantiate lists of time ranges
        a = TimeRangeList()
        b = TimeRangeList()
        #Load the ranges (a + b)
        a.insert(self.tr("9:00", "9:30"))
        b.insert(self.tr("9:30", "15:00"))
        #Sort the lists (a log a + b log b)
        a.sort()
        b.sort()
        #Subtract the arrays (a + b)
        a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        correct.insert(self.tr("9:00", "9:30"))
        #Check
        self.assertTrue(correct.compare(a))

    def test_d(self):
        #Instantiate lists of time ranges
        a = TimeRangeList()
        b = TimeRangeList()
        #Load the ranges (a + b)
        a.insert(self.tr("9:00", "9:30"))
        a.insert(self.tr("10:00", "10:30"))
        b.insert(self.tr("9:15", "10:15"))
        #Sort the lists (a log a + b log b)
        a.sort()
        b.sort()
        #Subtract the arrays (a + b)
        a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        correct.insert(self.tr("9:00", "9:15"))
        correct.insert(self.tr("10:15", "10:30"))
        #Check
        self.assertTrue(correct.compare(a))


    def test_e(self):
        #Instantiate lists of time ranges
        a = TimeRangeList()
        b = TimeRangeList()
        #Load the ranges (a + b)
        a.insert(self.tr("9:00", "11:00"))
        a.insert(self.tr("13:00", "15:00"))
        b.insert(self.tr("9:00", "9:15"))
        b.insert(self.tr("10:00", "10:15"))
        b.insert(self.tr("12:30", "16:00"))
        #Sort the lists (a log a + b log b)
        a.sort()
        b.sort()
        #Subtract the arrays (a + b)
        a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        correct.insert(self.tr("9:15", "10:00"))
        correct.insert(self.tr("10:15", "11:00"))
        #Check
        self.assertTrue(correct.compare(a))
    
    def test_full_day(self):
        #Instantiate lists of time ranges
        a = TimeRangeList()
        b = TimeRangeList()
        #Load the ranges (a + b)
        a.insert(self.tr("0:00", "23:00"))
        b.insert(self.tr("9:00", "9:15"))
        b.insert(self.tr("10:00", "10:15"))
        b.insert(self.tr("11:00", "11:15"))
        b.insert(self.tr("12:00", "12:15"))
        b.insert(self.tr("13:00", "13:15"))
        b.insert(self.tr("14:00", "14:15"))
        b.insert(self.tr("15:00", "15:15"))
        #Sort the lists (a log a + b log b)
        a.sort()
        b.sort()
        #Subtract the arrays (a + b)
        a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        correct.insert(self.tr("0:00", "9:00"))
        correct.insert(self.tr("9:15", "10:00"))
        correct.insert(self.tr("10:15", "11:00"))
        correct.insert(self.tr("11:15", "12:00"))
        correct.insert(self.tr("12:15", "13:00"))
        correct.insert(self.tr("13:15", "14:00"))
        correct.insert(self.tr("14:15", "15:00"))
        correct.insert(self.tr("15:15", "23:00"))
        #Check
        self.assertTrue(correct.compare(a))

    def test_empty_case_both(self):
        #Instantiate lists of time ranges
        a = TimeRangeList()
        b = TimeRangeList()
        #Subtract the arrays (a + b)
        a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        #Check
        self.assertTrue(correct.compare(a))

    def test_empty_case_a(self):
        #Instantiate lists of time ranges
        a = TimeRangeList()
        b = TimeRangeList()
        #Load the ranges (a + b)
        a.insert(self.tr("9:00", "9:30"))
        #Subtract the arrays (a + b)
        a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        correct.insert(self.tr("9:00", "9:30"))
        #Check
        self.assertTrue(correct.compare(a))

    def test_empty_case_b(self):
        #Instantiate lists of time ranges
        a = TimeRangeList()
        b = TimeRangeList()
        #Subtract the arrays (a + b)
        a.subtract(b)
        #Load the ranges (a + b)
        b.insert(self.tr("9:00", "9:30"))
        #Subtract the arrays (a + b)
        a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        #Check
        self.assertTrue(correct.compare(a))


if __name__ == '__main__':
    unittest.main()