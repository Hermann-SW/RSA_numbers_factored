var G = require("./gaussian_module")
const start = Date.now()
var r = G.sq2(2n ** 2n ** 13n + 897n)
console.error(`${(Date.now() - start)/1000}s`);
console.log(r[0] + " " + r[1])
