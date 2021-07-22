from django.urls import path
from . import views
urlpatterns=[
	path("", views.index, name="index"),
	path("kiran", views.kiran, name="kiran"),
	path("virat", views.virat, name="virat"),
	path("<str:name>", views.greet, name="greet")
]