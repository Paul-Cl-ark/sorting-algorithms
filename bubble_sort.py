def bubble_sort(arr):
  # loop backwards from the end of the list
  for i in range(len(arr) -1, -1, -1):

    # this value is used to break out of the list if values are
    # sorted before the last item in the range
    no_swaps = True

    # loop 'forwards' through a shortening list (end is sorted)
    for j in range(i):
       
      # check if the current element is larger than the next,
      # swap them if it is
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        # sorting is not done
        no_swaps = False

    # break out of the loop if the sorting is done early
    if no_swaps:
      print(f'Breaking at iteration {abs(i - len(arr))}!')
      break
  

  return arr

print(bubble_sort([0, 2, 99, 12, 49, 1, -1, 63, 54, 21]))
# print(bubble_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
