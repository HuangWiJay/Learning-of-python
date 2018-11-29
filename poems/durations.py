from time import time as t
import time
def duration(func):
    start_time = t()
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        end_time = t()
        print('本次执行所需时间为：%.2f秒' % (end_time - start_time))
    return wrapper
