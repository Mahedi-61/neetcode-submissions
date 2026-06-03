class TimeMap:

    def __init__(self):
        self.recent_time = defaultdict(list)
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append(value)
        self.recent_time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            ls_stamps = self.recent_time[key]
            ls_values = self.data[key]

            if ls_stamps[0] > timestamp: return ""
            # O(log_n) solution using bs
            l, r = 0, len(ls_stamps)-1
            idx = -1
            while l <= r:
                mid = (l + r) // 2

                if timestamp > ls_stamps[mid]:
                    l = mid + 1

                elif timestamp < ls_stamps[mid]:
                    r = mid - 1
                else:
                    r = mid
                    break

            return ls_values[r]
                
        return ""