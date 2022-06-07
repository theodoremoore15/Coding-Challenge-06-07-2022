#Author: Theodore Moore
#Coding Challenge 6/7/2022 Part 2

def getSum(T):
    a=[]
    #get input for each string T times
    for x in range(T):
        a.append(input())
    #check if each characte has a digit and if so adds it to the total for that string
    for y in a:
        total=0
        for z in y:
            if z.isdigit():
                total= total+ int(z)
        print(total)


getSum(int(input()))