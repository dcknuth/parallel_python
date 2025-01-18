# Advent of Code Walk-through
Working through an easier day (but non-trivial) of Advent of Code

Let’s walk through an easier Advent of Code Day. Day 5 of 2018 should be solvable, by me, without a couple weeks of attempts finally resulting in failure. This time, you are given a string of upper and lower case letters and need to remove the ones where an upper and lower of the same type meet. This happens to be one where [the terrible, brut force approach](day15_2018.py) works for the first part.

It takes 52 seconds and the guidelines say that there is always an answer that will take < 15 seconds on 10 year old hardware. So we are already over, but I knew this was a bad way to do this. Part two will make this up to 26x harder (remove each set of upper/lower and see which is least), so this method would still run overnight (or over lunch), but it is a good example to try something that is obviously better and then look at what others did.

I will try [an improvement](day15_2018_p2.py) where one only walks the list once, but still using just a list. The nice part is that it is short to write. The possible bad part is that deleting from the middle of a list is supposed to be expensive. Since most list operations are pretty optimized under the hood, let’s hope it’s fine.

This ran in under three seconds, so it counts as an OK solution. The tricky part here is not to do anything that screws up the index during the list operations. That is the reason for the ‘continues’ so that we don’t try to rely on anything that might change during the while loop. It might be better to use a linked list, but this worked and was pretty easy, so let’s see what others did. Here is a nifty part 2 from the [Reddit solutions thread](https://www.reddit.com/r/adventofcode/comments/a3912m/2018_day_5_solutions/):
```
s = open('5.in').read().strip()

alpha = 'abcdefghijklmnopqrstuvwxyz'
M = {}
for c in alpha:
    M[c.lower()] = c.upper()
    M[c.upper()] = c.lower()

ans = 1e5
for rem in alpha:
    s2 = [c for c in s if c!=rem.lower() and c!=rem.upper()]
    stack = []
    for c in s2:
        if stack and c == M[stack[-1]]:
            stack.pop()
        else:
            stack.append(c)
    ans = min(ans, len(stack))
print ans
```

This seems similar to what I did in approach, but using a list like a stack to build the answer from each starting list and making a dictionary to give the opposite case. This took a half second. This next is from [fudlede on GitHub](https://github.com/fuglede/adventofcode/blob/master/2018/day05/solutions.py). He seems to have very nice AOC Python answers:
```
with open('input') as f:
    data = f.read().strip()

# Part one
def react(polymer):
    result = []
    for l in polymer:
        if result and ord(result[-1]) - ord(l) in (-32, 32):
            result.pop()
        else:
            result.append(l)
    return result

print(len(react(data)))

# Part two
def react_char(polymer, i):
    return react(a for a in polymer if ord(a) % 32 - 1 != i)

print(min(len(react_char(data, i)) for i in range(25)))
```
This took 0.4 seconds and ends up being very similar to the other example. However, what is ord()? It turns out to give you the ASCII number from a letter. Since the same letter of different case are 32 positions away from each other, you can test for the pair without all my conversions and if statements. It was noted in the Reddit thread and another solution example that Python’s swapcase() is also a compact way to do this. This last example also uses ord() to create a cute way to drop a letter of both cases from the original list. The first example uses list comprehensions and the second, advanced for looping.
