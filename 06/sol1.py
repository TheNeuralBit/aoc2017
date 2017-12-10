from array import array
from operator import itemgetter

def max_index(iterable):
    return max(enumerate(iterable), key=itemgetter(1))

def redistribute_banks(banks):
    idx, val = max_index(banks)
    banks[idx] = 0
    length = len(banks)
    while val > 0:
        idx = (idx + 1) % length
        banks[idx] += 1
        val -= 1


def reallocate(banks):
    previous_banks = []
    count = 0

    while banks not in previous_banks:
        #print(banks)
        #print(previous_banks)
        previous_banks.append(array('I', banks))
        redistribute_banks(banks)
        count += 1

    return count

assert reallocate(array('I', [0, 2, 7, 0])) == 5


with open('input', 'r') as fp:
    banks = array('I', map(int, fp.readline().strip('\n').split()))
    print(reallocate(banks))
