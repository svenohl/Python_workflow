# To do:
# open file with filenames
# while through filenames
# Start with a message
print("Start visualizing ...")

# import
import numpy
#from matplotlib import pyplot

# load tab
tab = numpy.loadtxt("exp1vp02.txt",dtype=str,unpack=True)
dat = numpy.loadtxt("exp1vp02.dat",dtype=str,unpack=True)

print(len(dat))

eyex = dat[1]
eyey = dat[2]

cnt1 = 60000
cnt2 = 61000

fig1 = pyplot.plot(eyex[cnt1:cnt2],eyey[cnt1:cnt2],'.')
pyplot.xlabel('x Achxe')
pyplot.ylabel('y Achse')
pyplot.title(' Eye trace')
pyplot.axis([0, 1920, 0, 1200])
pyplot.grid(True)

pyplot.show()
#x = tab[1]
#n, bins, patches = pyplot.hist(x, 50, normed=1, facecolor='green', alpha=0.75)
