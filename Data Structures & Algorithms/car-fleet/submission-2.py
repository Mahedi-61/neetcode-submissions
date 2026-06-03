class Solution:
    # A car can not pass another car ahead of it. 
    # It can only catch up to another car and then drive at the same speed as the car ahead of it.

    # If a car catches up to a car fleet the moment the fleet reaches the destination, 
    # then the car is considered to be part of the fleet.

    # Return the number of different car fleets that will arrive at the destination.

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [ [p, s] for p,s in zip(position, speed)]
        cars.sort(key = lambda x: x[0], reverse=True)
        time = [ (target - c[0])/c[1] for c in cars]

        stack_fleet = []
        for t in time:

            while stack_fleet and t <= stack_fleet[-1]:
                t = stack_fleet[-1]
                stack_fleet.pop()

            stack_fleet.append(t)

        return len(stack_fleet)

