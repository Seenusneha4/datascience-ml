import numpy as np
import os
x=np.arange(16).reshape(4,4)
header='c1 c2 c3 c4'
np.savetxt('seenu.txt',x,fmt="%d",header=header)
print("ln after loading content of the text file!!")
print(np.loadtxt('seenu.txt'))