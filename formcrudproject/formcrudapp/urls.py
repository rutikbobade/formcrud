from django.urls import path
from formcrudapp import views

urlpatterns=[
    path('',views.registration),
    path('table/',views.Table,name='table'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update')

]