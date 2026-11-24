class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Understand:
        - There are two arrays, one for position and speed of each car
        - All positions will be smaller than the target
        - Fleet is a set of cars driving in the same position and same speed
        - When a car catches up to the car in front of it, it will then start driving the same speed
        - Positions will not always be in order
        - We are looking for the number of fleets that exist 
        - Cars that are bottlenecked by cars going faster them will have to join the fleet 
        Happy Case:
        - [4,1,0,7][2,2,1,1]
        -> (0,1)(1,2)(4,2)(7,1)
        -> 10, 4.5, 3, 3 so 3 and 3 will merge
        - (1,5)(4,2)
        - 2, 3
        Edge Case:
        - All cars are already a fleet
        - No cars catch up to each other (each one its own fleet): [1,2,3,4], [1,1,1,1] -> 4
        - Cars going at different speeds and paces but don't catch up to each other
        Match:
        - Sorting based on position so we can tell which cars can potentially catch up to others
        - Pair or zip position and speed together becuase we want indexes to stay the same
        - Monotonic stack to see how many cars will ever catch up
        Plan:
        - Zip position and speed together
        - Sort the cars by position
        - For each car, we're going to calculate the time it will appear : (target - position) / speed
        - If the car is lower than the car in front of it, we add to stack
        - Else, we pop all smaller cars
        - Finally, we count how many items in the stack and return
        """

        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort() # Sort the cars in increasing order
        stack = [] # Times remaining until destination per fleet
        numFleets = 0

        for p, s in cars:
            # Seconds until the car reaches the target
            timeToArrival = (target - p) / s

            # If cars toward the back of the line are estimated to reach the target
            # Faster, they'll join a later arriving fleet, so we consider these cars
            # As one now
            while stack and timeToArrival >= stack[-1]:
                stack.pop()
                numFleets -= 1

            stack.append(timeToArrival)
            numFleets += 1
        return numFleets
            


