from datetime import datetime, date, time

class TimeRange:

    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def __str__(self):
        return "{0} - {1}".format(self.t1.strftime('%H:%M'), self.t2.strftime('%H:%M'))
    
    def __lt__(self, other_time_range):
        return self.t2 < other_time_range.t2

    def overlaps(self, other_time_range):
        return not (self.t1 > other_time_range.t2 or self.t2 < other_time_range.t1) #check for non-overlaps and negate
    
    def compare(self, other_time_range):
        return self.t1 == other_time_range.t1 and self.t2 == other_time_range.t2

    def subtract(self, other_time_range, time_range_list):
        if (self.t1 < other_time_range.t1):
            time_range_list.insert(TimeRange(self.t1, other_time_range.t1))
        
        if (self.t2 > other_time_range.t2):
            time_range_list.insert(TimeRange(other_time_range.t2, self.t2))

        return time_range_list

class TimeRangeList:

    def __init__(self):
        self.time_ranges = []
        self.length = 0

    def __str__(self):
        if(self.length == 0):
            return "()"

        pretty = "{0}".format(self.time_ranges[0])
        for time_range in self.time_ranges[1:]:
            pretty += ", {0}".format(time_range)
        return "({})".format(pretty)
    
    def __len__(self):
        return self.length

    def __getitem__(self, i):
        return self.time_ranges[i]

    def insert(self, new_time_range):
        self.time_ranges.append(new_time_range)
        self.length += 1

    def sort(self):
        self.time_ranges.sort()

    def subtract(self, other_time_ranges):
        current_time_range_index = 0 #keep track of index in list a
        current_other_time_range_index = 0 #keep track of index in list b
        output = TimeRangeList()

        while(current_time_range_index < len(self.time_ranges) and current_other_time_range_index < len(other_time_ranges)):
            if self.time_ranges[current_time_range_index].overlaps(other_time_ranges[current_other_time_range_index]): #if the two time ranges overlap
                self.time_ranges[current_time_range_index].subtract(other_time_ranges[current_other_time_range_index], output) #subtract the ranges and adds to output
            
            if self.time_ranges[current_time_range_index] < other_time_ranges[current_other_time_range_index]: #if current list a's timerange ends before current list b's
                current_time_range_index += 1 #move to the next timerange in list a
            else:
                current_other_time_range_index += 1 #move to the next timerange in list b

        return output
    
    def compare(self, other_time_ranges):
        if(self.length != len(other_time_ranges)):
            return False

        for a, b in zip(self.time_ranges, other_time_ranges):
            if (not a.compare(b)):
                return False
        
        return True