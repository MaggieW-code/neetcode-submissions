class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        right = 0
        mytable = {}

        s1count = [0] * 26
        s2count = [0] * 26

        if len(s1) > len(s2):
            return False
    
        for i in range(len(s1)):
            s1index = ord(s1[i])-ord('a')
            s1count[s1index] += 1 
            s2index = ord(s2[i])-ord('a')
            s2count[s2index] += 1 

        if s1count == s2count:
            return True

        point = 0
        for r in range(len(s1), len(s2)):
            removeindex = ord(s2[point])-ord('a')
            s2count[removeindex] -= 1 
            
            addindex = ord(s2[r])-ord('a')
            s2count[addindex] += 1 
            
            point += 1 
            if s1count == s2count:
                return True
        return False
