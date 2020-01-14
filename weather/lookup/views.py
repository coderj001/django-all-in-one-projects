from django.shortcuts import render
# Create your views here.
def home(request):
	import json
	import requests
	api_req=requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20001&distance=25&API_KEY=EABC3623-4BCF-4437-8D1B-B515131C0BC7').content
	try:
		api=json.loads(api_req)
	except Exception as e:
		api="ERROR...."
	return render(request,'home.html',{'api':api})
def about(request):
	return render(request,'about.html',{})