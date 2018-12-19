# !/usr/bin/python3
# -*- coding:UTF-8 -*-
from matplotlib import pyplot as plt
input_values = [1,2,3,4,5]
cubic = [1,8,27,64,125]
plt.plot(input_values,cubic,linewidth=5)
plt.title('Cubic Numbers',fontsize=24)
plt.xlabel('Values',fontsize=20)
plt.ylabel('Cubic of Values',fontsize=24)
plt.tick_params(axis='both',labelsize=14)
plt.show()