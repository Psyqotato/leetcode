class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def fillstr(work):
            strings = ''
            for i in range(1,len(work)+1):
                if work[i-1] < n:strings +=  '('
                else:strings += ')'
            result.append(strings)
        def strstep(work,x,y): 
            for i in range(x+1,min(work[x]*2+1,y)):
                work1 = work[:]
                work1[x], work1[i] = work1[i], work1[x]
                fillstr(work1)
                if x > 1:strstep(work1,x-1,i)
        result = []
        work = [i for i in range(0,n*2)]
        fillstr(work)
        strstep(work,n-1,work[-1])
        return result