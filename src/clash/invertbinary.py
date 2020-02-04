import sys
import math
import re
b = input()
b = re.sub('[0]','2',b)
b = re.sub('[1]','0',b)
print(re.sub('[2]','1',b))