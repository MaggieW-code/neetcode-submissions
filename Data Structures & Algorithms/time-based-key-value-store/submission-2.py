class TimeMap:

    def __init__(self):
        self.n = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.n:
            self.n[key] = []
        self.n[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.n:
            return ""
        
        value = self.n[key]
        left = 0
        right = len(value) - 1
        while left <= right:
            mid = (right+left) // 2
            if value[mid][1] == timestamp:
                return value[mid][0]
            elif value[mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0:
            return value[right][0]
        return ""

