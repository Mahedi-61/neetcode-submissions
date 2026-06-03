class CountSquares:

    def __init__(self):
        self.dict_points = {}        

    def add(self, point: List[int]) -> None:
        self.dict_points[tuple(point)] = self.dict_points.get(tuple(point), 0) + 1


    def count(self, point: List[int]) -> int:
        point = tuple(point)
        count = 0

        for p in self.dict_points:
            if p != point:
                if abs(point[0] - p[0]) == abs(point[1] - p[1]):
                    first = (point[0], p[1])
                    second = (p[0], point[1])

                    if first in self.dict_points and second in self.dict_points:
                        count += self.dict_points[first] * self.dict_points[second] * self.dict_points[p]

        return count