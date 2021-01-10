#!/usr/bin/python3 



def couldConvert(lastWord: str, targetWord: str) -> bool:
    set1 = set()
    set2 = set()
    for char in lastWord:
        set1.add(char)
    for char in targetWord:
        set2.add(char)
    # return len(set1.difference(set2)) == 1
    if len(set1.difference(set2)) == 1:
        print(lastWord, "could be convert to", targetWord)
        return True
    else:
        return False



if __name__ == "__main__":
    print(couldConvert("leet", "lost"))
    # print(couldConvert("leet", "lost"))