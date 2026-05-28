class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result +=  str(len(s)) + "#" + s
        return result
    
    def decode(self, s: str) -> List[str]:
        output = []
        i=0
        while i < len(s):
            length = 0
            word = ""
            j = i
            while s[j] != "#":
                j+=1
            if s[j-1] == "#":
                length = 1
            else:
                length = int(s[i:j])
            word = s[j+1:j+1+length]
            output.append(word)
            i = j+1+length
        return output
