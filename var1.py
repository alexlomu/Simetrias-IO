import sympy as sym

y1 = "8-x"
y2= "18-3*x"
Z = "13-2*x"
x = sym.symbols("x")
plt = sym.plotting.plot(y1,y2, Z, (x,0,15), show = False)
plt.ylim = (0,None)
plt.show()