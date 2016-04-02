from matplotlib import pyplot
import numpy
import cv2

im1 = pyplot.imread("im0-600.jpg")
im2 = pyplot.imread("im1-600.jpg")

g1 = cv2.cvtColor(im1, cv2.COLOR_BG2RGRAY)

print "length im1", numpy.shape(im1)
print "length im2", numpy.shape(im2)

s1 = im1[:,300,0]
s2 = im2[:,300,0]

print "length s1", numpy.shape(s1)
print "length s2", numpy.shape(s2)

f1 = open("slice1.txt","w")
f2 = open("slice2.txt","w")

for k in range(379):
	f1.write(str(im1[k,300,0]) + "\n")
	f2.write(str(im2[k,300,0]) + "\n")

f1.close()
f2.close()