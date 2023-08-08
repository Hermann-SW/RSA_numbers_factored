from sys import argv
assert len(argv) == 4
with open(argv[1]) as f:
    x = int(f.readlines()[-3].split(":")[1], 16)
p = int(argv[2])*2**int(argv[3])+1
print(pow(x, 2,  p) == p-1)
