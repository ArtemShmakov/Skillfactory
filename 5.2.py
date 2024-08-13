def my_decorator(fn):
    dict_={}
    def wrapper(*args, **kwargs):
        nonlocal dict_
        fn(*args, **kwargs)

    return wrapper