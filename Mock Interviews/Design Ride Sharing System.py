""" Mock Interview with Ellika - 13th April, 2026 """
"""
A ride sharing system manages ride requests from riders and availability from drivers. 
Riders request rides, and drivers become available over time. The system should match riders and drivers in the order they arrive.

Implement the RideSharingSystem class:

RideSharingSystem() Initializes the system.
void addRider(int riderId) Adds a new rider with the given riderId.
void addDriver(int driverId) Adds a new driver with the given driverId.
int[] matchDriverWithRider() Matches the earliest available driver with the earliest waiting rider and removes both of them from the system. 
Returns an integer array of size 2 where result = [driverId, riderId] if a match is made. If no match is available, returns [-1, -1].
void cancelRider(int riderId) Cancels the ride request of the rider with the given riderId if the rider exists and has not yet been matched.

Example 1:

Input:
["RideSharingSystem", "addRider", "addDriver", "addRider", "matchDriverWithRider", "addDriver", "cancelRider", "matchDriverWithRider", "matchDriverWithRider"]
[[], [3], [2], [1], [], [5], [3], [], []]

Output:
[null, null, null, null, [2, 3], null, null, [5, 1], [-1, -1]]

Explanation

RideSharingSystem rideSharingSystem = new RideSharingSystem(); // Initializes the system
rideSharingSystem.addRider(3); // rider 3 joins the queue
rideSharingSystem.addDriver(2); // driver 2 joins the queue
rideSharingSystem.addRider(1); // rider 1 joins the queue
rideSharingSystem.matchDriverWithRider(); // returns [2, 3]
rideSharingSystem.addDriver(5); // driver 5 becomes available
rideSharingSystem.cancelRider(3); // rider 3 is already matched, cancel has no effect
rideSharingSystem.matchDriverWithRider(); // returns [5, 1]
rideSharingSystem.matchDriverWithRider(); // returns [-1, -1]

"""
from collections import deque

class RideSharingSystem:
    def RideSharingSystem(self):
        self.cancelledRides = set()
        self.rideRequests = deque()
        self.driversAvailable = deque()
        
    def addRider(self, riderId): # O(1)
        self.rideRequests.append(riderId)
        
    def addDriver(self, driverId): # O(1)
        self.driversAvailable.append(driverId)
        
    def matchDriverWithRider(self): # O(N)
        if not self.rideRequests or not self.driversAvailable:
            return [-1, -1]
        rider = self.rideRequests.popleft()
        while rider in self.cancelledRides:
            if not self.rideRequests:
                return [-1,-1]
            rider = self.rideRequests.popleft()
        driver = self.driversAvailable.popleft()
        return [driver, rider]
        
    def cancelRider(self, riderId): # O(1)
        self.cancelledRides.add(riderId)
        
        
sol = RideSharingSystem()
sol.RideSharingSystem()
sol.addRider(3)
sol.addDriver(2)
sol.addRider(1)
print(sol.matchDriverWithRider())
sol.addDriver(5)
sol.cancelRider(3)
print(sol.matchDriverWithRider())
print(sol.matchDriverWithRider())
        
        