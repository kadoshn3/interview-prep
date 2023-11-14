#!/Users/neevekadosh/anaconda3/bin/python3

def one_edit_away(str1, str2):
    if len(str1) == len(str2):
        return one_edit_replace(str1, str2)
    elif len(str1) >len(str2):
        return one_edit_insert(str1, str2)
    else:
        return one_edit_insert(str2, str1)


def one_edit_replace(str1, str2):
    found_diff = False
    for idx, value in enumerate(str1):
        if value != str2[idx]:
            # Hits only on second time it is found meaning one edit
            if found_diff:
                return False
        found_diff = True
    return True

def one_edit_insert(str1, str2):
    for

if __name__=='__main__':
    print(one_edit_away("pale", "bale"))
    print(one_edit_away("apple", "aple"))
    print(one_edit_away("aple", "apple"))