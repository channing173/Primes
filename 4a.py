import sys

for i in xrange(2, sys.maxsize):
    num = (6 * (i ** 2)) + 27
    for p in range(2, num):
        if num % p == 0:
            print "(6 * (%s^2) + 27) is not prime, can be divided by %s" % (i, p)
            continue
