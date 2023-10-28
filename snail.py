
'''
A snail crawls up a pole starting from the ground.
Every day it will crawl up 5 inches, and every night it slides back down 3 inches.

Given the height of the pole the snail climbed, you are to calculate when the snail first reached the top of the pole.
'''

height = int(input())

day = 0

while height > 0:
    day += 1
    height -= 5
    if height <= 0:
        break
    height += 3

print(day)