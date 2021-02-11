class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def comp(x1,x2):
            k = 0
            for j in range(0,wordlend):
                if x1[j] != x2[j]:
                    k = k + 1
            if k == 1:
                return True
            else:return False
        wordlend = len(beginWord)
        wordList = set(wordList)
        ab = {beginWord}
        ae = {endWord}
        if endWord not in wordList:return 0
        else:wordList.remove(endWord)
        if beginWord in wordList:wordList.remove(beginWord)
        if comp(beginWord,endWord):return 2
        t = 3
        while ab:
            at1 = set()
            for j in ab:
                for i in wordList:
                    if comp(str(i),str(j)):
                        for z in ae:
                            if comp(str(i),str(z)):return t
                        at1.add(i)
            wordList = wordList - at1       
            if (len(wordList) == 0) or (len(at1) == 0):return 0
            if len(at1) >= len(ae):ab,ae = ae, at1
            else:ab = at1
            t = t + 1