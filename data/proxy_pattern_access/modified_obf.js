const _d={_k:"12345",_p:"admin"};
const _px=new Proxy(_d,{
 get:(_t,_r)=>{
  if(_r==="_p")return "X";
  return _t[_r];
 }
});