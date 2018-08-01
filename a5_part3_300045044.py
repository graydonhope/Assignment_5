## Assignment 5 Part 3
## Sadiq Abbas
## ITI 1120 Computing
## Graydon Hope 300045044

def digital_sum(n):
    '''(Integer) -> Integer '''
    if n==0:
        return 0
    else:
        return digital_sum(n//10) + (n%10)


def digital_root(n):
    '''(Integer) -> Integer '''
    newn = digital_sum(n)
    if newn < 10:
        return newn
    else:
        return digital_root(newn)
    
        
    
