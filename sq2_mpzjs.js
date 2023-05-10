const mpzjs = require('mpzjs');

function assert(condition, message) {
    if (!condition) {
        throw (message || "Assertion failed");
    }
}

function abs(x) {
    return x < 0 ? x.neg() : x;
}

//##############################################################################
// Robert Chapman 2010 code from https://math.stackexchange.com/a/5883/1084297
// with small changes:
// - asserts instead bad case returns
// - renamed root4() to root4m1() indicating which 4th root gets determined
// - made sq2() return tuple with positive numbers; before sq2(13) = (-3,-2)
// - sq2(p) result can be obtained from sympy.solvers.diophantine.diophantine function diop_DN(): diop_DN(-1, p)[0]
//
function mods(a, n){
    assert(n > 0);
    a = a.mod(n);
    if (a.mul(2) > n){
        a = a.sub(n);
    }
    return a;
}

function powmods(a, r, n){
    var out = mpzjs(1);
    while (r > 0){
        if ((r.mod(2)) == 1){
            r = r.sub(1);
            out = mods(out.mul(a), n);
        }
        r = r.div(2);
        a = mods(a.mul(a), n);
    }
    return out;
}

function quos(a, n){
    assert(n > 0);
    return a.sub(mods(a, n)).div(n);
}

function grem(w, z){
    // remainder in Gaussian integers when dividing w by z
    var w0=w[0]; var w1 = w[1];
    var z0=z[0]; var z1 = z[1];
    var n = z0.mul(z0).add(z1.mul(z1));
    assert(n != 0);
    var u0 = quos(w0.mul(z0).add(w1.mul(z1)), n);
    var u1 = quos(w1.mul(z0).sub(w0.mul(z1)), n);
    return[w0.sub(z0.mul(u0)).add(z1.mul(u1)),
           w1.sub(z0.mul(u1)).sub(z1.mul(u0))];
}

function ggcd(w, z){
    while (z[0] != 0 && z[1] != 0){
        var a = z; z =grem(w, z); w = a;
    }
    return w;
}

function root4m1(p){
    // 4th root of 1 modulo p
    var k = p.div(4);
    var j = mpzjs(2);
    for(;;){
        var a = powmods(j, k, p);
        var b = mods(a.mul(a), p)
        if (b == -1){
            return a;
        }
        assert(b == 1 && "p not prime");
        j = j.add(1);
    }
}

function sq2(p){
    assert(p > mpzjs(1) && p.mod(mpzjs(4)) == 1);
    var a = root4m1(p);
    var xy = ggcd([p,mpzjs(0)],[a,mpzjs(1)]);
    return [abs(xy[0]), abs(xy[1])];
}
//
//##############################################################################

const start = Date.now()
var r = sq2(mpzjs(2n ** 2n ** 13n + 897n))
console.error(`${(Date.now() - start)/1000}s`);
console.log(r[0] + " " + r[1])
