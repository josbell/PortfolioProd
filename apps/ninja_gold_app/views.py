from django.shortcuts import render, HttpResponse, redirect, reverse
from datetime import datetime
import random

# Create your views here.
def index(request):
	if 'balance' not in request.session:
		request.session['balance']=0
	if 'activity' not in request.session:
		request.session['activity'] = []

	return render(request,'ninja_gold_app/index.html')

def process(request, locn):
		#local variables
		
	earning=0
	date = datetime.now().strftime('%m/%d/%Y %-I:%m %p')


	#print session['activity']

	if locn=='farm':
		earning = random.randrange(10,20)
		string = 'Earned ' + str(earning) + ' gold from the ' + locn + '!' + ' (' + date +')'
	elif locn=='cave':
		earning = random.randrange(5,10)
		string = 'Earned ' + str(earning) + ' gold from the ' + locn + '!' + ' (' + date +')'
	elif locn=='house':
		earning=random.randrange(2,5)
		string = 'Earned ' + str(earning) + ' gold from the ' + locn + '!' + ' (' + date +')'
	elif locn=='casino':
		earning=random.randrange(-50,50)
		if earning>0:
			string = 'Earned ' + str(earning) + ' gold from the ' + locn + '!' + ' (' + date +')'
		else:
			string = 'Entered a casino and lost ' + str(earning*-1) + ' gold... Ouch.. ''(' + date +')'

	request.session['activity'].append(string)
	request.session['balance']+=earning


	return redirect(reverse('ninja_gold:index'))