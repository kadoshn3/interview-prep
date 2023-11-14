#!/Users/neevekadosh/anaconda3/bin/python3

NO_CHARS = 256

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    count_1 = [0] * NO_CHARS
    count_2 = [0] * NO_CHARS
    
    for asci in str1:
        count_1[ord(asci)] += 1
    for asci in str2:
        count_2[ord(asci)] += 1

    return count_1 == count_2

if __name__=='__main__':
    print(check_permutation("daavd", "addav"))
    print(check_permutation("abcdv", "addav"))
    print(check_permutation("vaadd", "addav"))
