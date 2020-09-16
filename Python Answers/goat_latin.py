class Solution:
    def toGoatLatin(self, S: str) -> str:

        vowels = ['a', 'e', 'i', 'o', 'u']
        output = ''
        strings = S.split()
        
        for i in range(len(strings)):
            temp = strings[i]
            #   If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
            #   For example, the word 'apple' becomes 'applema'.
            if temp[0].lower() in vowels:
                temp += 'ma'
            # If a word begins with a consonant (i.e. not a vowel), remove the first letter and append 
            # it to the end, then add "ma".
            # For example, the word "goat" becomes "oatgma"
            else:
                temp = temp[1:] + temp[0]
                temp += 'ma'
            temp += ('a'*(i+1))
            # Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
            # For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
            if i+1 < len(strings):
                output += temp + ' '
            else:
                output += temp
        return output
                

        
        
        

        
        
if __name__ == "__main__":
    s = Solution()
    print(s.toGoatLatin('I speak Goat Latin'))