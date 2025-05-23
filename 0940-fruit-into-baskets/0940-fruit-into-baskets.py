class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {} # fruit_type -> times_seen
        max_len = 0
        start = 0

        for end in range(len(fruits)):
            fruit = fruits[end]
            basket[fruit] = basket.get(fruit, 0) + 1 # new entry or increment
            while len(basket) >= 3:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
            max_len = max(max_len, end - start + 1)

        return max_len

