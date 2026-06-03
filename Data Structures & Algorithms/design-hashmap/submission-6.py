class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None

class MyHashMap:
    def __init__(self):
        self.hash_map = [Node(0, 0) for _ in range(10_000)]

    def hashf(self, key):
        return key % 10_000

    def put(self, key: int, value: int) -> None:
        idx = self.hashf(key)
        head = self.hash_map[idx]

        if head.next is None:
            head.next = Node(key, value)
        else:
            curr = head.next
            while curr: 
                if key == curr.key:
                    curr.val = value
                    break
                
                if curr.next is None:
                    curr.next = Node(key, value)
                    break
                curr = curr.next


    def get(self, key: int) -> int:
        idx = self.hashf(key)
        head = self.hash_map[idx]

        if head.next:
            curr = head.next
            while curr: 
                if key == curr.key:
                    return curr.val
                curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        idx = self.hashf(key)
        head = self.hash_map[idx]

        if head.next:
            prev = head
            curr = head.next
            while curr:
                if key == curr.key:
                    prev.next = curr.next
                    break
                curr = curr.next
                prev = prev.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)