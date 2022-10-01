import math


def solution(number):

    a3 = math.floor((number-1)/3)
    a5 = math.floor((number-1)/5)
    a15 = math.floor((number-1)/15)
    print(a3, a5, a15)
    result = math.floor((a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15)
    return result


print(solution(35))
