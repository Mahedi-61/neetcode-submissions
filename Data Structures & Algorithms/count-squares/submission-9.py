class CountSquares:
    #  Duplicate points are allowed and should be treated as separate points.
    # three points and the query point form a square
    #  no diagonal squares are allowed
    def __init__(self):
        self.ls_points = []

    def add(self, point: List[int]) -> None:
        self.ls_points.append(point)

    def count(self, point: List[int]) -> int:
        count_sq = 0
        # logic here
        diagonal = []
        same_x = []
        same_y = []

        # O(n)
        for p in self.ls_points:
            if p != point:
                if point[0] == p[0]:
                    same_x.append(p[1])

                if point[1] == p[1]:
                    same_y.append(p[0])

                if abs(p[0] - point[0]) == abs(p[1] - point[1]):
                    diagonal.append(p)

        # O(d)
        for d in diagonal:
            count_x = sum([1 for s_x in same_x if s_x == d[1]])
            count_y = sum([1 for s_y in same_y if s_y == d[0]])
            count_sq += count_x * count_y

        return count_sq
