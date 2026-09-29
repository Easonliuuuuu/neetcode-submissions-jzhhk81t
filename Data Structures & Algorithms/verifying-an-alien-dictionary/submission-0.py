class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        o = {}
        for i in range(26):
            o[order[i]] = i
        l = len(words)
        for i in range(l - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if o[words[i + 1][j]] < o[words[i][j]]:
                    return False
                elif o[words[i + 1][j]] > o[words[i][j]]:
                    break
                if j == min(len(words[i]), len(words[i + 1])) - 1:
                    if len(words[i]) > len(words[i + 1]):
                        return False
            
        return True 