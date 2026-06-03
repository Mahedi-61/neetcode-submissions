class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Greedy solution
        # stones = [-1*stone for stone in stones]
        # heapq.heapify(stones)

        # while True:
        #     if len(stones) == 1:
        #         return stones[0]
        #     elif len(stones) == 0:
        #         return 0
        #     else:
        #         a, b = heapq.heappop(stones), heapq.heappop(stones)
        #         a, b = abs(a), abs(b)
        #         print(a, b)
        #         if a != b:
        #             heapq.heappush(stones,  abs(a - b))

        # need dp solution (more optimized for this problem)
        # 1. Compute total sum.
        # 2. Use DP to compute all subset sums ≤ total // 2.
        # 3. Find the max achievable sum ≤ total // 2.
        # 4. Final result is total - 2 * max_sum.

        total_sum = sum(stones)
        all_sums = set([0, stones[0]]) #dp
        new_sum = set()

        for s in stones[1:]:
            for a_sum in all_sums:
                new_sum.add(a_sum + s)
            all_sums.update(new_sum)

        print(all_sums)
        max_sum = max(s for s in all_sums if s <= total_sum //2)
        return total_sum - 2 * max_sum
