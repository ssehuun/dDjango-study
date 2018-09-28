from django.urls import include, path
from bookmark.views import BookmarkLV, BookmarkDV # import view class to call view

urlpatterns = [
	# class-based views for bookmark app
	# path('bookmark/', BookmarkLV.as_view(), name='index'),
	# path('bookmark/detail', BookmarkDV.as_view(), name='detail'),
]
