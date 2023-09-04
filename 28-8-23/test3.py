# dic = {}
# n = int(input())
# while n!=0:
#     rem = n%10
#     if rem in dic:
#         dic[rem] += 1
#     else:
#         dic[rem] = 1
#     n = int(n/10)
# print(dic)

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = [None] * (len(a)+len(b))
itr = 0

for i in range(len(a)):
    c[itr] = a[i]
    itr = itr+1
    
for i in range(len(b)):
    c[itr] = b[i]
    itr = itr+1

print(c)