str = input()

lst = [""] * len(str)
itr = 0
cur = ''

newlst = list(str)
# print(newlst)

for i in range(len(newlst)):
    lst[itr] = newlst[i]
    for j in range(i+1,len(newlst)):
        if newlst[i]!=newlst[j]:
            lst[itr]+=newlst[j]
        else:
            itr = itr+1
                       
print(lst)