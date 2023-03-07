def merge_sort(string: list):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = merge_sort(string[:mid])
    right = merge_sort(string[mid:])
    return merge(left, right)

def merge(left: list, right: list):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def is_anagram(first_string, second_string):
    first_sort = ''.join(merge_sort(list(first_string.lower())))
    second_sort = ''.join(merge_sort(list(second_string.lower())))
    is_anagram = (first_sort == second_sort and bool (first_string) and bool (second_string))
    return (first_sort, second_sort, is_anagram)
