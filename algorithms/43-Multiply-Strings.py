class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: num1 or num2 is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        if len(num1) < len(num2):
            small = num1
            big = num2
        elif len(num1) > len(num2):
            small = num2
            big = num1
        else:
            small = min(num1, num2)
            big = max(num1, num2)

        results = list()
        for i in range(1, len(small) + 1):
            digitS = int(small[-i])
            carry = 0
            result = "" + (i - 1) * "0"
            for j in range(1, len(big) + 1):
                digitB = int(big[-j])
                prod = digitS * digitB + carry
                result = str(prod % 10) + result
                carry = prod // 10
            if carry > 0:
                result = str(carry) + result
            results.append(result)

        lens = list(map(len, results))
        maxLen = max(lens)
        diff = [maxLen - l for l in lens]
        results = [diff[k] * "0" + result for k, result in enumerate(results)]

        output = ""
        carry = 0
        for k in range(1, maxLen + 1):
            digits = [result[-k] for result in results]
            digits = list(map(int, digits))
            total = sum(digits) + carry
            output = str(total % 10) + output
            carry = total // 10
        if carry > 0:
            output = str(carry) + output
        return output
