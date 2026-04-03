""" Mock Interview - 28th March, 2026 with Ellika """
'''
You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays startTime and 
endTime, each of length n.

These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime,
where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping, 
to maximize the longest continuous period of free time during the event.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event and they should remain non-overlapping.

Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting.


Example 1:

Input: eventTime = 5, startTime = [1,3], endTime = [2,5]

Output: 2

Input: eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]

Output: 7

Input: eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]

Output: 6

'''
# 0 1 2 3 4 5 
#  1-2 3---5 1 1
#    2 3---5

# 0 1 2 3 4 5 6 7 8 9 10
# 0-1           7-8 9-10 

# 1
# 6

# 2
# 3
# 1

from typing import List

class Solution:
    def findLongestFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        freeTimes = []
        if startTime[0] != 0:
            freeTimes.append(startTime[0])

        for i in range(1,len(startTime)):
            freeTimes.append(endTime[i] - startTime[i-1])

        if endTime[-1] != eventTime:
            freeTimes.append(eventTime - endTime[-1])

        freeTimes.sort()    // 1, 2, 3    