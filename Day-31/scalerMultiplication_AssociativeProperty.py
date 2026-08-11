import numpy as np
# logic:(ab)c=a(bc)
a = np.array([1, 2, 3])

left = (2 * 3) * a
right = 2 * (3 * a)

print(left)
print(right)

print(np.array_equal(left, right))