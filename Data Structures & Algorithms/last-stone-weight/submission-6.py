class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)

        while len(stones) > 1:
            a, b = stones.pop(), stones.pop()
            if len(stones) == 0:
                stones.append(a - b)
                break 
                
            if a != b:
                temp = a - b
                l = 0 
                r = len(stones) - 1

                print(l, r)
                while l <= r:
                    mid = (l + r) // 2
                    if temp > stones[mid]:
                        l = mid + 1
                    elif temp < stones[mid]:
                        r = mid - 1 
                    else:
                        break
                
                if temp < stones[mid]:
                    stones.append(temp)
                    stones[mid + 1:] = stones[mid: -1]
                    stones[mid] = temp
                else:
                    stones.append(temp)
                    stones[mid + 2:] = stones[mid + 1: -1]
                    stones[mid + 1] = temp

        stones.append(0)
        return stones[0] 