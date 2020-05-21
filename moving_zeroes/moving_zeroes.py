'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
  # Sample input: [0, 3, 1, 0, -2]
  # Expected output: 3
  # Expected output array state: [3, 1, -2, 0, 0]
  num_zeros = 0
  new_arr = []

  for num in arr: # for each num in array, if 0, increment counter, else add to new array
    if num == 0:
      num_zeros += 1
    else:
      new_arr.append(num)

  for _ in range(num_zeros): # append the count of zeros
    new_arr.append(0)

  return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")