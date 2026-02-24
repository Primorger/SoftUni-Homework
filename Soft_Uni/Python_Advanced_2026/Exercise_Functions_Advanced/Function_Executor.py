def func_executor(*args):
    result = []
    
    for func, func_args in args:
        function_result = func(*func_args)
        result.append(f"{func.__name__} - {function_result}")
    
    return "\n".join(result)