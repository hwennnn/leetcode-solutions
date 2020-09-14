class Solution:
    def insert(self, intervals, newInterval):
        """
        Given an ordered list of intervals and a new interval,
        this program inserts the new interval into the ordered
        list of intervals while incorporating mergers of intervals
        where appropriate.

        :param intervals: array of intervals where each interval
                          is a [start, end] pair and the intervals
                          are sorted by their start points
        :type intervals: list[list[int]]
        :param newInterval: interval to be inserted into intervals
        :type newInterval: list[int]
        :return: updated array of intervals
        :rtype: list[list[int]]
        """
        new_intervals_front = []
        new_intervals_back = []
        new_begin, new_end = newInterval
        for ibegin, iend in intervals:
            if iend < new_begin:
                """
                [ibegin, iend] occurs before newInterval without
                overlap.
                """
                new_intervals_front.append( [ibegin, iend] )
            elif ibegin < new_begin:
                if iend <= new_end:
                    """
                    [ibegin, iend] precedes and overlaps newInterval,
                    but does not exceed newInterval
                    """
                    new_begin = ibegin
                else:
                    """
                    newInterval resides within [ibegin, iend]
                    """
                    return intervals
            elif ibegin >= new_begin and iend <= new_end:
                """
                [ibegin, iend] resides within newInterval
                """
                pass
            elif new_begin <= ibegin <= new_end and iend > new_end:
                """
                [ibegin, iend] overlaps and exceeds newInterval
                """
                new_end = iend
            else:
                """
                [ibegin, iend] exceeds, but does not overlap
                newInterval
                """
                new_intervals_back.append( [ibegin, iend] )
        insert_interval = [new_begin, new_end]
        return new_intervals_front + [insert_interval] + new_intervals_back