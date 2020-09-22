import math
import matplotlib.pyplot as plt
import numpy as np
def logistic (t):
        return 1000./(1+999*math.exp(-2*t))

x = np.linspace(0,10,11)
y = [logistic(i) for i in x]
plt.scatter(x,y)
plt.plot(x, y)


def ode_FE(f, U_0, dt, T):
    N_t = int(round(float(T)/dt))
    u = zeros(N_t+1)
    t = linspace(0, N_t*dt, len(u))
    u[0] = U_0
    for n in range(N_t):
        u[n+1] = u[n] + dt*f(u[n], t[n])
    return u, t

for dt, T in zip((0.5, 20), (60, 100)):
    u, t = ode_FE(f=lambda u, t: 0.1*(1 - u/500.)*u, \
                               U_0=100, dt=dt, T=T)
    plt.figure()  # Make separate figures for each pass in the loop
    plt.plot(t, u, 'b-')
    plt.xlabel('t'); plt.ylabel('N(t)')
    plt.savefig('tmp_%g.png' % dt); plt.savefig('tmp_%g.pdf' % dt)