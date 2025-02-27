def solution(a, b):
    answer = ''
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    
    months = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    firstday_index = days.index("FRI")
    target_last_day = months[a]
    target_before_all_sum_day = 0
    for i in range(1, a):
        if a == 1:
            break
        target_before_all_sum_day += months[i]
            
    target_first_day_index = (firstday_index + target_before_all_sum_day) % 7
    
    for i in range(b-1):
        target_first_day_index += 1
    target_day_index = target_first_day_index % 7 
    answer = days[target_day_index]
        
    return answer