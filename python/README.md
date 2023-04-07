# RSA_numbers_factored.py

Related forum thread:  
[https://forums.raspberrypi.com/viewtopic.php?t=343468](https://forums.raspberrypi.com/viewtopic.php?t=343468)

Continuation of [RSA_numbers_factored.py gist](https://gist.github.com/Hermann-SW/839dfe6002810d404e3f0fe1808a6333) (now in [./RSA_numbers_factored.py](./RSA_numbers_factored.py)), with Python changes getting manually transpiled to [../RSA_numbers_factored.js](../RSA_numbers_factored.js) for use in nodejs and HTML demos.

## RSA_numbers_factored.py documentation  

Generated with lazydocs, can be found here:  
[docs/RSA_numbers_factored.py.md](docs/RSA_numbers_factored.py.md)

## Non-standard Python environments

### MicroPython

Version with  emulation of used sympy functionality [RSA_numbers_factored_mp.py](RSA_numbers_factored_mp.py) does run on MicroPython on a 264KB ram only Raspberry Pico RP2040 microcontrolller (just for fun — "Validation demo takes 3:09min on RP2040 MicroPython, instead of 1 second in Python or browser JavaScript version though ..."). More details in [this forum posting](https://forums.raspberrypi.com/viewtopic.php?t=343468&start=25#p2085457)  
![MicroPython demo](RSA_numbers_factored_mp.py.png)

### Android

Unmodified RSA_numbers_factored.py works on Android (with [Pydroid3](https://play.google.com/store/search?q=Pydroid3) playstore app, 3 day free trial, 2$/month, 16$/lifetime) as well. Details in [this forum posting](https://forums.raspberrypi.com/viewtopic.php?t=343468&start=25#p2090124)  
![Pydroid3 demo](Pydroid3_demo.png)

