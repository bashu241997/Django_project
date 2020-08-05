from django.urls import path ,include

from rest_framework.routers import DefaultRouter
from profiles import views


router=DefaultRouter()
router.register('hello-viewset',views.Helloviewset, basename = 'hello-viewset')

router.register('profile-viewset',views.Userprofileviewset)

router.register('profilefeed-viewset',views.userprofileviewset)

urlpatterns = [
    path('helloapi',views.HelloApiView.as_view()),
    path('login/',views.Userloginapiview.as_view()),
    path('',include(router.urls))
    
]
