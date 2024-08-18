def callLimit(limit: int):
    count = 0
    def callLimmiter(function):
        def limit_function(*args: any, **kwargs: any):
            try:
                nonlocal count
                count += 1
                if count > limit:
                    raise AssertionError(f"{function} call too many times")
                return function(*args, **kwargs)
            except AssertionError as aerr:
                print(f'Error : {aerr}')
        return limit_function
    return callLimmiter
