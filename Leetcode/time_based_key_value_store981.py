class TimeMap:

    def __init__(self):
        # self.key_val_dict = defaultdict(list)
        self.key_val_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_val_dict:
            self.key_val_dict[key] = []
        self.key_val_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, timestamp_val_tuple = "", self.key_val_dict.get(key, [])
        l, r = 0, len(timestamp_val_tuple) - 1
        while l <= r:
            m = (l + r) // 2

            current_timestamp = timestamp_val_tuple[m][0]
            current_val = timestamp_val_tuple[m][1]

            if current_timestamp <= timestamp:
                res = current_val
                l = m + 1
            else:
                r = m - 1
        return res
