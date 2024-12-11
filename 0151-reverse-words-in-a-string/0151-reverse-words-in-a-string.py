class Solution:
    def reverseWords(self, s: str) -> str:
        words =[]
        word = ''
        
        for c in s:
            if c != ' ':
                word += c
                
            else:
                if word:
                    words.append(word)
                    word= ''  # initialize word string
        if word:
            words.append(word)
                    
        res = ''
        
        for i in range(len(words)-1, -1, -1):
            res += words[i]
            
            if i > 0:
                res += ' '
            
        return res
                    
        
        
                