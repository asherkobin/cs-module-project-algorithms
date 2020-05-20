arr = [5, 9, 3, 7, 2, 8, 1, 6]
# split until arr for each elem
# merge pairs
# compare first elem of two arrs at a time
# increment ptr on first, write, increment ptr on second
# break it up, then merge it back

# MERGE SORT NOT IN-PLACE

def merge(A, B):
  # init the combined list that will hold the sorted elements from both A and B
  #merged = [0] * (len(A) + len(B))
  #merged = [0 for _ in range(len(A) + len(B))]
  merged = []
  
  a = 0
  b = 0

  while a < len(A) and b < len(B):
    if A[a] < B[b]:
      merged.append(A[a])
      a += 1
    elif A[a] >= B[b]:
      merged.append(B[b])
      b += 1

  # we need to add all of the elems to the merged list
  while a < len(A):
    merged.append(A[a])
    a += 1
  while b < len(B):
    merged.append(B[b])
    b += 1

  return merged



def merge_sort(arr):
  # break the array down recursively

  if len(arr) > 1:
    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])
    arr = merge(left, right)
    # print(left)
    # print(right)

  return arr

print(merge_sort(arr))



######## First Pass #########

# - Start asking question in order to go somewhere
# - Jot them before Bast, Bad, Wrong

# Find the Middle Node of A Linked List
# Write a function that, given a linked list as input, returns the middle
# node of the linked list. If the linked list contains an even number of nodes,
# return either of the middle two nodes.

## TREND can you use muliple "pointers"

# Our linked list node class looks like this:

# class Node:
#   def __init__(self, value=None, next=None):
#     self.value = value
#     self.next = next

#   def __str__(self):
#     return f'{self.value}'
# Example

# root = Node(3)
# root.next = Node(4)
# root.next.next = Node(5)
# root.next.next.next = Node(6)
# root.next.next.next.next = Node(7)

# root.find_middle()  # should return the Node with value 5

# Search In Sorted Matrix
# Given a matrix (a two-dimensional array), whose width and height do not necessarily match,
# containing distinct integers where each row is sorted and each column is also sorted, 
# write a function that searches for a target value in the matrix.
# The function should return a tuple (or two-element array) of the row and column indices
# of the target value. If the target value is not found in the array, the function should return [-1, -1].

# Sample input: 45,

# [
#     [1, 4, 7, 12, 15, 997, 999],
#     [2, 5, 19, 32, 35, 1001, 1007],
#     [3, 8, 24, 34, 36, 1008, 1015],
#     [40, 41, 42, 44, 45, 1018, 1020],
#     [98, 99, 101, 104, 190, 1021, 1025],
# ]
# Expected output: [3, 4]

# Analyze the space and time complexity of your solution.

#???
# How do we traverse and search in a matrix
# Fast Bad Wrong