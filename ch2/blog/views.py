# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.views import View

from blog.models import Post # import model class for lookup table
from django.http import HttpResponse
from django.shortcuts import render

def landing(request):
	return HttpResponse("landing page")

def home(request):
	return render(request, 'blog/home.html')

def news(request):
	temp = ['문재인', '오바마', '김정은', '푸틴', '아베']
	context = {'presidents' : temp}
	return render(request, 'blog/news.html', context = context)

def contact(request):
	return render(request, 'blog/contact.html')

def test(request, *args, **kwargs): # why?
	temp = kwargs['year'] * 1000
	return HttpResponse(temp)

class test1(View):
	def get(self, request, *args, **kwargs):
		temp = kwargs['year'] * 1111
		response = HttpResponse(temp)
		return response

	def post(self, request, *args, **kwargs):
		temp = kwargs['year'] * 9999
		response = HttpResponse(temp)
		return response

# #-----ListView
# class PostLV(ListView):
# 	model = Post
# 	template_name = 'blog/post_all.html'
# 	context_object_name = 'posts'
# 	paginate_by = 2

# #----DetailView
# class PostDV(DetailView) :
# 	model = Post

# #-----ArchiveView
# class PostAV(ArchiveIndexView):
# 	model = Post
# 	date_field = 'modify_date'

# #-----YearArchiveView
# class PostYAV(YearArchiveView):
# 	model = Post
# 	date_field = 'modify_date'
# 	make_object_list = True

# class PostMAV(MonthArchiveView):
# 	model = Post
# 	date_field = 'modify_date'

# class PostDAV(DayArchiveView):
# 	model = Post
# 	date_field = 'modify_date'

# class PostTAV(TodayArchiveView):
# 	model = Post
# 	date_field = 'modify_date'
