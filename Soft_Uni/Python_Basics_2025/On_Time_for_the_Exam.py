exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())
 
exam_time_in_minutes = exam_hour * 60 + exam_minute
arrival_time_in_minutes = arrival_hour * 60 + arrival_minute
 
time_difference = arrival_time_in_minutes - exam_time_in_minutes
 
if time_difference > 0:
    print("Late")
    hours_late = time_difference // 60
    minutes_late = time_difference % 60
    if hours_late >= 1:
        print(f"{hours_late}:{minutes_late:02d} hours after the start")
    else:
        print(f"{minutes_late} minutes after the start")
elif time_difference >= -30:
    print("On time")
    if time_difference < 0:
        minutes_early = abs(time_difference)
        print(f"{minutes_early} minutes before the start")
elif time_difference < -30:
    print("Early")
    time_early = abs(time_difference)
    hours_early = time_early // 60
    minutes_early = time_early % 60
    if hours_early >= 1:
        print(f"{hours_early}:{minutes_early:02d} hours before the start")
    else:
        print(f"{minutes_early} minutes before the start")
 