def even_odd(*args):
    command = args[-1]
    nums = args[:-1]
    if command == "even":
        return list(filter(lambda x: x % 2 == 0, nums))
    else:
        return list(filter(lambda x: x % 2 != 0, nums))