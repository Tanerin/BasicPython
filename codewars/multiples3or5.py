def solution (number):
    acum=0
    for i in range (number):
        if i%3==0 or i%5==0:
            acum=acum+i 
    return acum

if __name__=="__main__":
    res=solution(500)
    print (res)