'''
使用scikit-learn对iris（鸢尾花）进行预测分类，采用knn模型，最终对其进行评估
'''
import numpy as np
import pandas as pd
from sklearn import datasets

#加载IRIS数据集合
scikit_iris = datasets.load_iris()
#转换为pandas的DataFrame格式，便于观察数据
pd_iris = pd.DataFrame(
    data=np.c_[scikit_iris['data'],scikit_iris['target']],
    columns=np.append(scikit_iris.feature_names,['y'])
)
# print(pd_iris.head(3))
#选取全部特征参与训练模型
X = pd_iris[scikit_iris.feature_names]
Y = pd_iris['y']

from sklearn.model_selection import train_test_split
from sklearn import metrics
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3,random_state=1)

#选择模型
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=10)
#拟合模型
knn.fit(x_train,y_train)
#预测数据,0：Iris setosa,1:Iris versicolor,2:virginica
y_predict_on_train = knn.predict(x_train)
y_predict_on_test = knn.predict(x_test)

print('训练集合准确率为：{}'.format(metrics.accuracy_score(y_train,y_predict_on_train)))
print('测试集合准确率为：{}'.format(metrics.accuracy_score(y_test,y_predict_on_test)))