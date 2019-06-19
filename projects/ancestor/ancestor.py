class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_vertex):
    parent_set = {}

    for x in ancestors:
        if x[0] not in parent_set:
            parent_set[x[0]] = set()
        
        parent_set[x[0]].add(x[1])

    visited = set()
    earliest_ancestor = [-1]
    q = Queue()
    q.enqueue( [starting_vertex] )
    
    while q.size() > 0:
        v = q.dequeue()
        
        if len(v) > len(earliest_ancestor):
            earliest_ancestor = v

        if v[-1] not in visited:
            visited.add(v[-1])
            
            for parent, child in parent_set.items():
                child_list = list(child)

                for child in child_list:
                    if child == v[-1]:
                        path = v.copy()
                        path.append(parent)
                        q.enqueue(path)
    
    return earliest_ancestor[-1]