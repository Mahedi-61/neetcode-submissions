class CountSquares:

    def __init__(self):
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        count = 0
        test_points = self.points.copy()
        while point in test_points:
            test_points.remove(point)

        x = point[0]
        y = point[1]

        select_x = []
        select_y = []
        for p in test_points:
            if x == p[0]:
                select_x.append(p)
            if y == p[1]:
                select_y.append(p)

        for px in select_x:
            for py in select_y:
                temp = test_points.count([py[0], px[1]])
                count += temp

        return count
