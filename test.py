import numpy as np

a = np.array([1, 2, 3])

print(a.shape)
b = np.array([[1, 2, 3],

        [4, 5, 6]])

print(b.shape)

c = np.array([[[1, 2],

               [3, 4]]])

print(c.shape)

c = np.array([[[1, 2],[3,4]],

    [[5, 6],[7, 8]]])

print(c.shape)
sales = np.array([

    [100, 120, 90],

    [110, 130, 95],

    [105, 125, 100]

])

print("每天銷售:", sales.sum(axis=1))

print("每商品銷售:", sales.sum(axis=0))

print("總銷售:", sales.sum())

d = np.array([10, 20, 30, 40, 50])

print(d[0])

e = np.array([10, 20, 30, 40, 50])

print(e[0:4:2])

f = np.array([

[10, 20, 30],

[40, 50, 60],

[70, 80, 90]

])

print(f[1])

print(f[:,2])

print(f[0,:])

g = np.array([

[10, 20, 30],

[40, 50, 60],

[70, 80, 90]

])

print(g[0:2,:])

print(g[:,1:3])

print(g[0:2,1:3])

h = np.array([

[[10, 20, 30],

[40, 50, 60],

[70, 80, 90]],

[[100, 110, 120],

[130, 140, 150],

[160, 170, 180]]

])

print(h[0:2,:,:])

print(h[:,1:3,:])

print(h[0:2,:,1:3])


i = np.array([1, 2, 3])

j = 10

k = i + j

print(k)

l = np.array([

    [100, 120, 90],

    [110, 130, 95],

    [105, 125, 100]

])

m = np.array([10, 20, 30])

n = l + m

print("原始銷售：",l)

print("調整金額：",m)

print("調整後銷售：",n)

o = np.array([10, 50, 30])

print(np.argmax(o))

print(np.argmin(o))

p = np.array(["A", "B", "C"])

q = np.array([10, 20, 30])

r = np.argmax(q)

s = np.argmin(q)

print("最大的品項:",p[r])

print("最小的品項:",p[s])