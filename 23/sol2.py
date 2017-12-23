# Here's my attempt to decompile the program:
#
# b = 65
# c = b
# if (a != 0) {
#     b *= 100
#     b += 100000 # 106500
#     c = b       # 106500
#     c += 17000  # 123500
# }
#
# while (true) {
#     f = 1
#     d = 2
#     # for d in 2..b
#     do {
#         e = 2
#         # for e in 2..b
#         do {
#             if ( d*e == b )
#                 f = 0
#             e += 1
#         } while (e != b)
#
#         d += 1
#     } while (d != b)
#
#     # If there's any pair of numbers (e,d) that can be multiplied together to
#     # make b, add 1 to h
#     # So h is a count of the number of non-primes
#     if ( f == 0 )
#         h += 1
#
#     g = b - c
#     # We check all numbers between 102500 and 123500
#     # in steps of 17
#     if (b == c) break
#     b += 17
# }

# ===========================================
# So it looks like the program is trying to count the number of non-primes in
# the range 106500:123500:17
# First use a sieve of eratosthenes to find all eligible primes then iterate
# over the range to count the non-primes

# Adapted from https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
# I know, I know... I should've written my own. But I just wasn't up to it
# after doing all the decompiling
def sieve(N):
    not_prime = set()
    primes = set()

    for i in range(2, N + 1):
        if i in not_prime:
            continue

        for f in range(i*2, N + 1, i):
            not_prime.add(f)

        primes.add(i)

    return primes

primes = sieve(123500)
print(sum(1 for i in range(106500, 123500 + 1, 17) if i not in primes))
