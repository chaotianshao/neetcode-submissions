class TimeMap:

    def __init__(self):
        self.mp={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mp:
            self.mp[key].append([value, timestamp])
        else:
            self.mp[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        else:
            left = 0
            right = len(self.mp[key]) - 1
            ans = ""
            while left <= right:
                mid = left + (right - left) // 2

                if self.mp[key][mid][-1] <= timestamp:
                    ans = self.mp[key][mid][0]
                    left = mid + 1
                else:
                    right = mid - 1
            
            return ans
        
