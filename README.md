# RSA_numbers_factored

Continuation of [RSA_numbers_factored.py gist](https://gist.github.com/Hermann-SW/839dfe6002810d404e3f0fe1808a6333) (now in [python/RSA_numbers_factored.py](python/RSA_numbers_factored.py) and documented [here](python/README.md)), with transpiled [RSA_numbers_factored.js](RSA_numbers_factored.js) (from the Python version) and HTML demos.

[R.html](R.html)  browser term output RSA tuples if both prime factors are ≡1 (mod 4)  
[validate.html](validate.html)  do validation, with output in browser term  
[squares.html](squares.html)  initial version, dynamical onclick buttons if ≡1 (mod 4)  

Transpilation was done manually, using these templates:  
[human_transpiler.templates.md](human_transpiler.templates.md)  

## Functionality validation: Python, browser and nodejs demos 

Just executing RSA_numbers_factored.py does functionality validation with lots of asserts:  
![python.validation.png](python.validation.png)

Below screen recording of browser validation corresponds to above Python validation, just in browser term:  
https://hermann-sw.github.io/RSA_numbers_factored/validate.html  
![Peek_2022-12-18_22-29.gif](Peek_2022-12-18_22-29.gif)

Executing transpiled RSA_numbers_factored.js executes same functionality validation with console.log output:  
![nodejs.validation.png](nodejs.validation.png)

Finally, if redirecting output for JavaScript "print()" implementation to console.log, validation can be done in developer tools browser console as well:  
![browser_console.validation.png](browser_console.validation.png)

