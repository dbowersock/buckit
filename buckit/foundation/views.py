# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from foundation.models import Request


def requests_index(request):
    current_requests = Request.objects.all().order_by('-deadline')[:5]
    return render_to_response('requests.html', {'current_requests': current_requests})
    
def request_detail(request, request_id):
	try:
		p = Request.objects.get(pk=request_id)
	except Request.DoesNotExist:
		raise Http404
	return render_to_response('request_detail.html', {'request': p})

def index(request):
    return render_to_response('index.html')

def new_request(request):
	if request.method == 'POST':
		form = NewRequestForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			deadline = form.cleaned_data['deadline']
			amount = form.cleaned_data['amount']
			
			return HttpResponseRedirect('/requests/')
	else:
		form = NewRequestForm()
		
	return render(request, 'NewRequest.html', { 'form': form, })