import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # A, A, A, B, C

        count_of_letters = defaultdict(int)

        for task in tasks:
            count_of_letters[task] += 1
        
        max_heap = []
        for count in count_of_letters.values():
            heapq.heappush(max_heap, -count)
        
        # max_heap = [3, 1, 1]
        time = 0
        queue = deque() # [-cnt, idletime]
        while max_heap or queue:
            time += 1
            if max_heap:
                max_frequency = heapq.heappop(max_heap) + 1
                if max_frequency < 0:
                    queue.append([max_frequency, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
                
        
        return time

        
        