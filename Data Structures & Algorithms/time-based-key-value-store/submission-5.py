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

            j = len(ls_stamps) - 1
            while j >= 0:
                if ls_stamps[j] <= timestamp:
                    return ls_values[j]

                j -= 1
                
        return ""
        
