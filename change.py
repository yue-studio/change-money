#!/usr/bin/env python

import sys

def findchange(n, coins_available, coins_so_far):
   if sum(coins_so_far) == n:
      yield coins_so_far
   elif sum(coins_so_far) > n:
      pass
   elif coins_available == []:
      pass
   else:
      for c in findchange(n, coins_available[:], coins_so_far+[coins_available[0]]):
         yield c
      for c in findchange(n, coins_available[1:], coins_so_far):
         yield c


def main():

   if (len(sys.argv) < 3 or len(sys.argv) > 3):  
      print """\
Given the cost of the product and money given (payment),
this script will show change with the least number of coins/notes. 

Usage:  change.py cost payment 
"""
      sys.exit(1)

   dollars = [1, 5, 10, 50, 100]
   cents = [1, 5, 10, 25, 50]
   product_cost = round(float(sys.argv[1]), 2)
   money_given = round(float(sys.argv[2]), 2)

   if product_cost < 0 or money_given < 0:
      print 'input need to be greater than 0'
      sys.exit(1)

   change =  money_given - product_cost
   
   print 'product cost: ', product_cost
   print 'money given: ', money_given 
   print 'change: ', change

   if change > 400:
      print 'no optimize for large changes'
      sys.exit(1)

   number_dec = float(str(change-int(change))[1:]) * 100

   if change == 0.0: 
      print 'exact change'
   elif change < 0.0:
      print 'not enough money to cover the cost'
   else:
      solutions = [s for s in findchange(int(change), dollars, [])]
      print 'change (dollars) :', min(solutions, key=len)
      if number_dec > 0:
         solutions = [s for s in findchange(int(number_dec), cents, [])]
         print 'change (cents): ', min(solutions, key=len)

if __name__== "__main__":
  main()


