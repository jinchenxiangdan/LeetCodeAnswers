
def titleToNumber(s: str) -> int:
    # A: 65
    # 26
    total = 0
    for index in range(len(s)):
        
        power = 26 ** index
        position = len(s)-index-1
        total += (ord(s[position])-64)*power
        
    return total


print(titleToNumber('AB'))