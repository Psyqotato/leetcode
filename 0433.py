class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def pathing(x) -> bool:
            if (x == 1):return(True)
            p = len(a3) - 1
            for i in a4[x-1]:
                if (i != a3[0]) and (set(a2[a3[p]]) > set(a2[i])):
                    a3.append(i)
                    if not pathing(x-1):a3.remove(i)
                    else:return True
            if (x < 8): 
                for i in a4[x+1]:
                    if (i != a3[0]) and (set(a2[i]) > set(a2[a3[p]])):
                        a3.append(i)
                        if not pathing(x+1):a3.remove(i)
                        else:return True
            return(False)
        banknum = len(bank)
        if (banknum == 0) or (end not in bank):return(-1)
        a1,a2,a3 = [],[],[]
        a4 = [[],[],[],[],[],[],[],[],[]]
        for j in range(0,8):
            if end[j] != start[j]:a1.append(j) 
        for i in range(0,banknum):
            b = []
            for j in range(0,8):
                if bank[i][j] != start[j]:
                    b.append(j)
            a2.append(b)
            if a2[i] == a1:a3.append(i)
            a4[len(a2[i])].append(i)
        if pathing(len(a1)):return(len(a3))
        else:return -1