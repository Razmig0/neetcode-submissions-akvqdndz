class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list =[]
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
             word = strs[i]
             word2 = strs[j]
             if len(word) == len(word2):
                if sorted(word) == sorted(word2):
                    list.append([word, word2])
        return list
        return []




    
  



        


        
            

    
        