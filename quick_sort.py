def pivot(arr, start, end):
  pivot_index = start

  for index in range(start + 1, len(arr)):
    if arr[start] > arr[index]:
      pivot_index += 1
      arr[pivot_index], arr[index] = arr[index], arr[pivot_index]

  arr[pivot_index], arr[start] = arr[start], arr[pivot_index]

  return pivot_index


def quick_sort(arr, left = None, right = None):
  if left is None: left = 0
  if right is None: right = len(arr) - 1

  if left < right:
    print(arr, left, right)
    pivot_index = pivot(arr, left, right)
    quick_sort(arr, left, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, right)

  return arr


# print(pivot([21, 2, 99, 12, 49, 1, -1, 63, 54, 0, 73]))
print(quick_sort([21, 2, 99, 12, 49, 1, -1, 63, 54, 0, 73]))
