'''
简单线性回归,从csv文件中读取数据
'''

from math import sqrt
from csv import reader
from random import randrange,seed
import matplotlib.pyplot as plt
#导入csv文件
def load_csv(filename:str) -> list:
    dataset = list()
    with open(filename,'r') as f:
        csv_reader = reader(f)
        #读取表头
        headings = next(csv_reader)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset
#将字符串列转换成浮点数
def str_column_to_float(dataset:list,column:int):
    for row in dataset:
        row[column] = float(row[column].strip())
#将数据按百分比分割为训练集合和测试集合,百分比为训练集合占数据百分比
def train_test_split(dataset:list,percent:float) -> tuple:
    train = list()
    train_size = len(dataset) * percent
    test = list(dataset)
    while len(train) < train_size:
        index = randrange(len(test))
        train.append(test.pop(index))
    return train,test

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
def rmse_metric(actual:list,predicted:list) -> float:
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
def evaluate_algorithm(dataset:list,algorithm,split_percent,*args) -> float:
    train,test = train_test_split(dataset,split_percent)
    predicted = algorithm(train,test)

    actual = [row[-1] for row in test]
    rmse = rmse_metric(actual,predicted)

    to_graph(train,test,predicted)
    return rmse
#将数据展示为图像
def to_graph(train:list,test:list,predicted:list):
    x_train = [row[0] for row in train]
    y_train = [row[-1] for row in train]
    x_test = [row[0] for row in test]
    y_test = [row[-1] for row in test]
    x_predicted = [row[0] for row in test]
    y_predicted = predicted
    plt.plot(x_train,y_train,'bo')
    plt.plot(x_test,y_test,'ro')
    plt.plot(x_predicted,y_predicted,'rx-')
    plt.xlabel('横轴',fontproperties = 'SimHei',fontsize = 15)
    plt.ylabel('纵轴',fontproperties = 'SimHei',fontsize = 15)
    plt.savefig('simle-linear-regression.png')
    plt.show()

if __name__ == '__main__':
    #设置随机数种子，为随机挑选训练和测试数据集做准备
    seed(2)
    #导入数据并做数据分割准备
    filename = 'dataset.csv'
    dataset = load_csv(filename)
    for i in range(len(dataset[0])):
        str_column_to_float(dataset,i)
    #设置数据集合百分比
    percent = 0.6

    rmse = evaluate_algorithm(dataset,simple_linear_regression,percent)
    print('rmse:%.3f' % rmse)







