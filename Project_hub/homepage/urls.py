"""Project_hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.firstpage, name='First Login Page'),
    path('admin-login', views.adminloginpage, name='Admin Login Page'),
    path('admin-index', views.adminindex, name='Admin Index Page'),
    path('admin-project', views.adminproject, name='Admin Project Page'),
    path('adminproject-list/', views.adminprojectlist, name='Admin Project List'),
    path('adminproject-add', views.adminprojectadd, name='Admin Project Add'),
    path('singleproject-info', views.projectinfosingle, name='Admin Project Single Info'),
    path('admin-client', views.adminclient, name='Admin Client Page'),
    path('adminproject-update',views.adminprojectupdate, name="Admin Project Update"),
    path('adminproject_search',views.adminproject_search, name='Admin search project'),
    path('adminclient-list/', views.adminclientlist, name='Admin Client List'),
    path('adminclient-add',views.adminclientadd,name= 'Admin Client Add'),
    path('adminclient-update', views.adminclientupdate, name="Admin Client Update"),
    path('adminclient-search', views.adminclient_search, name='Admin search Client'),
    path('adminrenew-project', views.adminrenew_project, name='Admin Renew Project'),
    path('adminadd-prosuccess', views.addprosucess, name='Admin Project add Successfully'),
    path('project-singlerecord/<int:project_id>/', views.adminproject_singlerecord, name="Admin Project Single Record Show"),
    path('adminupdate-prosuccess/<int:project_id>/', views.adminproject_updatesuccess, name='Admin Project Update Success'),
    path('adminproject-delete/<int:project_id>/', views.adminproject_deletesuccess, name="ADmin project Delete SUccessfully"),

    path('adminadd-clientsuccess', views.addclientsuccess, name='Admin Client Add Success'),
    path('adminupdate-clientsuccess/<int:client_id>/', views.adminclient_updatesuccess, name='Admin Client Update Success'),
    path('adminclient-view/<int:client_id>/', views.adminclientview, name="Admin Client View"),
    path('adminclient-delete/<int:client_id>/', views.adminclient_deletesuccess, name="ADmin Client Delete SUccessfully"),
    path('user-reglist/', views.admin_userreg, name=' Admin User Reg List'),
    path('admin-userview/', views.admin_userview, name=' Admin User Reg single view page'),
    path('adminuser-updatesuccess/<int:user_id>/', views.adminuser_updatesuccess, name=' Admin User Reg single update page'),
    path('adminuser-deletesuccess/<int:user_id>/', views.adminuser_deletesuccess, name=' Admin User Reg single Delete page'),


    path('user-login/', views.loginpage, name='User Login Page'),
    path('user-signup', views.signuppage, name="User Signup Page"),
    path('index-page/', views.home, name='Home Page'),
    path('about-page', views.about, name='About Page'),
    path('message-page/', views.messagepage, name='Message Page'),
    path('message-addsuccess', views.messageaddsuccessfully, name='Message ADD SUCCESS Page'),
    path('service-page', views.service, name='Service Page '),
    path('project-page', views.projectp, name='Project Page'),
    path('contact-page', views.contact, name='Contact Page'),
    path('renew-page/<int:project_id>/', views.renew, name='Project Renew Plan Page'),
    path('projectrenew-page', views.user_projectrenew, name='User Project Renew Page'),
    path('dreamproject-page', views.dreamproject, name='Dream Project'),
    path('useradd-prosuccess', views.userproject_addsuccess, name='User Project add Successfully'),
    path('payment-page/',views.payment, name='user side payment page'),
    path('payment-QRcode/',views.qrcode, name='user side QR payment page')

]
