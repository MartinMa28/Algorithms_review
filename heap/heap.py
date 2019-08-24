class Heap:
    @classmethod
    def build_min_heap(cls, heap_array):
        for i in reversed(range(1, len(heap_array) // 2 + 1)):
            # i is of 1-index
            cls.min_heapify(heap_array, i)
    
        return heap_array


    @classmethod
    def min_heapify(cls, heap_array, idx_1):
        if heap_array == []:
            return
    
        left_1 = 2 * idx_1
        right_1 = 2 * idx_1 + 1

        # 1-index to 0-index
        idx = idx_1 - 1
        left = left_1 - 1
        right = right_1 - 1

        length = len(heap_array) - 1
        smallest = idx

        if left <= length and heap_array[left] < heap_array[smallest]:
            smallest = left
        if right <= length and heap_array[right] < heap_array[smallest]:
            smallest = right
        
        if smallest != idx:
            heap_array[idx], heap_array[smallest] = heap_array[smallest], heap_array[idx]
            min_heapify(heap_array, smallest + 1)



def heap_sort(arr):
    h = Heap.build_min_heap(arr)
    sorted_list = []

    while len(h) > 0:
        # swap the root with the last node
        h[0], h[-1] = h[-1], h[0]
        sorted_list.append(h.pop())
        Heap.min_heapify(h, 1)

    return sorted_list

if __name__ == "__main__":
    t = [5, 3, 1, 2, 7, 9, 8, 6, 0, 4]
    print(heap_sort(t))