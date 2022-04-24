import random
import sys

builtin_input = input

def input():
    line = builtin_input()
    if line == "-1":
        sys.exit(0)
    return line

def solve():
    word = input()
    counts = []
    letters = []
    result = []

    for letter in word:
        if not letters or letters[-1] != letter:
            letters.append(letter)
            counts.append(1)
        else:
            counts[-1] += 1

    for i in range(len(letters)-1):
        if letters[i] < letters[i + 1]:
            counts[i] *= 2
        result.append(letters[i] * counts[i])

    result.append(letters[-1] * counts[-1])

    return ''.join(result)

for i in range(int(input())):
    print(f'Case #{i + 1}: {solve()}')
