import csv
import random
def loadDataset(filename,split,trainingSet,testSet):
    with open (filename,'r') as file:
        lines = csv.reader(file)
        dataset = list(lines)
        for i in range(len(dataset) - 1):
            for j in range(4):
                dataset[i][j] = float(dataset[i][j])
            if random.random() < split:
                trainingSet.append(dataset[i])
            else:
                testSet.append(dataset[i])

if __name__ == '__main__':
    trainSet = []
    textSet = []
    loadDataset('iris.csv',0.70,trainSet,textSet)
    print('训练集合样本数：' + repr(len(trainSet)))
    print('测试集合样本数：' + repr(len(textSet)))