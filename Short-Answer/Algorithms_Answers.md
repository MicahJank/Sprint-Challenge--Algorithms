#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
 a = 0
    while (a < n * n * n):
      a = a + n * n
a) - runtime is O(n) because the number of steps we need to perform is proportional to the size of n
i.e if n is size 4 the while loop has to run 4 times...if n is size 100 the loop would then have to run 100 times


sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
b) - i believe that the while loop inside the for loop has a runtime of O(log n) because on every iteration the size of j doubles which is equivalent to saying that the time it takes the while loop to finish is getting halved with each iteration. However since the while loop is inside a for loop and the for loops runtime is O(n) then the total runtime must be O(n log n)



def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
c) - i believe the runtime for this recursive function is O(n) because on every recursive call the size of n(in this case 'bunnies) is decremented by exactly 1. This means that the number of recursive calls is directly proportional to the size of bunnies, i.e linear time

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


ANSWER
The point is to find the highest level floor where dropping and egg wont break it. In other words we need to find where the nth level of the building is equal to 'f'.
I believe implementing a binary type search is the best method for this. I could start by finding the middle floor in the building - len(n) // 2 - and then use a while loop to keep checking if the floor 'f' is equal to the middle. if the middle floor is higher than i just need to keep halving the number until i either reach the same number as f or the middle floor becomes lower than f. If the middle floor is lower than i would need to take the difference between the end and the middle and halve that and add that value to the middle an recheck.
runtime complexity is O(log n)
