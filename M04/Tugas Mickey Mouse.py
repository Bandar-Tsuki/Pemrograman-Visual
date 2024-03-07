print("\033c")
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-20,20,10000)
plt.figure(figsize=(8,8))

y= x-x-0
y3 = 5 + (25-(x-5)**2)**0.5
y4 = 5 - (25-(x-5)**2)**0.5

plt.plot(x,y3, '-k', label='kepala')
plt.plot(x,y4, '-k')

def telinga(t1,t2):
  y= x-x-0
  y1 = t1 + (4-(x-t2)**2)**0.5
  y2 = t1 - (4-(x-t2)**2)**0.5
  plt.plot(x,y1, '-k', label='telinga')
  plt.plot(x,y2, '-k')

telinga(10,1)
telinga(10,9)

plt.legend(loc='upper center')

plt.show()
