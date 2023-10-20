#crowd computing

## way 1
from statistics import mean

estimates = [1000, 1010, 1786, 2000, 1500, 1500, 100, 120, 150, 150, 145]
estimates.sort()

print(estimates)

#tv = int(0.1*len(estimates))

#estimates = estimates[tv:]
#print(estimates)

#estimates = estimates[:len(estimates)-tv]
#print(estimates)

#print(mean(estimates))

## way 2

from scipy import stats

m = stats.trim_mean(estimates, 0.1)

print(m)

#plotting graphs

import matplotlib.pyplot as plt

#passing only y - values
plt.plot([1, 2, 3, 4])

#passing both y - values and x - values
# plot(x_values, y_values)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel("Squares")

#plotting dotted graph
# ro = red dots 
# r-- = red dashes 
# bs = blue squares
# g^ = green triangles
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'g^')

# plotting the estimates

import matplotlib.pyplot as plt
import statistics
estimates = [1000, 1010, 1786, 2000, 1500, 1500, 100, 120, 150, 150, 145]

y = []

estimates.sort()
tv = 0.1*len(estimates)
tv = int(tv)
estimates = estimates[tv : len(estimates) - tv]
for i in range(len(estimates)):
    y.append(5)
    
plt.plot(estimates, y, 'r--')
plt.plot([735], [5], 'g^')
plt.plot(statistics.mean(estimates), [5], 'ro')
plt.plot(statistics.median(estimates), [5], 'bs')