class Codec:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    
    def decode(self, str):
        res = []
        i = 0
        
        while i < len(str):
            j = i 
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j+1:j+1+length])
            i = j + 1 + length
            
        return res
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))



