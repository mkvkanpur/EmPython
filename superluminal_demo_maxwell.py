# Copyright (c) 2024 Mahendra Verma. All rights reserved.

# Authors:
# - Mahendra Verma
# - Rishabh Sahu

# This software is provided for non-commercial use only. You may not use, copy, modify, distribute, or otherwise exploit the software or any derivative works of the software for commercial purposes. Specifically, you may not sell, license, or profit from the software in any manner.

# Usage of the software is strictly limited to personal, academic, or non-commercial purposes. Any use, modification, or redistribution of this software outside of these constraints is prohibited without the explicit written consent of the copyright holder.

# THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



num_timesteps=400
n=1000

epsilon=8.85*(10**(-12))
mew=4*np.pi*(10**(-7))

Ez=np.zeros([n,n])
Hy=np.zeros([n-1,n-2])
Hx=np.zeros([n-2,n-1])

c=1/np.sqrt(epsilon*mew)
S=1/(2**0.5)
dx=1.0*(10**(-6))
dt=S*dx/c
lambd=20.0*dx
omega=2*np.pi*c/lambd

Ca=Da=1.0
Cb=dt/(epsilon*dx)
Db=dt/(mew*dx)

# fig = plt.figure()
# ax = plt.axes(xlim=(-0.0005, 0.0005-dx), ylim=(-1, 1))
# line, = ax.plot([], [], lw=2)
# x=np.arange(n)
# x=(x-500)*dx
# temp=np.zeros([1000,n])
# plt.ylim([-1,1])
#source=np.sin(omega*t)

# ax.autoscale(False)
j=0
for timesteps in range(num_timesteps):
	if (timesteps==0):
		Ez[int(n/2),int(n/2)]=1

	# Ez[int(n/2),int(n/2)]=np.sin(omega*timesteps*dt)
	Hy=Da*Hy+Db*(Ez[1:n,1:n-1]-Ez[0:n-1,1:n-1])

	Hx=Da*Hx-Db*(Ez[1:n-1,1:n]-Ez[1:n-1,0:n-1])
	Ez[1:n-1,1:n-1]=Ca*Ez[1:n-1,1:n-1]+Cb*(Hy[1:n-1,0:n-2]-Hy[0:n-2,0:n-2]+Hx[0:n-2,0:n-2]-Hx[0:n-2,1:n-1])

	# Ez[int(n/2),int(n/2)]=np.cos(omega*timesteps*dt)
	Ez[int(n/2),int(n/2)]=1
	print (timesteps)

	# if(np.mod(timesteps,5)==0):
	# 	# temp[j,:]=Ez[int(n/2),:]
	# 	j=j+1

#
# ani = animation.ArtistAnimation(fig, imz, interval=50, blit=True,repeat_delay=1000)
#
# plt.show()







##############################################################
temp=np.zeros(n)
for i in range(n):
	temp[i]=Ez[i,i]

x=np.arange(n)
x=(x-int(n/2)-1)*dx
plt.plot((x+dx)*np.sqrt(2),temp,label='$45^o$')
plt.plot(x+dx,Ez[int(n/2),:],label='$0^o$')
plt.xlim([-0.0004,0.0004])
plt.legend(fontsize=10)
plt.xlabel('Radial Distance, $r$  (in meters)',fontsize=10)
plt.ylabel('$E_z$  (arb. units)',fontsize=10)
plt.show()
##############################################################




# def init():
#     line.set_data([], [])
#     return line,
#
#
#
#
#
# def animate(i):
#     line.set_data(x+dx, temp[i,:])
#     return line,
# anim = animation.FuncAnimation(fig, animate, init_func=init,frames=319, interval=100, blit=True)
# plt.show()
