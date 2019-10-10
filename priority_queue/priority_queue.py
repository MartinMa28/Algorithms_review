import heapq
import itertools

pq = []                     # list of entries arranged in a heap
entry_finder = {}           # mapping of tasks to entries
REMOVED = '<removed-task>'  # placeholder for a removed task
counter = itertools.count() # unique sequence count


def add_task(task, priority=0):
    '''
    Add a new task or update the priority of an existing task
    '''
    if task in entry_finder:
        remove_task(task)
    
    entry = [priority, next(counter), task]
    entry_finder[task] = entry

    heapq.heappush(pq, entry)
    

def remove_task(task):
    '''
    Mark an existing task as REMOVED. Raise KeyError if not found.
    '''
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

