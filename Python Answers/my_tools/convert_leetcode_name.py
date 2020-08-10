import string



################################################################################
# best way to remove punctuation in a string                                   #
################################################################################
def convert_leetcode_name(input_string: str) -> str:
    # my translation 1: remove all punctuation
    my_trans_remove = str.maketrans('', '', string.punctuation)
    # my translation 2: translate all punctuation to char "-"
    my_trans_translate = str.maketrans(string.punctuation, "-"*len(string.punctuation))
    return input_string.translate(my_trans_translate).replace(' ', '_').lower()
    

if __name__ == "__main__":
    print(convert_leetcode_name(input("input string: ")))