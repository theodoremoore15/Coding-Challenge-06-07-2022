#Author: Theodore Moore
#Coding Challenge 6/7/2022 Part 1

def pickTuple(N):
    a=[]
    #get input for each triple N times
    for x in range(N):
        a.append(input().split())
    #for each triple get the largest and the next largest
    for y in a:
        largest=0
        nextLargest=0
        for z in y:
            if int(z)>largest:
                nextLargest=largest
                largest=int(z)
            elif int(z)>nextLargest:
                nextLargest=int(z)
        #print the 2nd largest output each time
        print(nextLargest)


pickTuple(int(input()))