#compute all possible hexamer
import itertools

bases=['A','T','G','C']

#value of k set to 6 for hexamer
k = 6
six_mer = [''.join(p) for p in itertools.product(bases, repeat=k)]

print("Total number of hexamer:", len(six_mer))

#start included and stop excluded
sample_mer = six_mer[0:400]

print("Number of selected hexamer:", len(sample_mer))

test_mer = six_mer[400:(len(six_mer))]

print("The number of rest of the hexamer:", len(test_mer))

#finding out the most different hexamer:

def jaccard_index(a, b):
    a = set(a)
    b = set(b)

    intersection = len(a.intersection(b))
    union = len(a.union(b))

    return intersection / union


f = open("test_out",'w')

for i in sample_mer:
    for j in test_mer:
         sim_index = jaccard_index(i,j)
    if sim_index == 0:
        break
        
print("Most different hexamer found:", j)

#display the duplex in a convenient format:

def reverse_compliment(seq):
    seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
    return "".join([seq_dict[base] for base in reversed(seq)])


def display_complements(seq):

    rev_comp = reverse_compliment(seq)
    
# Print template
    print(seq)
    
# Print "base pairs"
    for base in seq:
        print('|', end='')
    
# Print final newline character after base pairs
    print()
    
# Print reverse complement
    for base in reversed(rev_comp):
        print(base, end='')
    
# Print final newline character
    print()

#display_complements("CCCCCC")

print("The most different dulex hexamer:")
display_complements(j)

#generate all possible k-mer when k = 7, 8, 9, 10, 11, 12, 13...:
import itertools

bases=['A','T','G','C']
k = 7
%timeit k_mer = [''.join(p) for p in itertools.product(bases, repeat=k)]

import itertools

bases=['A','T','G','C']
k = 8
%timeit k_mer = [''.join(p) for p in itertools.product(bases, repeat=k)]

import itertools

bases=['A','T','G','C']
k = 9
%timeit k_mer = [''.join(p) for p in itertools.product(bases, repeat=k)]

import itertools

bases=['A','T','G','C']
k = 10
%timeit k_mer = [''.join(p) for p in itertools.product(bases, repeat=k)]

import itertools

bases=['A','T','G','C']
k = 11
%timeit k_mer = [''.join(p) for p in itertools.product(bases, repeat=k)]

import itertools

bases=['A','T','G','C']
k = 12
%timeit k_mer = [''.join(p) for p in itertools.product(bases, repeat=k)]

import itertools

bases=['A','T','G','C']
k = 13
%timeit k_mer = [''.join(p) for p in itertools.product(bases, repeat=k)]
