import matplotlib.pyplot as plt

y = [1,-1,1,-1,1,-1] #sample input array y
x = [1,2,3,4,5,6]    #sample input array x

plt.figure(1)
plt.clf()
plt.plot(x,y,label="y=f(x)")
plt.legend()
plt.show()        #check image plot2.jpg for output
