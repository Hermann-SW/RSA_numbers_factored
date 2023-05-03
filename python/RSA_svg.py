# pylint: disable=C0103
#                 invalid-name
"""svg demo"""
from sys import argv
from typing import Union
from RSA_numbers_factored import RSA, RSA_number, bits


def svg(n: Union[int, RSA_number]) -> str:
    """
    Generate prime factors svg.
    """
    r = RSA().get_(n)
    if len(r) < 4:
        return ""
    p, q = r[2:4]
    s = (
        '<svg width="'
        + str(bits(q))
        + '" height="'
        + str(bits(p))
        + '" xmlns="http://www.w3.org/2000/svg">'
    )
    for y in range(bits(p) - 1, -1, -1):
        for x in range(bits(q) - 1, -1, -1):
            col = "blue" if (p & (1 << y) != 0 and q & (1 << x) != 0) else "cyan"
            s += (
                '<rect x="'
                + str(x)
                + '" y="'
                + str(y)
                + '" width="1" height="1" fill="'
                + col
                + '" stroke-width="0"/>'
            )
    s += "</svg>"
    return s


if len(argv) < 2:
    print('"python svg.py X" creates SVG image for factored RSA-X')
else:
    print(svg(int(argv[1])))
