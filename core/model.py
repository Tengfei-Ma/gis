from sklearn.ensemble import RandomForestRegressor
from sklearn import svm
import xgboost


def build(modelIndex, modelArgs):
    model = None
    if modelIndex == 0:
        model = RandomForestRegressor(n_estimators=modelArgs[0], max_features=modelArgs[1], max_depth=modelArgs[2])
    elif modelIndex == 1:
        model = svm.SVR(kernel=modelArgs[0], gamma=modelArgs[1], C=modelArgs[2])
    elif modelIndex == 2:
        model = xgboost.XGBRegressor(n_estimators=modelArgs[0], max_depth=modelArgs[1], learning_rate=modelArgs[2])
    else:
        model = None
    return model
