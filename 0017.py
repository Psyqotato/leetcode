
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':return []
        work =  ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        nums = [(int(i) - 2) for i in digits]
        res = []
        def trans(num,res):
            res1 = []
            if res == []:
                for i in range(len(work[nums[0]])):
                    res1.append(work[nums[0]][i])
            else:
                for i in range(len(res)):
                    for j in range(len(work[num[0]])):
                        res1.append(res[i] + work[num[0]][j])
            num.remove(num[0])
            if num == []:return res1
            else:return trans(num,res1)
        return trans(nums,res)