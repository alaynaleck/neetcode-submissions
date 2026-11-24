class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # closest to target first
        numFleets = 0
        fleetArrival = 0

        for p, s in cars:
            timeToArrival = (target - p) / s
            if timeToArrival > fleetArrival:   # can't catch the fleet ahead
                numFleets += 1
                fleetArrival = timeToArrival
            # otherwise it joins the fleet ahead, so fleetArrival stays the same

        return numFleets



