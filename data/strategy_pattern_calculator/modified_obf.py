from abc import ABC as _A, abstractmethod as _b

class _X(_A):
 @_b
 def _z(self,p,q):pass

class _Y(_X):
 def _z(self,p,q):return p+q

class _W(_X):
 def _z(self,p,q):return p*q

class _K:
 def __init__(self,s):self._s=s
 def _m(self,s):self._s=s
 def _c(self,i,j):return self._s._z(i,j)

if __name__=="__main__":
 _o=_K(_Y())
 print(_o._c(10,5))