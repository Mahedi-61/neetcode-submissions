class TimeMap:
    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ls_values = self.hash_map[key]
        if len(ls_values) == 0: return ""
        
        for value, time in ls_values[::-1]:
            if time <= timestamp:
                return value

        return ""