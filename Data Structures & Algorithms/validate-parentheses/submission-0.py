class Solution:
    def isValid(self, s: str) -> bool:
        lis = []
        par = []
        dic = []

        for n in s:
            if n =="(" or n==")":
                par.append(n)
            if n =="[" or n=="]":
                lis.append(n)
            if n =="{" or n=="}":
                dic.append(n)
        
        if len(lis)%2 == 0 and len(par)%2 == 0 and len(dic)%2 == 0:
            return True
        else:
            return False
            
        