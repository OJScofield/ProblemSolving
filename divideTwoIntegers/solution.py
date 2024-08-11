class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Edge cases
        if dividend == 0:
            return 0
        if divisor == 0:
            return 2**31 - 1  # Division by zero case, returning max integer
        
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine sign of result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values for simplicity
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        
        # Subtract divisor from dividend using bit manipulation
        while dividend >= divisor:
            temp_divisor, num_divisors = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_divisors <<= 1
            
            dividend -= temp_divisor
            quotient += num_divisors
        
        # Apply the sign to the result
        quotient = -quotient if negative else quotient
        
        # Clamp the result within the 32-bit signed integer range
        return max(min(quotient, 2**31 - 1), -2**31)
