# A key is considered used if a get or a put operation is called on it.
class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} #key: Node
        self.capacity = capacity
        self.size = 0
        self.front = Node(val=0, key=0)
        self.rear = self.front

    def get(self, key: int) -> int:
        if key in self.cache:
            if self.cache[key] != self.rear:
                self.make_used(key)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            if self.cache[key] != self.rear:
                self.make_used(key)

        else:
            temp = Node(val=value, key=key)
            temp.prev = self.rear
            self.rear.next = temp

            self.cache.update({key : temp})
            self.rear = self.rear.next
            self.size += 1

        if self.size == 1:
            self.front = self.rear

        if self.size > self.capacity:
            del self.cache[self.front.key]
            self.front = self.front.next
            self.size -= 1


    def make_used(self, key):
        prev_node = self.cache[key].prev
        next_node = self.cache[key].next

        if prev_node is not None:
            prev_node.next = next_node
        
        if next_node is not None:
            next_node.prev = prev_node

        if self.front == self.cache[key]:
            self.front = next_node

        self.rear.next = self.cache[key]
        self.cache[key].prev = self.rear
        self.rear = self.rear.next
