import heapq

if __name__ == '__main__':
    l = [(1, 'a'), (3, 'b'), (4, 'c'), (6, 'd'), (2, 'e'), (7, 'f'), (5, 'g')]
    heapq.heapify(l)
    print(l)
    # update the priority
    l[len(l) - 1] = (-1, 'g')
    print(l)
    heapq._siftdown(l, 0, len(l) - 1)
    print(l)

