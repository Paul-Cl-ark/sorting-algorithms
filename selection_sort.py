def selection_sort(arr):

  # loop through each item in the list
  for i in range(len(arr)):
    # set the current index to be the lowest value
    lowest = i

    # create a second index to compare to the current lowest
    j = i +   1 
    # loop through the rest of the list (maintaining the original indexes)
    while j < len(arr):
      # if the element at the current index is lower than that element
      # at the outer index, set it to be the lowest
      if arr[lowest] > arr[j]:
        lowest = j
      
      # increment the loop  
      j += 1

    # this is the outer loop - swap the lowest index found in the inner
    # loop for the index in the outer loop (if it's smaller)
    if i != lowest:
      arr[i], arr[lowest] = arr[lowest], arr[i]
    
  return arr

print(selection_sort([0, 2, 99, 12, 49, 1, -1, 63, 54, 21]))
# print(selection_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
