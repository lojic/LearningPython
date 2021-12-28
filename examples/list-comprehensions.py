# The Python versions of list comprehensions found in Graham Hutton's
# "Programming Haskell" book, chapter 5.

[ x**2 for x in range(1,6) ]

[ (x,y) for x in range(1,4) for y in range(4,6) ]

[ (x,y) for x in range(1,4) for y in range(x,4) ]

concat = lambda xss: [ x for xs in xss for x in xs ]

firsts = lambda ps: [ x for (x,_) in ps ]

length = lambda xs: sum(1 for _ in xs)

factors = lambda n: [ x for x in range(1,n+1) if n % x == 0 ]

prime = lambda n: factors(n) == [1, n]

primes = lambda n: [ x for x in range(2, n+1) if prime(x) ]

find = lambda k, t: [ v for (k1,v) in t if k == k1 ]

pairs = lambda xs: zip(xs, xs[1:])

is_sorted = lambda xs: all(x <= y for (x,y) in pairs(xs))

positions = lambda x, xs: [ i for (x1,i) in zip(xs, range(len(xs))) if x == x1 ]

lowers = lambda xs: len([ x for x in xs if x.islower() ])

count = lambda x, xs: len([ x1 for x1 in xs if x == x1])
