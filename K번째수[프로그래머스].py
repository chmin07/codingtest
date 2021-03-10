#프로그래머스 K 번째 수

array=[1,5,2,6,3,7,4]

commands=[[2,5,3],[4,4,1],[1,7,3]]

def solution(array,commands):
    c=d=e=[]
    for i in range(len(commands)):
        c=array[commands[i][0]-1:commands[i][1]]
        d=sorted(c)
        e.append(d[commands[i][2]-1])
    return e