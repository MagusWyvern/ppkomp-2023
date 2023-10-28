'''
A shape consisting of several squares is created by continuing a similar pattern on the right side as shown in the diagram.
Each additional square will share a side with the previous square.
Every square has side length 1

Given the perimeter of the shape, you are to find the number of squares used.

'''

n = int(input())

print(int(n / 2 - 1))