#!/usr/bin/python

import sys
  
def do_the_work(options, arr, num_plays, possible_plays): 
  if num_plays == 0: 
    possible_plays.append(arr)
    return

  for i in range(len(options)):
    new_arr = arr.copy()
    new_arr.append(options[i])
    
    do_the_work(options, new_arr, num_plays - 1, possible_plays)

def rock_paper_scissors(num_plays):
  options = ["rock", "paper", "scissors"] # can be any number of words
  possible_plays = []

  do_the_work(options, [], num_plays, possible_plays) 

  return possible_plays 

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
  
  # print(rock_paper_scissors(3))