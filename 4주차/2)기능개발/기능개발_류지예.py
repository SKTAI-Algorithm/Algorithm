import math

def solution(progresses, speeds):
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    answer = []
    th = 0

    for idx in range(len(progresses)):
        if progresses[idx] > progresses[th]:  
            answer.append(idx - th)
            th = idx 
    answer.append(len(progresses) - th)  

    return answer
