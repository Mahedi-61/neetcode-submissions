class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def left_child(self, index):
        return 2*index + 1

    def right_child(self, index):
        return 2*index + 2

    def parent(self, index):
        return (index-1) // 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, val):
        self.heap.append(val)
        index = len(self.heap) - 1
        parent = self.parent(index)

        while(parent >= 0 and self.heap[index] > self.heap[parent]):
            self.swap(index, parent)
            index = parent
            parent = self.parent(index)

    def sink_down(self, index):
        while(True):
            max_index = index
            left_index = self.left_child(index)
            if  left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            right_index = self.right_child(index)
            if  right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if index != max_index:
                self.swap(index, max_index)
                index = max_index
            else: 
                break

    def remove(self):
        if not self.heap:
            return None 

        elif len(self.heap) == 1:
            return self.heap.pop()

        else:
            max_val = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.sink_down(0)
            return max_val

import heapq
from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        while len(stones) > 1:
            stones.sort()

            diff = stones.pop() - stones.pop()
            if diff !=0: stones.append(diff)

        return 0 if len(stones) == 0 else stones[-1] 



