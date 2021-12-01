'''
Link:
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

Problem: Nested List 
VVIP
'''
#Solution
if __name__ == '__main__':
    
    #Store name and scores in list
    student_grades = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_grades.append([name,score])
        scores.append(score)
    
    # find second lowest score    
    scores.sort()
        #after sorting we have to get second element of which must be greater than the minimum or we can say greater than the first element after sorting
    for i in range(len(scores)):
        if scores[i]<scores[i+1]:
            second_lowest = scores[i+1]
            break
    
    #storing students with same score as second lowest
    students = []
    for i in range(len(student_grades)):
        if student_grades[i][1] == second_lowest:
           students.append(student_grades[i][0])
       
    # sorting students list
    students.sort()
    
    #printing elements of students list
    for i in range(len(students)):
        print(students[i])