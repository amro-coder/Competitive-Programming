# You are given a permutation p1,p2,…,pn of length n. You have to choose two integers l,r (1≤l≤r≤n) and reverse the subsegment [l,r] of the permutation.
# The permutation will become p1,p2,…,pl−1,pr,pr−1,…,pl,pr+1,pr+2,…,pn.
#
# Find the lexicographically smallest permutation that can be obtained by performing exactly one reverse operation on the initial permutation.
#
# Note that for two distinct permutations of equal length a and b, a is lexicographically smaller than b if at the first position they differ, a has the smaller element.
#
# A permutation is an array consisting of n distinct integers from 1 to n in arbitrary order. For example, [2,3,1,5,4] is a permutation,
# but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    for i in range(1,n+1):
        if(x[i-1]!=i):
            index = x[i-1:].index(i)+i-1
            x[i-1:index+1]=list(reversed(x[i-1:index+1]))
            print(*x)
            break
    else:
        print(*x)
