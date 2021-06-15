#!/usr/env/bin python3

# "Algorithm" taken from https://rosettacode.org/wiki/Best_shuffle

# Satisfy prompt stating that the score is the sum of all chars which have not changed position within the original string
# s = original string, ns = new string
def count(s, ns):
    return sum(a == b for a, b in zip(s, ns))

# Best Shuffle - returns tuple to satisfy print requirements from prompt
def best_sort(s):
    srange = range(len(s))
    nsa = list(s) # New string as array
    
    for i in srange:
        for j in srange:
            # Change position of char where possible
            if i != j and nsa[i] != nsa[j] and s[i] != nsa[j] and s[j] != nsa[i]:
                nsa[j], nsa[i] = nsa[i], nsa[j]
                break
    
    ns = ''.join(nsa)
    
    return (s, ns, count(s, ns))

# Print in format as per requirement from prompt
def print_best_sort(st):
    print("%s, %s, (%d)" % best_sort(st))
