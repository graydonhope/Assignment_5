## Assignment 5 Part 1
## Sadiq Abbas
## ITI 1120 Computing
## Graydon Hope 300045044

def largest_34(a):
    '''(list) -> number '''
    a.sort()
    return (a[-3] + a[-4])

def largest_third(a):
    '''(list) -> number '''
    a.sort()
    return sum(a[-(len(a)//3):])

def third_at_least(a):
    a.sort()
    for item in range(len(a)):
        if a.count(a[item]) >= ((len(a)//3) +1):
            return a[item]

def sum_tri(a,x):
    '''(list, number) -> Bool '''
    list_n = a*3
    counter = 0
    y = len(list_n) // 2
    for index in range(y):
        for index2 in range(index+1,len(list_n)):
            for index3 in range(index2+1,len(list_n)):
                if x == list_n[index] + list_n[index2] + list_n[index3]:
                    return True
    return False


    

    

    
