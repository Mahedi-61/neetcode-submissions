class TimeMap:
    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append([value, timestamp])

    # def get(self, key: str, timestamp: int) -> str:
    #     ls_values = self.hash_map[key]
    #     if len(ls_values) == 0: return ""
        
    #     for value, time in ls_values[::-1]:
    #         if time <= timestamp:
    #             return value

    #     return ""

    def get(self, key: str, timestamp: int) -> str:
        ls_values = self.hash_map[key]
        if not ls_values: return ""

        def binary_search():
            l = 0
            r = len(ls_values) - 1

            while l <= r:
                mid = (l + r) // 2
                if timestamp < ls_values[mid][1]:
                    r = mid - 1
                elif timestamp > ls_values[mid][1]:
                    l = mid + 1
                else:
                    return ls_values[mid][0]

            if ls_values[mid][1] < timestamp:
                return ls_values[mid][0]
            else:
                mid = mid - 1
                if mid < 0:
                    return ""
                else:
                    return ls_values[mid][0]

        value = binary_search()
        return value