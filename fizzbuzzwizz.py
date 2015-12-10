result = ''

for i in xrange(1, 100):
    if i % 3 == 0:
        result += ' Fizz '
    elif i % 5 == 0:
        result += ' Buzz '
    elif i % 7 == 0:
        result += ' Wizz '
    else:
        result += ' %d ' % i

print result
