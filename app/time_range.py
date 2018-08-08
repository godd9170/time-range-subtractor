from datetime import datetime, date, time

class TimeRange:

    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def __str__(self):
        return "{0} - {1}".format(self.t1.strftime('%H:%M'), self.t2.strftime('%H:%M'))
    
    def __lt__(self, other_time_range):
        return self.t2 < other_time_range.t2
    
    def to_dict(self):
        return {
            'h1': int(self.t1.strftime('%H')), 
            'm1': int(self.t1.strftime('%M')),
            'h2': int(self.t2.strftime('%H')),
            'm2': int(self.t2.strftime('%M'))
        }

    def overlaps(self, other_time_range):
        """Given other_time_range, returns True if the ranges overlap at all"""
        return not (self.t1 > other_time_range.t2 or self.t2 < other_time_range.t1) #check for non-overlaps and negate
    
    def compare(self, other_time_range):
        """Returns True if other_time_range is identical to time range"""
        return self.t1 == other_time_range.t1 and self.t2 == other_time_range.t2

    def subtract(self, other_time_range):
        """Computes the resulting times range(s) not included in other_time_range"""
        output = []
        if (self.t1 < other_time_range.t1):
            output.append(TimeRange(self.t1, other_time_range.t1))
        
        if (self.t2 > other_time_range.t2):
            output.append(TimeRange(other_time_range.t2, self.t2))

        return output

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

    def to_array(self):
        if(self.length == 0):
            return []
        arr = []
        for time_range in self.time_ranges:
            arr.append(time_range.to_dict())
        return arr
    
    def __len__(self):
        return self.length

    def __getitem__(self, i):
        return self.time_ranges[i]

    def insert(self, new_time_range, index=None):
        """Adds a new time range to the list at the index specified, appends to the end should no index be provided"""
        if (index is not None):
            self.time_ranges.insert(index, new_time_range)
        else:
            self.time_ranges.append(new_time_range)
        self.length += 1

    def overwrite(self, new_time_range, index):
        """Replaces the time range at the provided index"""
        self.time_ranges[index] = new_time_range
    
    def delete(self, index):
        """Deletes a time range given it's index"""
        del self.time_ranges[index]
        self.length -= 1

    def sort(self):
        """Basic nlogn sort of the TimeRangeList list"""
        self.time_ranges.sort()

    def subtract(self, other_time_ranges):
        """In place update the time ranges to remove any ranges that overlap with other_time_ranges"""
        current_time_range_index = 0 #keep track of index in list a
        current_other_time_range_index = 0 #keep track of index in list b
        output = TimeRangeList()

        while(current_time_range_index < self.length and current_other_time_range_index < len(other_time_ranges)):
            if self.time_ranges[current_time_range_index].overlaps(other_time_ranges[current_other_time_range_index]): #if the two time ranges overlap
                difference = self.time_ranges[current_time_range_index].subtract(other_time_ranges[current_other_time_range_index]) #subtract the ranges
                if(len(difference) >= 1): #if there is only one range yielded 
                    self.overwrite(difference[0], current_time_range_index) #inplace replace the range
                else: #if there are no date ranges yielded 
                    self.delete(current_time_range_index) #remove the range
                    continue #skip the rest of the iteration, all iterators are correct

                if(len(difference) == 2): #if there are two ranges yielded
                    self.insert(difference[1]) #insert the second range inorder, into the range list

            
            if self.time_ranges[current_time_range_index] < other_time_ranges[current_other_time_range_index]: #if current list a's timerange ends before current list b's
                current_time_range_index += 1 #move to the next timerange in list a
            else:
                current_other_time_range_index += 1 #move to the next timerange in list b
    
    def compare(self, other_time_ranges):
        """Returns true if other_time_ranges is identical to time range list"""
        if(self.length != len(other_time_ranges)):
            return False

        for a, b in zip(self.time_ranges, other_time_ranges):
            if (not a.compare(b)):
                return False
        
        return True
