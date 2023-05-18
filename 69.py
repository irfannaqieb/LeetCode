class Solution:
    def mySqrt(self, x: int) -> int:
        lower_lim = 1
        upper_lim = x

        if x < 2:
            return x

        while lower_lim < upper_lim:
            mid = (lower_lim + upper_lim) // 2

            if (mid * mid) == x:
                return mid
            elif (mid * mid) > x:
                upper_lim = mid
            elif (mid * mid) < x:
                lower_lim = mid + 1

        return lower_lim - 1
