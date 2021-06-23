from django.urls import path
from . import views



urlpatterns = [
    path('newlisting/', views.new_listing, name='new_listing'),    
    path('homepage/', views.personal_homepage, name='personal_homepage'),    
    path('alllistings/', views.all_listings, name='all_listings'),    
    path('interested/<int:listing_id>', views.interested, name='interested'),    
    path('notinterested/<int:listing_id>', views.not_interested, name='notinterested'),    
    path('listing/<int:j_id>', views.single_listing, name='single_listing'),    
    path('myapplications/intertested', views.my_applications_intertested, name='my_applications_intertested'),    
    path('myapplications/applied', views.my_applications_applied, name='my_applications_applied'),    
    path('myapplications/interview', views.my_applications_interview, name='my_applications_interview'),    
    path('myapplications/accepted', views.my_applications_accepted, name='my_applications_accepted'),    
    path('myapplications/rejected', views.my_applications_rejected, name='my_applications_rejected'),    
    path('myapplications/<int:application_id>', views.my_applications_single, name='my_applications_single'),    
    path('update/<slug:pk>/delete', views.DeleteComment.as_view(), name= 'delete_update'),

]