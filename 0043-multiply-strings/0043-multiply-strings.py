class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is zero, just return "0"
        if num1 == "0" or num2 == "0":  # Check if any input is zero
            return "0"  # Product is zero if either input is zero

        m = len(num1)  # Store length of first string
        n = len(num2)  # Store length of second string
        res = [0] * (m + n)  # Result can be at most m+n digits (e.g., 99 * 99 = 9801)

        # Go right to left on num1
        for i in range(m - 1, -1, -1):  # Loop over each digit in num1 from rightmost
            digit1 = ord(num1[i]) - ord('0')  # Convert to int using ASCII math
            for j in range(n - 1, -1, -1):  # Loop over each digit in num2 from rightmost
                digit2 = ord(num2[j]) - ord('0')  # Convert to int
                mul = digit1 * digit2  # Multiply the two digits

                # Place the product at position i+j+1 (ones), carry at i+j (tens)
                p1 = i + j              # Position for carry
                p2 = i + j + 1          # Position for current place

                total = mul + res[p2]    # Add previous value at this place
                res[p2] = total % 10     # Place the single digit result
                res[p1] += total // 10   # Carry the tens place

        # Now, build a string from the result array, skipping leading zeros
        result_str = ""  # To hold our final result

        for num in res:   # Loop through every digit in the result array
            if len(result_str) != 0 or num != 0:  # Skip leading zeros
                result_str += str(num)   # Add digit to result string

        return result_str