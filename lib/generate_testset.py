from sklearn.datasets import load_iris
from pprint import pprint

data = load_iris()
#pprint(data)
print(len(data.data))
print(len(data.target))

