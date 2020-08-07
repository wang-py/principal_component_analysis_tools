from modes import get_xvg_stats
from modes import modes
import sys

# input xvg file
xvgfile = sys.argv[1]
# mode number
mode = int(sys.argv[2])

mean1, mean2, cov, s, u, v = get_xvg_stats(xvgfile)

