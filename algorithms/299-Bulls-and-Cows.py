class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secretMap = dict()
        guessMap = dict()
        for i, num1 in enumerate(secret):
            num2 = guess[i]
            if num1 == num2:
                bulls += 1
            else:
                secretMap[num1] = secretMap.get(num1, 0) + 1
                guessMap[num2] = guessMap.get(num2, 0) + 1
        cows = 0
        for k, v in secretMap.items():
            if k in guessMap:
                cows += min(v, guessMap[k])
        return f"{bulls}A{cows}B"
