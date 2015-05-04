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
from pprint import pprint

def graph(request):
	#x = [1,2,3,4,5]
	#y = [5,2,6,0,7]
	#y = ""
	#response = urllib2.urlopen("http://192.168.43.168:8080/")
	response = urllib2.urlopen("http://aqi.iitk.ac.in:9000/metrics/station/893?d=03%2F05%2F2015&h=23")
	#print response.read()
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

def airquality(request):
	response = urllib2.urlopen("http://aqi.iitk.ac.in:9000/metrics/station/893?d=04%2F05%2F2015&h=23")
	datajson = response.read()
	datajson = json.loads(datajson)
	save_path = '/home/kartik/Documents/Projects/evsgraph/static/static/'
	for gas_data in datajson["metrics"]:
		###print gas_data["name"]
		# var rawFile = new XMLHttpRequest();
		# rawFile.open("GET", gas_data["name"]+".txt", false);
		filename = gas_data["name"]+".txt" 
		#print filename
		fo = open(save_path+filename, "wb")
		for i in gas_data["data"]:
			###print str(i["value"])
			fo.write(str(i["value"]))
			fo.write("\n")	
		fo.close()
	return render(request,"Clients.html",{})