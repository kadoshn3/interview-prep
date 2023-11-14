#!/Users/neevekadosh/anaconda3/bin/python3

def is_unique(str):
    return len(set(str)) == len(str)

if __name__=='__main__':
    print(is_unique("abcd"))
    print(is_unique("bbda"))
    print(is_unique("apple"))
    print(is_unique("blue"))
