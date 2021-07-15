class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def strstep(strings,x,y): 
            for i in range(x+1,min(x*2+1,y)):
                strings1 = strings[0:x] + strings[i] + strings[x+1:i] + strings[x] + strings[i+1:]
                result.append(strings1)
                if x > 1:strstep(strings1,x-1,i)
        result = []
        strings = ''
        for i in range(0,n):strings += '('
        for i in range(n,n*2):strings += ')'
        result.append(strings)
        strstep(strings,n-1,len(strings)-1)
        return result