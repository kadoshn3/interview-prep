#!/Users/neevekadosh/anaconda3/bin/python3

# Best case O(1) worst case O(n)
def linear_search(data, value):
    for idx in range(len(data)):
        if data[idx] == value:
            return idx
    
    return -1

# Runtime is O(log(n)) Space is O(1)
def iterative_binary_search(data, value):
    left = 0
    right = len(data) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if data[mid] == value:
            return mid
        
        elif data[mid] < value:
            left = mid + 1
            
        else: 
            right = mid - 1
    
    return -1


def recursive_binary_search(data, left, right, value):
    if right >= left:
        mid = left + (right - left) // 2
        
        if data[mid] == value:
            return mid

        elif data[mid] > value:
            return recursive_binary_search(data, left, mid-1, value)
        
        else:
            return recursive_binary_search(data, mid + 1, right, value)
    
    else:
        return -1

if __name__=='__main__':
    data = [4, 2, 8, 9, 32, 1, -5, 14, 102, 12, 11, 6, 77, 39]
    value = 14
    sorted_data = sorted(data)
    print(sorted_data)
    print("Expected index is 9")
    print("Linear Search:", linear_search(sorted_data, value))
    print("Iterative Binary Search:", iterative_binary_search(sorted_data, value))
    print("Recursive Binary Search:", recursive_binary_search(sorted_data, 0, len(data) - 1, value))
    