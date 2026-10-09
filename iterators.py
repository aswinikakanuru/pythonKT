'''Iterator
An iterator produces values one at a time.
Important functions:
iter()
next()'''

numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))


#Generator

#Generator uses yield.

def numbers():
    yield 10
    yield 20
    yield 30
for x in numbers():
    print(x)

'''Difference

Normal function:
return → returns value and function ends

Generator:
yield → produces one value at a time
Generators are useful for memory-efficient processing.'''