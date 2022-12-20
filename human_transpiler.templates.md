```
Python                 ==>                 JavaScript / NodeJS


multiple assignment
-------------------
(a,b,c) = ...                              [a,b,c] = ...


dictionary
----------
{2: 3, 41: 1, 149: 1,...}                  {"2": 3n,"41": 1n,"149": 1n,...}


complete function sample
------------------------
def dict_int(d):                           function dict_int(d){
    p = 1                                      var p = 1n;
    for k in d.keys():                         for(k of Object.keys(d)){
        p *= k ** d[k]                             p *= BigInt(k) ** d[k];
                                               }
    return p                                   return p;
                                           }


for loops
---------
for ... in ...:                            for(... of ...){
    ...                                        ...
                                           }


for ... in range(...):                     for(...; ...; ...){
    ...                                        ...
                                           }

function
--------
def f(...):                                function f(...){
    ...                                        ...
                                           }


Python print()
--------------
print(...)                                 print(...)

print(..., end="")                         "build string" workaround


Class
-----

class ...:                                 class ...{
    ...                                        ...
                                           };


    def __init__(self):                        constructor(){
        ...                                        ...
                                               }


    def get_(self, x):                         get_(x){
        if type(x) == list:                        if (typeof(x) == 'object')
            return x                                   return x;
        else:                                      else
            return self.get(x)                         return this.get(x);
                                               }


    def __iter__(self):                        *[Symbol.iterator]() {
        self.i = 0                                 yield* rsa;
        return self                            }

    def __next__(self):
        if self.i < len(rsa):
            r = rsa[self.i]
            self.i += 1
            return r
        else:
            raise StopIteration


>>> from RSA_numbers_factored import RSA   > R = require("./RSA_numbers_factored")
>>> RSA = RSA()                            ...
>>> for r in RSA:                          > RSA = new R.RSA()
...     print(r)                           RSA {}
...                                        > for(r of RSA){
[59, ...                                   ...     console.log(r);
...                                        ... }
>>>                                        [
                                             59n,
                                           ...
                                           ]
                                           undefined
                                           >


if __name__ == "__main__":                 if (typeof navigator != 'undefined')
    # executed with python                     // in browser
else:                                      } else if (process.argv.length > 1) {
    # imported                                 // executed with nodejs
                                           } else {
                                               // required
                                               module.exports = {
                                                   ...
                                               };
                                           }
```
