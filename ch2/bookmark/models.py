from django.db import models
#from __future__ import unicode_literals # python 2.x 지원

#from django.utils.encoding import python_2_unicode_compatible #객체를 문자열로 표현__str__()

class Bookmark(models.Model):
	title = models.CharField(max_length=100, blank=True, null=True)
	url = models.URLField('url', unique=True)

	def __str__(self):
		return self.title


