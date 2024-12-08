def solution(array, commands):
    answer = []
    newArray = []
    for i in range(len(commands)):
        newArray = array[(commands[i][0]-1):(commands[i][1])]
        newArray.sort()
        answer.append(newArray[(commands[i][2]-1)])
    return answer