# Python version
import sys

print('Python: {}'.format(sys.version))
# scipy
import scipy

print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy

print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib

print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas

print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn

print('sklearn: {}'.format(sklearn.__version__))

from numpy import array

# data[from:to]
x = array([1, 2, 3, 4])
a = array([[11, 22, 33], [44, 55, 66], [77,88,99]])
X, y = a[:, :-1], a[:,-1]

from sklearn.model_selection import KFold

data = array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
kfold = KFold(n_splits=3, random_state=1, shuffle=True)
for train, test in kfold.split(data):
    print('train: %s, test: %s' % (data[train], data[test]))
