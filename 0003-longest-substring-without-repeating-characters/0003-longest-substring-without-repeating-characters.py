class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        seen = {} # char -> count

        for right in range(len(s)):
            curr_char = s[right]
            seen[curr_char] = seen.get(curr_char, 0) + 1 # add new entry or increment
            while seen[curr_char] > 1:
                if seen[s[left]] == 1:
                    del seen[s[left]]
                else:
                    seen[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len