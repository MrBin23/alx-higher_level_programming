#!/usr/bin/node
const myobject = {
  type: 'object',
  value: 12
};
console.log(myobject);
myObject.incr = function () {
  this.value++;
};
myObject.incr();
console.log(myobject);
myObject.incr();
console.log(myobject);
myObject.incr();
console.log(myobject);
