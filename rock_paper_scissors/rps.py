#!/usr/bin/python

import sys

# - You'll want to define a list with all of the possible Rock Paper Scissors plays.
# - Another problem that asks you to generate a bunch of permutations, so we're probably
#   going to want to opt for using recursion again. Since we're building up a list of results,
#   we'll have to pass the list we're constructing around to multiple recursive calls so that
#   each recursive call can add to the overall result. However, the tests only give our
#   function `n` as input. To get around this, we could define an inner recursive helper function 
#   that will perform the recursion for us, while allowing us to preserve the outer function's 
#   function signature. 
# - In Python, you can concatenate two lists with the `+` operator. However, you'll want to make
#   sure that both operands are lists!
# - If you opt to define an inner recursive helper function, don't forget to make an initial call
#   to the recursive helper function to kick off the recursion.
# def get_all_permutations(string): 
#   data = [""] * len(string)

#   dirty_work(string, data, len(string) - 1, 0)

# def dirty_work(string, data, last, index): 
#     length = len(string) 
#     for i in range(length): 
#       data[index] = string[i] 
#       if index==last: 
#         print(data)
#       else: 
#         dirty_work(string, data, last, index+1)

def get_all_sets(data, k):
  all_sets = []
  n = len(data)  
  do_the_work(data, "", n, k, all_sets) 

  return all_sets
  
def do_the_work(data, prefix, n, k, all_sets): 
      
    # Base case: k is 0, 
    # print prefix 
    if (k == 0) : 
        all_sets.append(prefix) 
        return
  
    # One by one add all characters  
    # from set and recursively  
    # call for k equals to k-1 
    for i in range(n): 
        newPrefix = prefix + data[i]
       
        # k is decreased, because  
        # we have added a new character 
        do_the_work(data, newPrefix, n, k - 1, all_sets)

def rock_paper_scissors(num_plays):
  # output all permutations ["paper", "rock"] AND ["rock", "paper"]
  # Permutations without Repetition

  # objects = ["rock", "paper", "scisors"]
  # word =  "rpsr"
  # word1 = "rpsr"
  # word2 = "rpsp"
  # word3 = "rpsr"
  sets = get_all_sets("RPS", num_plays)
  
  print(sets)
  #for string in sets:
   # get_all_permutations(string)
  # generate all x length strings containing only one of a character
  
  #
  # objects is a word with an array of letters where letter is a string
  #            a word is   an array of letters
  # keep recursing until num_plays == 0


if __name__ == "__main__":
  # if len(sys.argv) > 1:
  #   num_plays = int(sys.argv[1])
  #   print(rock_paper_scissors(num_plays))
  # else:
  #   print('Usage: rps.py [num_plays]')

  #get_all_permutations("RPS", 5)

  rock_paper_scissors(2)