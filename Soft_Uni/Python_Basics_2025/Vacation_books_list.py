num_pages = int(input())
pages_per_hour = int(input())
time_needed = int(input())

sum_time_needed = num_pages // pages_per_hour
time_needed_per_day = sum_time_needed//time_needed

print(time_needed_per_day)