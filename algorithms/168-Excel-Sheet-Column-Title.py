class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = ""
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        while columnNumber > 0:
            mod = columnNumber % 26 - 1
            output = alphabet[mod] + output
            columnNumber = columnNumber // 26
            if mod == -1:
                columnNumber -= 1
        return output
