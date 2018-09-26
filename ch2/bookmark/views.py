from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark # import model class for searching table

# Create your views here.
class BookmarkLV(ListView):
	model = Bookmark

class BookmarkDV(DetailView):
	model = Bookmark
