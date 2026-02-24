command = input()
times = int(input())

def repeat_string(string, times):
    answer = ""
    for _ in range(times):
        answer += string
    return answer

print(repeat_string(command, times))