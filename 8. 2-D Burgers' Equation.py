import numpy
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

#Set up the grid
nx = 41
dx = 2/(nx-1)
ny = 41
dy = 2/(ny-1)
nt = 120
c = 1
sigma = .0009
nu = .01
dt = sigma*dx*dy/nu

x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)

u = numpy.ones((ny,nx))
v = numpy.ones((ny,nx))
un = numpy.ones((ny,nx))
vn = numpy.ones((ny,nx))
comb = numpy.ones((ny,nx))

#Set up ICs
u[int(0.5/dy):int(1/dy+1),int(0.5/dx):int(1/dx+1)]=2
v[int(0.5/dy):int(1/dy+1),int(0.5/dx):int(1/dx+1)]=2

###Plot ICs
##fig = plt.figure(figsize=(11,7),dpi=100)
##ax = plt.axes(projection='3d')
##X,Y = numpy.meshgrid(x,y)
##ax.plot_surface(X,Y,u,cmap=cm.viridis,rstride=1,cstride=1)
##ax.plot_surface(X,Y,v,cmap=cm.viridis,rstride=1,cstride=1)
##ax.set_xlabel('$x$')
##ax.set_ylabel('$y$')
##ax.set_zlabel('$z$')
##plt.show()

#Implement 2D Burgers' equation
for n in range(nt+1):
    un = u.copy()
    vn = v.copy()
##    for j in range(1,ny-1):
##        for i in range(1,nx-1):
##            u[j,i] = un[j,i]\
##                     -dt*un[j,i]/dx*(un[j,i]-un[j,i-1])\
##                     -dt*vn[j,i]/dy*(un[j,i]-un[j-1,i])\
##                     +nu*dt/dx**2*(un[j,i+1]-2*un[j,i]+un[j,i-1])\
##                     +nu*dt/dy**2*(un[j+1,i]-2*un[j,i]+un[j-1,i])
##            v[j,i] = vn[j,i]\
##                     -dt*un[j,i]/dx*(vn[j,i]-vn[j,i-1])\
##                     -dt*vn[j,i]/dy*(vn[j,i]-vn[j-1,i])\
##                     +nu*dt/dx**2*(vn[j,i+1]-2*vn[j,i]+vn[j,i-1])\
##                     +nu*dt/dy**2*(vn[j+1,i]-2*vn[j,i]+vn[j-1,i])

    u[1:-1,1:-1] = un[1:-1,1:-1]\
                   -dt*un[1:-1,1:-1]/dx*(un[1:-1,1:-1]-un[1:-1,0:-2])\
                   -dt*vn[1:-1,1:-1]/dy*(un[1:-1,1:-1]-un[0:-2,1:-1])\
                   +nu*dt/dx**2*(un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,0:-2])\
                   +nu*dt/dy**2*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[0:-2,1:-1])
    v[1:-1,1:-1] = vn[1:-1,1:-1]\
                   -dt*un[1:-1,1:-1]/dx*(vn[1:-1,1:-1]-vn[1:-1,0:-2])\
                   -dt*vn[1:-1,1:-1]/dy*(vn[1:-1,1:-1]-vn[0:-2,1:-1])\
                   +nu*dt/dx**2*(vn[1:-1,2:]-2*vn[1:-1,1:-1]+vn[1:-1,0:-2])\
                   +nu*dt/dy**2*(vn[2:,1:-1]-2*vn[1:-1,1:-1]+vn[0:-2,1:-1])
#BCs
    u[0,:]=1
    u[-1,:]=1
    u[:,0]=1
    u[:,-1]=1
    v[0,:]=1
    v[-1,:]=1
    v[:,0]=1
    v[:,-1]=1
    
#Plot
fig = plt.figure(figsize=(11,7),dpi=100)
ax = plt.axes(projection='3d')
X,Y = numpy.meshgrid(x,y)
#ax.plot_surface(X,Y,u,cmap=cm.viridis,rstride=1,cstride=1)
ax.plot_surface(X,Y,v,cmap=cm.viridis,rstride=1,cstride=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
plt.show()
