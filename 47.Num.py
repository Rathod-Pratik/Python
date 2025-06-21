import numpy as np

a=np.array([[1,2,3],[11,22,33]])
# print(a.ndim)

# Reshape
a=a.reshape(3,2)
# print(a)

# Meanimum value
a1=np.array([1,2,3,4,5])
v=np.mean(a1)
v1=np.max(a1)
# print(v,v1)

# Arrange
a2=np.arange(0,20,3,float)
print(a2)
