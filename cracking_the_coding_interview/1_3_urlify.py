#!/Users/neevekadosh/anaconda3/bin/python3

def urlify(str):
    return str.replace(" ", "%20")

if __name__=='__main__':
    # Replace spaces with %20 - should all return True
    print("hello%20" == urlify("hello "))
    print("hello%20world" == urlify("hello world"))
    print("hello%20%20world%20" == urlify("hello  world "))
