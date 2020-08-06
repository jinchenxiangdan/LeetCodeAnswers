import string
class Solution:
    def isPalindrome(self, s:str) -> bool:
        s = s.lower()
        # ignore all punctuations
        # s = s.replace(string.punctuation, "")
        s = s.translate(str.maketrans("","", string.punctuation))
        # ignore all spaces 
        s = s.replace(" ", "")
        print(s)
        # checking 
        for i in range(int(len(s)/2)):
            print(s[i], "<->", s[-i-1])
            if s[i] != s[-i-1]:
                return False
        return True



if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome('"A man, a plan, a canal: Panama"'))