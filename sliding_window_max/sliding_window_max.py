'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k): # takes too long with large arrays (for now)
  # Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
  # Expected Output: [3,3,5,5,6,7] 
  # Explanation: 

  # Window position                Max
  # ---------------               -----
  # [1  3  -1] -3  5  3  6  7       3
  # 1 [3  -1  -3] 5  3  6  7       3
  # 1  3 [-1  -3  5] 3  6  7       5
  # 1  3  -1 [-3  5  3] 6  7       5
  # 1  3  -1  -3 [5  3  6] 7       6
  # 1  3  -1  -3  5 [3  6  7]      7
  start_idx = 0
  end_idx = k # 2nd pass changed k-1 to k
  result_arr = []

  while end_idx <= len(nums): # 2nd pass changed = to <=
    max_num = 0
    for x in range(start_idx, end_idx):
      if nums[x] > max_num or max_num == 0: # 2nd pass added "or max_num == 0"
        max_num = nums[x]
    
    result_arr.append(max_num)
    start_idx += 1
    end_idx += 1

  return result_arr # I always forget this!


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    #arr = [1, 3, -1, -3, 5, 3, 6, 7]
    #k = 3
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2  
    #output = sliding_window_max(arr, k)
    #expected = [3, 3, -1, 5, 5, 6, 7]
    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
