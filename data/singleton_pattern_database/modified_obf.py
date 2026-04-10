class _D:
 _i=None
 def __new__(_c):
  if _c._i is None:_c._i=super(_D,_c).__new__(_c)
  return _c._i
 def _g(self):return "..."

_x=_D()
_y=_D()
print(_x is _y)