import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        acc = {}
        for num in nums:
            acc[num] = acc.get(num, 0) + 1

        min_heap = []
        for key, value in acc.items():
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [i[1] for i in min_heap]