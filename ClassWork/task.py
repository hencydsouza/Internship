def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)

def npr(n,r):
    return fact(n)/fact(n-r);

def ncr(n,r):
    return fact(n)/(fact(n-r)*fact(r));

# a = int(input("Enter n value: "))
# b = int(input("Enter r value: "))

# print("Permutation:",npr(a,b))
# print("Combination:",ncr(a,b))

lst = ['gautam','ankith','linesh']

# from itertools import permutations
# comb = permutations(lst, len(lst))
  
# for i in comb:
#     print(i)

# def perm(ls):
#     for i in ls:
#         bin(len(ls))

for i in range(3):  
        for j in range(3):  
            for k in range(3):
                if (i!=j and i!=k and j!=k):  
                    print(lst[i], lst[j], lst[k])