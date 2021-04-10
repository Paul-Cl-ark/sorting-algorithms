def insertion_sort(arr):
  for i in range(len(arr) -1):
    j = i + 1
    # while the value at index j is greater than the element at the index before it
    while j >= 1 and arr[j] < arr[j -1]:
      # swap the values of the 2 indices
      arr[j], arr[j-1] = arr[j-1], arr[j]
      # decrement j
      j -= 1

  return arr

print(insertion_sort([2, 0, 99, 12, 49, 1, -1, 63, 54, 21]))
# print(insertion_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
