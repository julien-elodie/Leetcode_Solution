#!/usr/bin/env python3


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        MAX_INT = 2147483647
        MIN_INT = -2147483648

        # if a > MAX_INT or a < MIN_INT or a > MAX_INT or a < MIN_INT:

        def isPos(a):
            if MIN_INT < a < MAX_INT:
                return (a & 0xFFFFFFFF) and not (a & 0x80000000)
            else:
                return True if a == MAX_INT else False

        def isNeg(a):
            if MIN_INT < a < MAX_INT:
                return (a & 0x80000000)
            else:
                return True if a == MIN_INT else False

        def neg(a):
            return add(~a, 1)

        def isZero(a):
            if MIN_INT < a < MAX_INT:
                return not (a & 0xFFFFFFFF)
            else:
                return False

        def add(a, b):
            """
            TODO: a + b = 0 时有bug
            """
            if a == -b:
                return 0
            ret = 0
            while b:
                ret = a ^ b
                b = (a & b) << 1
                a = ret
            return a

        def sub(a, b):
            return add(a, neg(b))

        def posMulti(a, b):
            ret = 0
            while b:
                if b & 1:
                    ret = add(ret, a)
                    a = a << 1
                    b = b >> 1
            return ret

        def multi(a, b):
            if isZero(a) or isZero(b):
                return 0
            if isPos(a) and isPos(b):
                return posMulti(a, b)
            if isNeg(a):
                if isNeg(b):
                    return posMulti(neg(a), neg(b))
                else:
                    return neg(posMulti(neg(a), b))
            else:
                return neg(posMulti(a, neg(b)))

        def posDiv(a, b):
            if a < b:
                return 0
            ret = 0
            for i in range(31, -1, -1):
                if (a >> i) >= b:
                    ret += 1 << i
                    a -= b << i
            return ret

        def div(a, b):
            if isZero(b):
                raise ZeroDivisionError
            if isZero(a):
                return 0
            if isPos(a) and isPos(b):
                return posDiv(a, b)
            if isNeg(a):
                if isNeg(b):
                    return posDiv(neg(a), neg(b))
                else:
                    return neg(posDiv(neg(a), b))
            else:
                return neg(posDiv(a, neg(b)))

        ret = div(dividend, divisor)
        return MAX_INT if ret > MAX_INT else ret


if __name__ == "__main__":
    s = Solution()
    output = s.divide(1004958205, -2137325331)
    print(output)