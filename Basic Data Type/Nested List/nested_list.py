'''
Link:
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

Problem: Nested List 
VVIP
'''






if __name__ == '__main__':
    
    #Store name and scores in list
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
        
    # Initailaize the lowest and second lowest with maximum grade possible i.e., 100
    lowest = second_lowest = 100 
     
    # store the minimum score in the list
    for i in range(len(arr)):
        if arr[i][1]<lowest:
            lowest = arr[i][1]

    # finding second lowest score
    for i in range(len(arr)):
        if arr[i][1] > lowest and arr[i][1] <= second_lowest:
            second_lowest = arr[i][1]
            break
            
    students = []
    for i in range(len(arr)):
        if arr[i][1] == second_lowest:
           students.append(arr[i][0])
    
    students.sort()
    for i in range(len(students)):
        print(students[i])
