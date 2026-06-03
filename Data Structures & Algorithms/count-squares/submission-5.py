class CountSquares:
    # The square must have all sides parallel to the x-axis and y-axis
    # Counts the number of ways to form valid squares with point point = [x, y]
    # Duplicate points are allowed and should be treated as separate points.
    # 0 <= x, y <= 1000

    def __init__(self):
        self.ls_points = []

    def add(self, point: List[int]) -> None:
        self.ls_points.append(point)

    def count(self, point: List[int]) -> int:
        x, y = point
        ls_x = []
        ls_y = []
        for p in self.ls_points:
            if p == point: continue
            
            if p[0] == x: ls_x.append(p)
            if p[1] == y: ls_y.append(p)

        res = 0
        for p in self.ls_points:
            x, y = p
            for x_p in ls_x:
                for y_p in ls_y:
                    if x_p[1] == y and y_p[0] == x:
                        res += 1
        return res