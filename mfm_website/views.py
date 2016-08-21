from django.shortcuts import render
from .models import Program,Testimony,Gallery,Announcement,Address
# Create your views here.
def index(request):

	pQuery = Program.objects.all()
	tQuery = Testimony.objects.all().order_by('-id')[:5]
	gQuery = Gallery.objects.all().order_by('-id')[:10]
	aQuery = Announcement.objects.all().order_by('-id')[:5]
	adQuery = Address.objects.get(position="president")
	context = {
		'pQuery' : pQuery,
		'tQuery' : tQuery,
		'gQuery' : gQuery,
		'aQuery' : aQuery,
		'adQuery': adQuery
	}

	return render(request, "mfm_website/index.html", context)


def blog(request):
	return render(request, "mfm_website/blog.html")		