#!/usr/bin/env python3

from tqdm import tqdm

data = [ 0xd1, 0xc0, 0xd8, 0x7c, 0xc7, 0x62, 0x00, 0x92, 0x7e, 0x57, 0x7f, 0x9c, 0xcf, 0x0f, 0x78, 0x6c, 0xf9, 0x1f, 0x85, 0x16, 0xcf, 0x78, 0xc2, 0x98, 0xee, 0xdd, 0x81, 0x38, 0x40, 0x45, 0xa3, 0xdc, 0x92, 0x75, 0x8e, 0x63, 0x4f, 0x9d, 0xbf, 0x95, 0x6d, 0x24, 0xdf, 0xec, 0xf7, 0xc7, 0xec, 0xea, 0xf0, 0x79, 0x28, 0xf5, 0x2c, 0x52, 0x33, 0x35, 0x35, 0x31, 0x35, 0x36, 0x38, 0x1a, 0x00, 0x00, 0x03, 0x00, 0x00, 0x14, 0x00, 0x00, 0x52, 0x00, 0x07, 0x32, 0x21, 0x0b, 0x66, 0x7c, 0x44, 0x9a, 0xf9, 0x7c, 0x44, 0x52, 0x53, 0x34, 0x31, 0x2d, 0x53, 0x47, 0x50, 0x72, 0x1b, 0x7a, 0x2a, 0x36, 0x50, 0x02, 0x9e, 0xfb, 0x01, 0xa8, 0xe0, 0x02, 0x9b, 0x83, 0x08, 0x6c, 0x7b, 0x07, 0xc7, 0x89, 0x08, 0xe0, 0x3e, 0x02, 0xa0, 0xfb, 0x01, 0xa8, 0xe0, 0x02, 0xba, 0x48, 0x05, 0xdb, 0x85, 0x04, 0xfa, 0x81, 0x06, 0x00, 0x00, 0x4a, 0x01, 0x00, 0x00, 0xb6, 0x35, 0x7c, 0x1e, 0x65, 0x08, 0xb9, 0x7f, 0x5d, 0x10, 0x16, 0x94, 0x1b, 0x92, 0x20, 0xfb, 0x03, 0x87, 0x0a, 0xb9, 0x15, 0xd9, 0x14, 0x89, 0x1f, 0xb1, 0x01, 0x94, 0x0b, 0xb7, 0x17, 0x8b, 0x08, 0xb6, 0x2f, 0xe0, 0x7d, 0x59, 0xbb, 0xd7, 0x3d, 0x01, 0xff, 0x80, 0x79, 0xd8, 0x0f, 0x86, 0x68, 0xff, 0x2b, 0xdd, 0x93, 0x13, 0x3e, 0x24, 0x01, 0xfe, 0xb7, 0x77, 0x00, 0xb2, 0xae, 0x00, 0x1c, 0x65, 0x0a, 0x1c, 0x50, 0x68, 0xff, 0x4a, 0x1c, 0xff, 0x0b, 0xc5, 0xd4, 0x00, 0x2d, 0x00, 0x00, 0x00, 0x51, 0x9a, 0xff, 0x46, 0x51, 0x70, 0x1d, 0x60, 0xfb, 0x00, 0xc4, 0x28, 0x57, 0x0e, 0xc4, 0x56, 0xff, 0x9f, 0x6b, 0x50, 0x0d, 0xb2, 0x48, 0xff, 0x94, 0x63, 0xbc, 0x0a, 0x7c, 0xd4, 0xff, 0x3c, 0x71, 0xdf, 0x1a, 0x2a, 0xf6, 0x00, 0x60, 0xb8, 0x80, 0x0d, 0x8e, 0xd1, 0x00, 0x55, 0x90, 0x7b, 0x15, 0x98, 0x2c, 0x55, 0xe7, 0x34, 0x02, 0x43, 0x11, 0x27, 0x3a, 0xca, 0xe8, 0xe4, 0x00, 0x9e, 0xff, 0xd0, 0x00, 0x0a, 0x07, 0x10, 0x16, 0x05, 0x7e, 0x15, 0x3a, 0x30, 0x35, 0x30, 0x31, 0x30, 0x35, 0x39, 0x31, 0x30, 0x31, 0x38, 0x46, 0x35, 0x41, 0x31, 0x30, 0x39, 0x31, 0x30, 0x30, 0x1b, 0x37, 0x76, 0xbe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xeb, 0xff]
#data.extend([0] * (510 - len(data)))
data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
# data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
#         0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0,
#         1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1]
data = [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1,
        1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1]


N = 63
K = 51
T = N-K

ALPHA = [0] * 64
LOGTABLE = [0] * 64

def gfmul(x, y):
    if x == 0 or y == 0:
        return 0
    return ALPHA[(LOGTABLE[x] + LOGTABLE[y]) % N];

def poly_eval(poly, point):
    ret = 0
    for coeff in poly:
        ret = gfmul(ret, point) ^ coeff
    return ret



def syndromes(data, zeroes):
    ret = 0
    for zero in zeroes:
        if poly_eval(data, zero):
            ret += 1

    return ret


def deinterleave(data, splits):
    blocks = [[] for i in range(splits)]

    for i in range(len(data)):
        blocks[i % len(blocks)].append(data[i])

    return tuple(i for i in blocks)


#data = data[48:] + data[:48]
'''
rs0 = data[:24]
rs1 = data[24:48]
(block0, block1) = deinterleave(data[48:], 2)

block0 += rs0
block1 += rs1

block0 = list(reversed(block0))
'''
rs = data[-T:]
block = data[:-T]
padding = [0 for i in range(K - len(block))]

print(len(block))
print(block + padding)
print(rs)

block = list(reversed(padding + block + rs))

generator = 0x61
roots = [0x0, 0x1, 0x2, 0x4, 0x8, 0xf, 0x10, 0x1a, 0x21, 0x27, 0x2a, 0x2d, 0x34, 0x3e]
midata = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1]

ALPHA[0] = 1
LOGTABLE[1] = 0
for i in range(1,len(ALPHA)):
    tmp = ALPHA[i-1] << 1;
    tmp = tmp ^ generator if tmp >= len(ALPHA) else tmp
    ALPHA[i] = tmp
    LOGTABLE[tmp] = i

print(list(map(hex, ALPHA)))


for root in roots:
    print(poly_eval(midata, root))



print("---------------------------")

poly = list(reversed([0x01, 0x1b, 0x3b, 0x22, 0x34, 0x38]))
for i in range(64):
    print(i, poly_eval(poly, i))

print("---------------------------")

for generator in range(len(ALPHA), 2*len(ALPHA)):
    zeroes = [0] * T

    ALPHA[0] = 1
    LOGTABLE[1] = 0
    for i in range(1,len(ALPHA)):
        tmp = ALPHA[i-1] << 1;
        tmp = tmp ^ generator if tmp >= len(ALPHA) else tmp
        ALPHA[i] = tmp
        LOGTABLE[tmp] = i


    if len(set(ALPHA)) != N:
        continue

    roots = list(filter(lambda x: poly_eval(block, x) == 0, range(len(ALPHA))))

    if len(roots) < T:
        continue

    print("{:x} {}: {}".format(generator, len(roots), [hex(x) for x in roots]))

