class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        
        for a,b in zip(word1, word2):
            output.append(a+b)
        
        output.append(word1[len(word2):])
        output.append(word2[len(word1):])

        return ''.join(output)