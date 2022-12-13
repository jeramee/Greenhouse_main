from django.urls import path
from . import views

'''Have to add multiple instances of greenhouse gh1-7
 this way because Django doesn't allow 
embedded functions that pass arguments inside of HTML documents'''
'''The greenhouse object won't be able to keep track of
which greenhouse it is associated with this is because
Django uses some old technology.'''


urlpatterns = [
    path('', views.home, name='home'),
    path('greenhouse/<int:pk>/', views.greenhouse, name='greenhouse'),

    path('gh1/', views.gh1, name='gh1'),
    path('gh2/', views.gh2, name='gh2'),
    path('gh3/', views.gh3, name='gh3'),
    path('gh4/', views.gh4, name='gh4'),
    path('gh5/', views.gh5, name='gh5'),
    path('gh6/', views.gh6, name='gh6'),
    path('gh7/', views.gh7, name='gh7'),
    
    path('devices/gh1_add_device/', views.gh1_add_device, name='gh1_add_device'),
    path('devices/gh2_add_device/', views.gh2_add_device, name='gh2_add_device'),
    path('devices/gh3_add_device/', views.gh3_add_device, name='gh3_add_device'),
    path('devices/gh4_add_device/', views.gh4_add_device, name='gh4_add_device'),
    path('devices/gh5_add_device/', views.gh5_add_device, name='gh5_add_device'),
    path('devices/gh6_add_device/', views.gh6_add_device, name='gh6_add_device'),
    path('devices/gh7_add_device/', views.gh7_add_device, name='gh7_add_device'),

    path('fruits/gh1_add_fruit/', views.gh1_add_fruit, name='gh1_add_fruit'),
    path('fruits/gh2_add_fruit/', views.gh2_add_fruit, name='gh2_add_fruit'),
    path('fruits/gh3_add_fruit/', views.gh3_add_fruit, name='gh3_add_fruit'),
    path('fruits/gh4_add_fruit/', views.gh4_add_fruit, name='gh4_add_fruit'),
    path('fruits/gh5_add_fruit/', views.gh5_add_fruit, name='gh5_add_fruit'),
    path('fruits/gh6_add_fruit/', views.gh6_add_fruit, name='gh6_add_fruit'),
    path('fruits/gh7_add_fruit/', views.gh7_add_fruit, name='gh7_add_fruit'),

    path('herbs/gh1_add_herb/', views.gh1_add_herb, name='gh1_add_herb'),
    path('herbs/gh2_add_herb/', views.gh2_add_herb, name='gh2_add_herb'),
    path('herbs/gh3_add_herb/', views.gh3_add_herb, name='gh3_add_herb'),
    path('herbs/gh4_add_herb/', views.gh4_add_herb, name='gh4_add_herb'),
    path('herbs/gh5_add_herb/', views.gh5_add_herb, name='gh5_add_herb'),
    path('herbs/gh6_add_herb/', views.gh6_add_herb, name='gh6_add_herb'),
    path('herbs/gh7_add_herb/', views.gh7_add_herb, name='gh7_add_herb'),

    path('vegetables/gh1_add_vegetable/', views.gh1_add_vegetable, name='gh1_add_vegetable'),
    path('vegetables/gh2_add_vegetable/', views.gh2_add_vegetable, name='gh2_add_vegetable'),
    path('vegetables/gh3_add_vegetable/', views.gh3_add_vegetable, name='gh3_add_vegetable'),
    path('vegetables/gh4_add_vegetable/', views.gh4_add_vegetable, name='gh4_add_vegetable'),
    path('vegetables/gh5_add_vegetable/', views.gh5_add_vegetable, name='gh5_add_vegetable'),
    path('vegetables/gh6_add_vegetable/', views.gh6_add_vegetable, name='gh6_add_vegetable'),
    path('vegetables/gh7_add_vegetable/', views.gh7_add_vegetable, name='gh7_add_vegetable'),


    path('vegetable/<int:pk>/', views.vegetable, name='vegetable'),
    path('fruit/<int:pk>/', views.fruit, name='fruit'),
    path('herb/<int:pk>/', views.herb, name='herb'),
    path('device/<int:pk>/', views.device, name='device')
]

