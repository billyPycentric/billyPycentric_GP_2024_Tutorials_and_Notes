### Python modules explained

import math
import random
import customModule as module_c


print(__name__)

print(module_c.__name__)

if(module_c.__name__ == "__main__"):
    print(module_c.hello())
else:
    print("The func is not run from this script")