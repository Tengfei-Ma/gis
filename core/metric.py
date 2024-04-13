import numpy as np


# 计算一致性相关系数Concordance Correlation Coefficient
def ccc(x, y):
    sxy = np.sum((x - x.mean()) * (y - y.mean())) / x.shape[0]
    CCC = 2 * sxy / (np.var(x) + np.var(y) + (x.mean() - y.mean()) ** 2)
    return CCC


# 计算均值误差Mean Error
def me(y_true, y_pred):
    ME = np.average(y_pred - y_true)
    return ME
