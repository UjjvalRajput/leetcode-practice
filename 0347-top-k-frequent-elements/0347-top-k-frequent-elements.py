import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequencies of each number in nums
        # naive solution would sort by values and return k most appearing elements in O(n log n)
        acc = {}
        for num in nums:
            acc[num] = acc.get(num, 0) + 1 # replace with 0 if key not found 

        min_heap = []
        # we don't need to sort all n elements, just what is required. So:
        # maintain a min heap of size k, pop the least valued element in the min heap everytime min heap's  
        # size gets bigger than k. This is a O(n log k) operation where k is size of heap and n is len(nums)
        # at the end return the keys of all elements in the heap as those are the most frequent k values
        # because the least frequent values would be swapped out as heap is of size k.
        for key, value in acc.items(): 
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [i[1] for i in min_heap] # return the keys (actual numbers and not their values)