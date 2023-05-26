from django.contrib import admin
from django.urls import path
from.import views
 


urlpatterns = [
    
    path('signup.html', views.signup, name='signup'),
    path('', views.homepage, name='index'),
    path('book/<int:id>',views.book_room ,name="book"),
    path('mybook',views.mybookings,name="mybook"),
    path('search',views.search,name="search"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout),
    path('cancel/<int:id>',views.cancel_booking),
    path('ownerlogin',views.owner_login,name='ownerlogin'),
    path('ownersignup',views.owner_signup,name="ownersignup"),
    path('ownerlogout',views.owner_logout),
    path('ownerhome',views.owner_home),
    path('addbuilding',views.add_building),
    path('viewrequest',views.view_request),
    path('view-doc/<int:id>',views.view_doc),
    path('approve/<int:id>',views.approve),
    path('reject/<int:id>',views.reject),
    
    

]