def solution(people, limit):
    answer = 0
    people.sort()
    heavy = len(people)-1
    light = 0
    
    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
        answer += 1
    
    return answer