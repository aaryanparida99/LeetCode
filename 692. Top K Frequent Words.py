class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #Error Case
        if words is None or k<=0:
            return []
        
        #Calculate Frequency
        dict = {}
        for word in words:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
                
        #Create Maxheap
        heap = []
        heapq.heapify(heap)
        for key, value in dict.items():
            heapq.heappush(heap,(-value,key))
            
        result = []
        for i in range(0,k):
            popped = heapq.heappop(heap)
            result.append(popped[1])
        
        return result
