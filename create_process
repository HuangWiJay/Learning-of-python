import time
def createProcess():
    scale = 50
    print('执行开始'.center(scale//2,'-'))
    start_time = time.perf_counter()
    for i in range(scale + 1):
        a = '*' * i
        b = '.' * (scale - i)
        c = (i/scale) * 100
        d = time.perf_counter() - start_time
        print('\r{:^3.0f}%[{}{}]{:.2f}'.format(c,a,b,d),end = '')
        time.sleep(0.1)
    print('\n' + '执行结束'.center(scale//2,'-'))

if __name__ == '__main__':
    createProcess()
    
