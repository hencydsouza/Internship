a = [[1,2,3,4,5],[1,5,6,7,8],[3,4,5,6,7]]

def highest(ls):
    ini = ls[0]
    for i in ls:
        if i>ini:
            ini = i
    return ini

def mul_lst(ls):
    newls = ls[0]
    for i in ls:
        for j in range(len(i)):
            if(i!=ls[0]):
                newls[j] = newls[j]*i[j]
    return newls

def main():
    list_1 = mul_lst(a)
    print("Multiplied List: ",list_1)
    print("Highest value: ",highest(list_1))

main()