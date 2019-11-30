class DoubleLinkedList:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
            
    def __init__(self):
        self.head = DoubleLinkedList.Node(-999, -999)
        self.tail = DoubleLinkedList.Node(-999, -999)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add_front(self, key, val) -> 'DoubleLinkedList.Node':
        node = DoubleLinkedList.Node(key, val)
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node
        
        return node
        
    def delete(self, node: 'DoubleLinkedList.Node') -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def delete_tail(self) -> int:
        k = self.tail.prev.key
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        
        return k
        
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.list = DoubleLinkedList()
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            value = self.map[key].val
            self.list.delete(self.map[key])
            self.map[key] = self.list.add_front(key, value)
            
            return value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if len(self.map) < self.capacity:
                self.map[key] = self.list.add_front(key, value)
            else:
                # evict the least recently used item
                popped_key = self.list.delete_tail()
                # add the new item at the front
                self.map.pop(popped_key)
                self.map[key] = self.list.add_front(key, value)
        else:
            # delete the node with this key from the double linked list
            self.list.delete(self.map[key])
            # add the node with the new value to the front
            self.map[key] = self.list.add_front(key, value)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)