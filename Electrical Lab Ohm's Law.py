import matplotlib.pyplot as plt
import numpy as np
x = [5,
     7,
     9,
     11,
     13,
     15,
     17,
     19,
     21,
     23
     ]
y = [1.26,
     1.76,
     2.29,
     2.76,
     3.28,
     3.78,
     4.28,
     4.79,
     5.28,
     5.80
    ]

x = np.array(x)
y = np.array(y)

plt.plot(x,y, 'b', color='black')
plt.plot(x,y,'bo', color='black')
#plt.plot([i*0.163 for i in range(9)], '--')
plt.title('To Verify Ohm\'s Law')
plt.xlabel('Voltage (V) in V')
plt.ylabel('Current (I) in mA')
plt.grid(True, alpha=0.5, aa=True, ls='dotted', clip_on=True)


plt.show()
