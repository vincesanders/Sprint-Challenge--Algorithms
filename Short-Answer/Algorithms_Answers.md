#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - Even though the while loop iterates to n^3, a is increased by n^2 every iteration, which cancels out the while loop to n


b) O(nlogn) - The base for loop is axiomatically n, the nested while loop is a little more tricky. It  doubles as n gets larger, so with larger increases in n, it's increase will get smaller. Definitely logn behavior.


c) O(infinity) - unless the input is 0 or a negative number, this function will result in an infinite loop. If the input is negative it will be O(n) as it steps up toward 0.

## Exercise II

I would start on the n/2 floor and throw an egg to see if it breaks.
If it does break I would go down to a floor half as high as the current floor (n/4) and try again
if the egg doesn't break, I would go to a floor that is half as high as n or the recent highest floor I've checked.
This would narrow down the highest floor to two floors, whichever floor doesn't break the egg is the highest floor.
This would result in the loss of logn eggs.