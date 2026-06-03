class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i, j = 0, 3
        collection = set()

        while j <= len(num):
            sub_str = num[i : j]

            if len(set(sub_str)) == 1:
                collection.add(sub_str)

            i += 1
            j += 1

        if len(collection) == 0: return ""

        max_num = float('-inf')
        for num in collection:
            max_num = max(max_num, int(num))

        return str(max_num) if max_num != 0 else "000"


