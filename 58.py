class Solution(object):
    def lengthOfLastWord(self, s):
        wordlist=s.strip().split()
        if not wordlist:
            return 0
        return len(wordlist[-1])
