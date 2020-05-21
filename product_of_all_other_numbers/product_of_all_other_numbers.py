'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
  # input: [1, 7, 3, 4]
  # output: [84, 12, 28, 21]
  # calculation: [7*3*4, 1*3*4, 1*7*4, 1*7*3]

  output_arr = [] # this will hold the array we return

  for i in range(len(arr)): # iterate over the input
    product = 1
    tmp_num = arr[i] # save for insert
    arr.remove(tmp_num)
    for num in arr: # muliply numbers in array with tmp_num removed
      product *= num
    output_arr.append(product)
    arr.insert(i, tmp_num) # put back tmp_num
  
  return output_arr #ugh I forgot this on first attempt!


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    #arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
