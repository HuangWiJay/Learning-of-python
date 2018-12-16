'''
简单线性回归
'''

from math import sqrt
#求均值
def mean(values: list) -> float :
    return sum(values) / float(len(values))
#求方差
def variance(values:list,mean:float) -> float :
    return sum([(i - mean) ** 2 for i in values])
#求协方差
def covariance(x,x_mean,y,y_mean) -> float:
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - x_mean) * (y[i] - y_mean)
    return covar
#求回归系数w1，w0
def coefficient(dataset:list) -> tuple:
    x = [i[0] for i in dataset]
    y = [i[-1] for i in dataset]
    x_mean,y_mean = mean(x),mean(y)
    cov = covariance(x,x_mean,y,y_mean)
    var = variance(x,x_mean)
    w1 = cov / var
    w0 = y_mean - w1 * x_mean
    return w1,w0
#求均方根误差rmse
def rsme_metric(actual:list,predicted:list) -> float:
    sum_error = 0.0
    for i in range(len(actual)):
        prediction_error = predicted[i] - actual[i]
        sum_error += (prediction_error ** 2)
    mean_error = sum_error / float(len(actual))
    return sqrt(mean_error)
#构建简单线形回归
def simple_linear_regression(train:list,test:list) -> list:
    predictions = list()
    w1,w0 = coefficient(train)
    for row in test:
        y_model = w1 * row[0] + w0
        predictions.append(y_model)
    return predictions
#评估算法数据准备及协调
def evaluate_algorithm(dataset:list,algorithm) -> float:
    #新建测试集合，y变量为None
    test_set = list()
    for row in dataset:
        row_copy = list(row)
        row_copy[-1] = None
        test_set.append(row_copy)

    predicted = algorithm(dataset,test_set)
    for val in predicted:
        print('%.3f' % val)

    actual = [row[-1] for row in dataset]
    rmse = rsme_metric(actual,predicted)
    return rmse

if __name__ == '__main__':
    dataset = [[1.2,1.1],[2.4,3.5],[4.1,3.2],[3.4,2.8],[5,5.4]]
    rmse = evaluate_algorithm(dataset,simple_linear_regression)
    print('RMSE:%.3f' % rmse)
    #简单绘图表示
    import matplotlib.pyplot as plt
    plt.subplot(111)
    plt.axis([0,6,0,6])
    x1,y1 = [row[0] for row in dataset],[row[-1] for row in dataset]
    x2 = x1
    y2 = [1.386,2.463,3.990,3.362,4.799]
    plt.plot(x1,y1,'bo',x2,y2,'rx-',markersize = 5)
    plt.show()






