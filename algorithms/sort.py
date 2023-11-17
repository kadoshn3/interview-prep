#!/Users/neevekadosh/anaconda3/bin/python3

from random import randint

# O(n log(n)) Uses Tim Sort built in
def python_sort(data):
    return sorted(data)

# Nested for loop hence O(n^2)
def bubble_sort(data):
    '''Compares each adjacent element one by one,
    swapping those out of order.
    Fine for small arrays, easy to understand
    '''
    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                already_sorted = False

        if already_sorted:
            break

    return data


# O(n^2) run time tho is faster than bubble_sort
def insertion_sort(data):
    '''Shifts elements left by doing size comparison'''
    for i in range(1, len(data)):
        key_item = data[i]
        j = i - 1
        
        while j >= 0 and data[j] > key_item:
            data[j + 1] = data[j]
            j -= 1
            
        data[j + 1] = key_item
        
    return data


# Helper function for merge sort
def merge(left, right):
    '''Divide and conquer with two functions
    (1) Recursively splits input in half
    (2) Merges both halves producing sorted array
    '''
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left
    
    result = []
    
    idx_left = 0
    idx_right = 0

    while len(result) < len(left) + len(right):
        if left[idx_left] <= right[idx_right]:
            result.append(left[idx_left])
            idx_left += 1
        else:
            result.append(right[idx_right])
            idx_right += 1
        
        if idx_right == len(right):
            result += left[idx_left:]
            break
        
        if idx_left == len(left):
            result += right[idx_right:]
            break
    
    return result


# O(n log(n))
def merge_sort(data):
    if len(data) < 2:
        return data
    
    midpoint = len(data) // 2

    return merge(merge_sort(data[:midpoint]), merge_sort(data[midpoint:]))


# O(n log(n)) because for loop and recursive half
def quick_sort(data):
    '''Divide and conquer approach by dividing input
    into two lists for small and large items. 
    Lists are partitioned using a pivot then recursively
    then recursively combines everything until its sorted
    '''
    if len(data) < 2:
        return data
    
    low = []
    same = []
    high = []
    
    # Select random pivot element
    random_idx = randint(0, len(data) - 1)
    pivot = data[random_idx]
    
    for item in data:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quick_sort(low) + same + quick_sort(high)


if __name__=='__main__':
    data = [4, 2, 8, 9, 32, 1, -5, 14, 9, 12, 11, 6, 77, 39]
    print(python_sort(data))
    data = [4, 2, 8, 9, 32, 1, -5, 14, 9, 12, 11, 6, 77, 39]
    print(bubble_sort(data))
    data = [4, 2, 8, 9, 32, 1, -5, 14, 9, 12, 11, 6, 77, 39]
    print(insertion_sort(data))
    data = [4, 2, 8, 9, 32, 1, -5, 14, 9, 12, 11, 6, 77, 39]
    print(merge_sort(data))
    data = [4, 2, 8, 9, 32, 1, -5, 14, 9, 12, 11, 6, 77, 39]
    print(quick_sort(data))    
    
    