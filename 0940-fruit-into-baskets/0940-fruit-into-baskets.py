class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        accumulator = 0
        state = {}
        for end in range(len(fruits)):
            state[fruits[end]] = state.get(fruits[end], 0) + 1 # {2:1, 4:2, 5:3, ...,}
            while len(state) > 2:
                state[fruits[start]] -= 1
                if state[fruits[start]] == 0:
                    del state[fruits[start]]
                start += 1
            accumulator = max(accumulator, end - start + 1) # len([2, 3, 4, 4]) = (index 3 - index 0) + 1 = 4
        return accumulator