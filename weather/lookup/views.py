from django.shortcuts import render
# Create your views here.
def home(request):
	import json
	import requests
	api_req=requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20001&distance=25&API_KEY=EABC3623-4BCF-4437-8D1B-B515131C0BC7').content
	try:
		api=json.loads(api_req)
		for i in api:
			if i['Category']['Name']=='Good':
				i['color']='good'
				i['msg']='Air quality is considered satisfactory, and air pollution poses little or no risk.'
			elif i['Category']['Name']=='Moderate':
				i['color']='moderate'
				i['msg']='Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
			elif i['Category']['Name']=='Unhealthy for Sensitive Groups':
				i['color']='usg'
				i['msg']='Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air.'
			elif i['Category']['Name']=='Unhealthy':
				i['color']='unhealthy'
				i['msg']='Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
			elif i['Category']['Name']=='Very Unhealthy':
				i['color']='veryunhealthy'
				i['msg']='Health alert: everyone may experience more serious health effects.'
			elif i['Category']['Name']=='Hazardous':
				i['color']='hazardous'
				i['msg']='Health warnings of emergency conditions. The entire population is more likely to be affected.'
	except Exception as e:
		api="ERROR...."
	return render(request,'home.html',{'api':api})
def about(request):
	return render(request,'about.html',{})