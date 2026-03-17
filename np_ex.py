
import numpy as np


a = np.zeros(10)
a[4] = 1


b = np.arange(10,50)

c = b[::-1]

d = np.arange(0,9)
d = d.reshape((3,3))


x = np.array([1,2,0,0,4,0])
e = np.where(x!=0)[0]

f = np.random.random(30).mean()


g = np.zeros((5,5))
g[0,:] = 1
g[-1,:] = 1
g[:,0] = 1
g[:,-1] = 1


h  = np.tile( np.array( [[1,0],[0,1]]), (4,4))


j= np.arange(11)
j[np.logical_and( j>3, j<8)] *=-1

k = np.random.random(10)
k = np.sort(k)


l1 = np.random.randint(0, 6,10)
l2 = np.random.randint(0, 6,10)

l = l1==l2

m = np.arange(10, dtype=np.int32)
m = m**2

n1 = np.arange(9).reshape(3,3)
n2 = n1+1
n1dotn2 = np.dot(n1,n2)
n = np.diag(n1dotn2)












if __name__ == '__main__':

    pass


