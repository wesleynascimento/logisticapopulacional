#!/usr/bin/env python

import matplotlib.pyplot as plt

r=[2,3,4,5]
dt=0.01


plt.figure(figsize=(8,5), dpi=96)
plt.axis([0,1,0,1.1])

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_label_coords(0.5, -0.025)

plt.rc('text', usetex=True) 
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'\textit{Tempo} (s)')
plt.ylabel(r'\textit{$x(t)$}')

plt.title(r'Crescimento populacional - $x_0 = 0.8$', fontsize=18)

for i in r:
	x=[0.55]
	t=[0.]	
	for tt in range(1000):
		x.append((i*x[-1]*(1 - x[-1])))
		t.append(t[-1]+dt)
	plt.plot(t,x,linewidth=0.8, label="r=%d" %i)
	del x

plt.legend(loc=9, mode='expand', ncol=8,prop={'size':6})
plt.savefig("dinamicapop.pdf",dpi=96)
