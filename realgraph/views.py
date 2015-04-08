from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import StringIO
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
import urllib2
import json
def graph(request):
	#x = [1,2,3,4,5]
	#y = [5,2,6,0,7]
	#y = ""
	response = urllib2.urlopen("http://192.168.43.168:8080/")
	#response = urllib2.urlopen("http://0.0.0.0:8080/data.txt")
	data = response.read()
	#print "y"
	y = data.split('\n')
	print y
	x = []
	length = len(y)
	# y = []
	for i in range(1,length-1):
		y[i]=float(y[i])
		x.append(i)
	# x = [1,2,3,4,5]
	# y = [5,2,6,0,7]
	del y[length-1]
	del y[0]
	print len(x)
	print len(y)
	print x
	print y

	plot(x,y,linewidth=2)
	xlabel('x axis')
	ylabel('y axis')
	title('sample graph')
	grid(True)
	buffer = StringIO.StringIO()
	canvas = pylab.get_current_fig_manager().canvas
	canvas.draw()
	graphIMG = PIL.Image.fromstring("RGB",canvas.get_width_height(),canvas.tostring_rgb())
	graphIMG.save(buffer,"PNG")
	#print buffer.getvalue()
	pylab.close()
	#return render(request,"index.html",{'image':graphIMG})
	return HttpResponse(buffer.getvalue(),mimetype="image/png")


def home(request):
	return render(request,"index.html",{})