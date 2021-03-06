#!/usr/bin/python
# -*- coding: utf-8 -*-

import theano
import theano.tensor as T

x = T.dvector('x')
v = T.dvector('v')
y = T.sum(x ** 2)
gy = T.grad(y, x)
vH = T.grad(T.sum(gy * v), x)
f = theano.function([x, v], vH)
print(f([4, 4], [2, 2]))
x = T.dvector('x')
v = T.dvector('v')
y = T.sum(x ** 2)
gy = T.grad(y, x)
Hv = T.Rop(gy, x, v)
f = theano.function([x, v], Hv)
print(f([4, 4], [2, 2]))
