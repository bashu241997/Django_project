from django.urls import path ,include

from rest_framework.routers import DefaultRouter
from profiles import views


router=DefaultRouter()
router.register('hello-viewset',views.Helloviewset, basename = 'hello-viewset')

urlpatterns = [
    path('helloapi',views.HelloApiView.as_view()),
    path('',include(router.urls))
]
