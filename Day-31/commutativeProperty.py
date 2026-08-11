# verify  commutative property 
import numpy as np
a = np.array([2, 4, 6])

print(3 * a)
print(a * 3)

print(np.array_equal(3 * a, a * 3))