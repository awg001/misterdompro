from django.urls import path, re_path
from rest_framework import routers
from .api import BruschatkaViewSet

from .views import *

router = routers.DefaultRouter()
router.register('api/bruschatka', BruschatkaViewSet, 'bruschatka')

urlpatterns = router.urls
#     path('', BruschatkaHome.as_view(), name='home'),
#     path('krovlya/', Krovlya.as_view(), name='krovlya'),
#     path('contact/', contact, name='contact'),
#     path('login/', login, name='login'),
#     path('about/', about, name='about'),
#     path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
#     path('category/<slug:cat_slug>/', BruschatkaCategory.as_view(), name='category'),
# ]
