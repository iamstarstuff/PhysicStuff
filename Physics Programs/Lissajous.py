import numpy as np
import matplotlib.pyplot as plt

m = np.arange(1,11)
n = np.arange(1,11)
theta = np.deg2rad(np.arange(1,721,1)) # already convert to radians
phase = [30,45,60,90]

def f1(m):
    return np.sin(m*theta)

def f2(n,phi):
    return np.sin(n*theta+phi)

figmain = plt.figure(figsize=(60,60),dpi=300,constrained_layout=True)
subfigs = figmain.subfigures(2,2)

figmain.suptitle("Lissajous Figures for different phases", fontsize=50)

for outerind, subfig in enumerate(subfigs.flat):
    subfig.suptitle(f"Lissajous Figures \n\n $\sin(n\\theta+\phi)$ vs $\sin(m\\theta)$ for\
 n and m = 1 to 10 respectively \n\n Phase={phase[outerind]} degrees",fontsize=20)
    ax = subfig.subplots(10,10)
    for i in m:
        for j in n:
            ax[i-1,j-1].plot(f2(j,np.deg2rad(phase[outerind])),f1(i),label=f"m={i},n{j}")

            # remove x and y ticks to make it look aesthetic
            ax[i-1,j-1].set_xticks([])  #removes x ticks as list is empty
            ax[i-1,j-1].set_yticks([])  ##removes x ticks as list is empty

            # Put titles only on 1st row to signify n 
            # ylabels only on 1st coloumn to signify m
            ax[0,j-1].set_title(f"n={n[j-1]}")
        ax[i-1,0].set_ylabel(f"m={m[i-1]}",rotation='horizontal',labelpad=20)
plt.savefig("Lissajous_Master.png")
