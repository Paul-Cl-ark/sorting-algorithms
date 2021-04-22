import math

def merge(arr_1, arr_2):
  merged_arr = []
  i = 0
  j = 0

  while len(merged_arr) < len(arr_1) + len(arr_2):
    if i == len(arr_1):
      merged_arr.extend(arr_2[j:])
    elif j == len(arr_2):
      merged_arr.extend(arr_1[i:])
    else:      
      if arr_1[i] < arr_2[j]:
        merged_arr.append(arr_1[i])
        i += 1
      else:
        merged_arr.append(arr_2[j])
        j += 1

  return merged_arr


def merge_sort(arr): 

  if len(arr) <= 1:
    return arr
  
  mid = math.floor(len(arr) / 2)
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  return merge(left, right)


# print(merge([1, 4, 5, 7, 11], [0, 2, 3, 4, 8, 9, 10]))
print(merge_sort([1, 5, 7, 11, -1, 0, 2, 3, 4, 8, 9, 10]))
