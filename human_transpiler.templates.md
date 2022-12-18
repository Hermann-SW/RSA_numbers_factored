```
Python         ==>         JavaScript / NodeJS


multiple assignment
-------------------
(a,b,c) = ...              [a,b,c] = ...


dictionary
----------
{2: 3, 41: 1, 149: 1,...}  {"2": 3n,"41": 1n,"149": 1n,...}


complete function sample
------------------------
def dict_int(d):           function dict_int(d){
    p = 1                      var p = 1n;
    for k in d.keys():         for(k of Object.keys(d)){
        p *= k ** d[k]             p *= BigInt(k) ** d[k];
                               }
    return p                   return p;
                           }


for loops
---------
for ... in ...:            for(... of ...){
    ...                        ...
                           }


for ... in range(...):     for(...; ...; ...){
    ...                        ...
                           }

function
--------
def f(...):                function f(...){
    ...                        ...
                           }


Python print()
--------------
print(...)                 print(...)

print(..., end="")         "build string" workaround
```
