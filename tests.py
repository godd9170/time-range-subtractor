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
        output = a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        correct.insert(self.tr("9:00", "9:30"))
        #Check
        print("{0} \"minus\" {1} = {2}".format(a,b,output))
        self.assertTrue(correct.compare(output))

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
        output = a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        #Check
        print("{0} \"minus\" {1} = {2}".format(a,b,output))
        self.assertTrue(correct.compare(output))

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
        output = a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        correct.insert(self.tr("9:00", "9:30"))
        #Check
        print("{0} \"minus\" {1} = {2}".format(a,b,output))
        self.assertTrue(correct.compare(output))

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
        output = a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        correct.insert(self.tr("9:00", "9:15"))
        correct.insert(self.tr("10:15", "10:30"))
        #Check
        print("{0} \"minus\" {1} = {2}".format(a,b,output))
        self.assertTrue(correct.compare(output))

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
        output = a.subtract(b)
        #Build correct answer time range
        correct = TimeRangeList()
        correct.insert(self.tr("9:15", "10:00"))
        correct.insert(self.tr("10:15", "11:00"))
        #Check
        print("{0} \"minus\" {1} = {2}".format(a,b,output))
        self.assertTrue(correct.compare(output))


if __name__ == '__main__':
    unittest.main()