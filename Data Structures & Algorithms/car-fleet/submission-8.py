class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # t = 9/3 = 3
        # t = 6/2 = 3
        cars = []
        ls_times = [(p, (target-p)/v) for p, v in zip(position, speed)]
        ls_times.sort(reverse=True)
        max_time = 0
        
        for pair in ls_times:
            p, t = pair
            if len(cars) == 0:
                cars.append(t)
                max_time = t

            if max_time < t:
                cars.append(t)
                max_time = t

        return len(cars)

            


        


