def even_odd_filter(**kwargs):
    result = {}
    for filter, nums in kwargs.items():
        if filter == "even":
            for num in nums:
                if not "even" in result.keys():
                    result["even"] = []
                if num % 2 == 0:
                    result["even"].append(num)
        else:
            for num in nums:
                if not "odd" in result.keys():
                    result["odd"] = []
                if num % 2 != 0:
                    result["odd"].append(num)
    return result

# Test Cases:
# print(even_odd_filter(odd=[4,6,8,0,2,42,60,56,32,5]))