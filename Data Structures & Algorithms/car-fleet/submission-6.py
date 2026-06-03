class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            t = (target - position[i]) / speed[i]
            cars.append([position[i], t])

        cars.sort(reverse=True)

        stack_fleet = []

        for (pos, time) in cars:
            if stack_fleet and time <= stack_fleet[-1]:
                pass
            else:
                stack_fleet.append(time)

        return len(stack_fleet)    


