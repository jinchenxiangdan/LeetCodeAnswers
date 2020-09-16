# Problem C
# Below is a Python function that has one parameter variable. The function contains several comments indicating LOCATIONs in the function. After the code, there are a few statements about this code. It is your job to determine if these statements are either always true, sometimes true, or never true. In each response box, you should write one of three words: always, sometimes, or never.

def a_function(strs):
    ''' Assume that strs is a list of strings, with at least 3 elements in it. '''
    name = 'abc'
    number = 100
    count = -1
    for s in strs:
        # LOCATION A
        if len(s) > 10 or len(s) < 2:
            number += 20
            count += 2
            # LOCATION B
        elif s[0] > 'c':
            count += 1
        if s[-1] == 'z' or s[0] == 'z':
            name = s
        number += 2
        count += 1
        # LOCATION C
        print(s, name, number, count)
    # LOCATION D
    return count
# The value len(s) will be greater than 20 at LOCATION B sometimes

# The variable number will be even at LOCATION C always

# The variable count will be positive LOCATION D always

if __name__ == "__main__":
    # print('d:', a_function(['abc','bcd','cde']))
    pass
