class CountSquares:
    def __init__(self):
        self.ls_points = []
        self.pcount = {}

    def add(self, point: List[int]) -> None:
        self.ls_points.append(point)
        self.pcount[tuple(point)] = 1 + self.pcount.get(tuple(point), 0)

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for p in self.ls_points:
            if p == point: continue

            if abs(p[0] - x) == abs(p[1] - y):
                a = self.pcount[tuple([p[0], y])] if tuple([p[0], y]) in self.pcount else 0
                b = self.pcount[tuple([x, p[1]])] if tuple([x, p[1]]) in self.pcount else 0
                res += (a * b)

        return res