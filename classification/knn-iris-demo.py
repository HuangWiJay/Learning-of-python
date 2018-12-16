import operator
import math
from random import seed,random
import csv
#读取数据，按百分比分别构建训练集合，测试集合
def loadDataset(filename,split,trainingSet,testSet):
    with open (filename,'r') as file:
        lines = csv.reader(file)
        dataset = list(lines)
        for i in range(len(dataset) - 1):
            for j in range(4):
                dataset[i][j] = float(dataset[i][j])
            if random() < split:
                trainingSet.append(dataset[i])
            else:
                testSet.append(dataset[i])
#计算欧式距离
def EuclidDist(instance1:list,instance2:list,len:int) -> float :
    distance = 0.0
    for i in range(len):
        distance += pow(instance1[i] - instance2[i],2)
    return math.sqrt(distance)
#获取实例与训练集合的k'个邻居
def getNeighbors(trainSet:list,testInstance:list,k:int) -> list:
    distance = list()
    length = len(testInstance) - 1
    for i in range(len(trainSet)):
        dis = EuclidDist(trainSet[i],testInstance,length)
        distance.append((trainSet[i],dis))
    distance.sort(key=operator.itemgetter(1))
    neighbors = list()
    for i in range(k):
        neighbors.append(distance[i][0])
    return neighbors
#从邻居中判断所属类
def getClass(neighbors:list) -> str:
    classVotes = {}
    for i in range(len(neighbors)):
        instance_class = neighbors[i][-1]
        if instance_class in classVotes:
            classVotes[instance_class] += 1
        else:
            classVotes[instance_class] = 1
    sortedVotes = sorted(classVotes.items(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]
#求精确度
def getAccuracy(testSet:list,predictions:list) -> float:
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1
    return correct / float(len(testSet)) * 100.0

def main():
    seed(3)
    trainSet = []
    testSet = []
    split = 0.7
    loadDataset('iris.csv',split,trainSet,testSet)
    print('训练集合个数：' + repr(len(trainSet)))
    print('测试集合个数：' + repr(len(testSet)))
    predictions = []
    k = 3
    for i in range(len(testSet)):
        neighbors = getNeighbors(trainSet,testSet[i],k)
        result = getClass(neighbors)
        predictions.append(result)
        print('>预测：' + repr(result) + '，实际：' + repr(testSet[i][-1]))
    accuracy = getAccuracy(testSet,predictions)
    print('精确度为：' + repr(accuracy) + '%')


if __name__ == '__main__':
    main()




