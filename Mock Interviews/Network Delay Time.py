""" Mock Interview with Hitha - May 14th, 2026 """
""" 
Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, 
a list of travel times as directed edges times[i] = (ui, vi, wi), 
where ui is the source node, vi is the target node, and wi is the time it 
takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it 
takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.

"""
from typing import List
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, target, time in times:
            adj[source].append([time, target])
            
        visited = set()
        counter = 0
        res = 0
        heap = []
        heapq.heappush(heap, [0,k])
        
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            counter += 1
                
            for t, nei in adj[node]:
                if nei in visited:
                    continue
                heapq.heappush(heap, [time + t, nei])
            visited.add(node)
            res = max(res, time)
            
        if counter == n:
            return res
        else:
            return -1

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
times = [[1,2,1]]
n = 2
k = 1
times = [[1,2,1]]
n = 2
k = 2

obj = Solution()
print(obj.networkDelayTime(times, n, k))