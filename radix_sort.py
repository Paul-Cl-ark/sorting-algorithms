import math

def get_digit(number, index):
  return math.floor(abs(number) / math.pow(10, index)) % 10

def get_digit_count(number):
  return 1 if number == 0 else math.floor(math.log10(abs(number))) + 1

def get_max_digit_count(arr):
  return max(get_digit_count(number) for number in arr)

def radix_sort(arr):
  for i in range(get_max_digit_count(arr)):
    value_bucket = [[] for digit_bucket in range(0, 10)]

    for j in arr:
      value_bucket[get_digit(j, i)].append(j)
    
    arr = [value for inner_arr in value_bucket for value in inner_arr]

  return arr

# print(get_digit(12345, 6))
# print(get_digit_count(12345678))
# print(get_max_digit_count([1, 2, 3, 400, 5000, 71234, -1, -123456]))

# print(radix_sort([0, 2, 99, 12, 200, 430, 49, 1, 1239012, 31, 63, 54, 21, 12039]))
print(radix_sort([23,345,5467,12,-2345,9852]))
