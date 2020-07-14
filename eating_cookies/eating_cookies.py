'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):  # the initial n must greater than 3 (solution: write outer fn for bounds checking)
  if n == 0:
    return 1 # by definition there is one way to eat zero cookies
  elif n < 0:
    return 0 # no cookies to eat
  #1
  one_cookies = eating_cookies(n - 1) # one less cookie
  #2
  two_cookies = eating_cookies(n - 2) # two less cookies
  #3
  three_cookies = eating_cookies(n - 3) # three less cookies
  #4 - for fun (ignored)
  # four_cookies = eating_cookies(n - 4) # four less cookies
  # _ _ _ _ _
  # 4=> 7
  # 5=> 2(1+1), 4(3+1), 7(6+1)        13
  # 6=> 2(1+1), 4(3+1), 7(6+1) , 11   24
  #(1^0 + 1) + 
#(5^3+5^2+5^1)/12

#[4,3] 7
#[5,3] 13
#[6,3] 24
#[7,3] 44

# [3]
  #print("Four Cookies: " + str(four_cookies))
  return one_cookies + two_cookies + three_cookies # return sum of each set

def eating_cookies_optimized(n, cache):
    #print(n)

    if n == 0:
      return 1
    elif n <= 0:
      return 0
    elif cache and cache[n] > 0:
      return cache[n]
    else:
      if not cache:
        cache = [0 for _ in range(n+1)]
      cache[n] = eating_cookies_optimized(n - 1, cache) + eating_cookies_optimized(n - 2, cache) + eating_cookies_optimized(n - 3, cache)
    return cache[n]
    
#4
    # x + (x + 6) + (x + 6 + 6) + (x + 6 + 6 + 6) + (x + 6 + 6 + 6 + 6) = 100
    # 5x + 60 = 100
    # 5x = 40
    # x = 8 cookies.
    # sum = 0
    # for x in range(n):
    #   sum += x + 0

      # the number of ways to eat n cookies (at most 3 at a time) is equal to...
    # the number of ways to first eat 3 cookies at once right now + the number of ways to eat the remaining cookies later
    # ways_if_3_cookies_eaten_first = eating_cookies_unoptimized(n - 3)
    # # the number of ways to first eat 2 cookies at once right now + the number of ways to eat the remaining cookies later
    # ways_if_2_cookies_eaten_first = eating_cookies_unoptimized(n - 2)
    # # the number of ways to first eat a single cookie right now + the number of ways to eat the remaining cookies later
    # ways_if_1_cookie_eaten_first = eating_cookies_unoptimized(n - 1)
    # return ways_if_3_cookies_eaten_first + ways_if_2_cookies_eaten_first + ways_if_1_cookie_eaten_first

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 6

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

print("0: " + str(eating_cookies(0))) #invalid
print("1: " + str(eating_cookies(1))) #invalid
print("2: " + str(eating_cookies(2))) #invalid
print("3: " + str(eating_cookies(3))) #invalid should be 1 but returns 4
print("4: " + str(eating_cookies(4)))
print("5: " + str(eating_cookies(5)))
print("6: " + str(eating_cookies(6)))
print("7: " + str(eating_cookies(7)))
#print(eating_cookies_optimized(500, None))

1^5
2^5
3^5