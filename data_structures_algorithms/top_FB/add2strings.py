class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1

        sum_ = ""
        carry = 0

        while i >= 0 and j >= 0:
            s = int(num1[i]) + int(num2[j])
            if carry == 1:
                s += 1
            if s >= 10:
                carry = 1
            else:
                carry = 0
            sum_ += str(s % 10)

            i -= 1
            j -= 1

        while i >= 0:
            s = int(num1[i]) + carry
            if s >= 10:
                carry = 1
            else:
                carry = 0
            sum_ += str(s % 10)
            i -= 1

        while j >= 0:
            s = int(num2[j]) + carry
            if s >= 10:
                carry = 1
            else:
                carry = 0
            sum_ += str(s % 10)
            j -= 1

        if carry == 1:
            sum_ += "1"

        return str(sum_[::-1])

    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1

        sum_ = ""
        carry = 0
        while i >= 0 and j >= 0:
            s = int(a[i]) + int(b[j])
            if carry == 1:
                s += 1
            if s > 1:
                carry = 1
                sum_ += str(s % 2)
            else:
                carry = 0
                sum_ += str(s % 2)

            i -= 1
            j -= 1

        while i >= 0:
            s = int(a[i])
            if carry == 1:
                s += 1
            if s > 1:
                carry = 1
                sum_ += '0'
            else:
                carry = 0
                sum_ += str(s % 2)
            i -= 1

        while j >= 0:
            s = int(b[j])
            if carry == 1:
                s += 1
            if s > 1:
                carry = 1
                sum_ += '0'
            else:
                carry = 0
                sum_ += str(s % 2)
            j -= 1

        if carry == 1:
            sum_ += '1'

        return sum_[::-1]