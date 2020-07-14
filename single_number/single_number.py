'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    non_dupes = []

    for x in arr: # for every number in the array
      if x not in non_dupes: # if number not in dupe array
        non_dupes.append(x) # add number to dupe array
      else:
        non_dupes.remove(x) # number seen again, remove from dupe array

    return non_dupes[0] # assuming the conditions are met, there should only be one non-duplicated number

def single_number_better(arr):
  # use dictionary instead of array!!
  counts = {}

  for x in arr:
    if x in counts:
      counts[x] += 1
    else:
      counts[x] = 1

  for key in counts:
    if counts[key] == 1:
      return key

arr = []

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2]

    print(f"The odd-number-out is {single_number(arr)}")
