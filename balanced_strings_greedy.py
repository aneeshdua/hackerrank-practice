class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res=0
        strt=0
        end=2
        while(end<=len(s)):
            temp = s[strt:end]
            if(temp.count('L')==temp.count('R')):
                res = res+1
                start = end
                end = start+2
            else:
                end = end+2
        return res                
