class CountSquares:
    def __init__(self):
        self.ls_points = []

    def add(self, point: List[int]) -> None:
        self.ls_points.append(point)

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for p in self.ls_points:
            if p == point: continue

            if abs(p[0] - x) == abs(p[1] - y):
                a = self.ls_points.count([p[0], y])
                b = self.ls_points.count([x, p[1]])

                res += (a * b)

        return res