import sympy as sym

y1 = "-8-x"
y2= "-18-3*x"
Z = "-13-2*x"
x = sym.symbols("x")
plt = sym.plotting.plot(y1,y2, Z, (x,-15,0), show = False)
plt.ylim = (None,0)
plt.show()