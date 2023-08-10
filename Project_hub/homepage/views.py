from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


from .models import Project
from .models import client
from .models import msgbox

# from .models import user

import datetime
from django.db.models.functions import ExtractMonth

# Create your views here.
@login_required(login_url='login')

def home(request):

    # if request.method == 'POST':
    #     id = request.POST['txtmsgid']
    #     fname = request.POST['txtname']
    #     email = request.POST['txtemail']
    #     mobile = request.POST['txtmobile']
    #     service = request.POST['txtservice']
    #     msg = request.POST['txtmessage']
    #
    #     x = msgbox(request.POST)
    #
    #     x.msg_id = id
    #     x.msg_name = fname
    #     x.msg_email = email
    #     x.msg_mobile = mobile
    #     x.msg_service = service
    #     x.msg_message = msg
    #
    #     x.save()

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def projectp(request):
    return render(request, 'project.html')

def contact(request):
    return render(request, 'contact.html')

def renew(request,project_id):
    x = Project.objects.get(project_id= project_id)

    context = {
        'projectlist': x,

    }
    return render(request, 'renew.html',context)

def user_projectrenew(request):
    x = None  # Initialize 'x' with a default value
    data_received = request.session.get('data_pass')
    print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    print(data_received)
    if request.method == 'POST':
        u = request.POST.get('txtusername')
        n = data_received
        print(type(n))

        x = Project.objects.filter(project_username =n)
    else:
        pass

    context = {'projectlist':x ,'username_received':data_received }
    return render(request, 'userproject_renew.html', context)


    # x = Project.objects.all()
    #y= User.objects.all()



def dreamproject(request):
    return render(request, 'dreamproject.html')

def firstpage(request):
    return render(request, 'firstpage.html')

def adminloginpage(request):
    return render(request, 'adminloginpage.html')

def adminindex(request):

    username = request.POST['txtusername']
    password = request.POST['txtpassword']

    if(username=='admin' and password=='super'):
        return render(request, 'adminindex.html')
    else:
        return render(request, 'adminloginerror.html')


def signuppage(request):
    if request.method =='POST':
        uname = request.POST.get('txtusername')
        email = request.POST.get('txtemail')
        pass1 = request.POST.get('txtpassw1')
        pass2 = request.POST.get('txtpassw2')

        print(uname)
        print(email)
        print(pass1)
        print(pass2)

        if pass1!=pass2:
            return HttpResponse("Your Password and Confirm Password are not same!!")
        else:
            my_user, created = User.objects.get_or_create(username=uname, email=email)
            if created:
                my_user.set_password(pass1)
                my_user.save()
                return redirect('/user-login')
            else:
                return HttpResponse("Username already exists. Please choose a different username.")

    return render(request, 'signup.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        # print(username, pass1)
        user = authenticate(request, username=username, password=pass1)

        request.session['data_pass'] = username

        if user is not None:
            login(request,user)
            return render(request, 'index.html',{'name':username},)
            #return redirect('/index-page')
            #return redirect('/index-page/?name=' + username)
        else:
            pass
            # return render(request, 'adminloginerror.html')
            # return HttpResponse('Username and password incorrect!!')

    x = User.objects.all()

    context = {
        'userlist' : x,

    }

    return render(request, 'login.html',context)



def loginerror(request):
    return render(request, 'adminloginerror.html')

def adminproject(request):
    return render(request, 'adminproject.html')

def adminprojectlist(request):
    x = Project.objects.all()

    return render(request, 'adminproject_projectlist.html',{'projectlist':x})


def adminprojectadd(request):
    return render(request, 'adminproject_addproject.html')

def projectinfosingle(request):
    return render(request, 'project_infosingle.html')

def adminclient(request):
    return render(request, 'adminclient.html')

def adminprojectupdate(request):
    return render(request, 'adminproject_updateproject.html')

def adminproject_search(request):
    return render(request, 'adminproject_search.html')

def adminclientlist(request):
    x = client.objects.all()

    return render(request,'adminclient_clientlist.html',{'clientlist':x})


def adminclientadd(request):
    return render(request, 'adminclient_addclient.html')

def adminclientupdate(request):
    return render(request, 'adminclient_update.html')


def adminclient_search(request):
    return render(request, 'adminclient_search.html')

def adminrenew_project(request):

        if request.method == 'POST':
            m = request.POST.get('txtdatestart')
            print(m)
            x = Project.objects.filter(project_enddate=m)
        else:
            x = Project.objects.all()  # Fetch all projects from the database

        return render(request, 'adminrenewproject.html', {'projectlist': x})


def addprosucess(request):
    if request.method == 'POST':
        i = request.POST['txtprojectid']
        u = request.POST['txtusername']
        n = request.POST['txtprojectname']
        c = request.POST['txtclientname']
        t = request.POST['txttechnology']
        tm = request.POST['txtteam']
        pi = request.POST['txtprojectinfo']
        pt = request.POST['txtprojecttype']
        im = request.POST['projectimg']
        pl = request.POST['txtlink']
        sd = request.POST['txtdatestart']
        ed = request.POST['txtdateend']
        y = request.POST['txtyear']
        dc = request.POST['txtcostdev']
        rc = request.POST['txtcostren']

        x = Project(request.POST)

        x.project_id = i
        x.project_username = u
        x.project_name = n
        x.project_clientname = c
        x.project_technology = t
        x.project_team = tm
        x.project_info = pi
        x.project_type = pt
        x.project_image = im
        x.project_link = pl
        x.project_startdate = sd
        x.project_enddate = ed
        x.project_validity = y
        x.project_dcost = dc
        x.project_rcost = rc

        x.save()

        return render(request, 'adminproaddsuccess.html')


def adminproject_singlerecord(request, project_id):
    x = Project.objects.get(project_id = project_id)

    return render(request, 'adminproject_singlerecord.html',{'projectlist':x})


def adminproject_updatesuccess(request, project_id):
    if request.method == 'POST':
        i = request.POST['txtprojectid']
        u = request.POST['txtusername']
        n = request.POST['txtprojectname']
        c = request.POST['txtclientname']
        t = request.POST['txttechnology']
        tm = request.POST['txtteam']
        pi = request.POST['txtprojectinfo']
        pt = request.POST['txtprojecttype']
        im = request.POST['projectimg']
        pl = request.POST['txtlink']
        sd = request.POST['txtdatestart']
        ed = request.POST['txtdateend']
        y = request.POST['txtyear']
        dc = request.POST['txtcostdev']
        rc = request.POST['txtcostren']

        x = Project.objects.get(project_id=project_id)

        x.project_username = u
        x.project_name = n
        x.project_clientname = c
        x.project_technology = t
        x.project_team = tm
        x.project_info = pi
        x.project_type = pt
        x.project_image = im
        x.project_link = pl
        x.project_startdate = sd
        x.project_enddate = ed
        x.project_validity = y
        x.project_dcost = dc
        x.project_rcost = rc

        x.save()
        print(pt)
        return render(request, 'adminproject_updatesuccess.html')


def adminproject_deletesuccess(request, project_id):
    if request.method== 'POST':
        x = Project.objects.get(project_id=project_id)

        x.delete()

        return render(request, 'adminproject_deletesuccess.html')


def addclientsuccess(request):

    if request.method == 'POST':
        i = request.POST['txtclientid']
        n = request.POST['txtclientname']
        g = request.POST['gender']
        m = request.POST['txtmobilenumber']
        e = request.POST['txtemailid']
        a = request.POST['txtabout']
        p = request.POST['txtprojectname']
        im = request.POST['image']
        l = request.POST['txtlink']

        x = client(request.POST)

        x.client_id = i
        x.client_name = n
        x.client_gender = g
        x.client_mobile = m
        x.client_email = e
        x.client_about = a
        x.client_projectname = p
        x.client_img = im
        x.client_link = l

        x.save()

        return render(request, 'adminclientaddsuccess.html')

def adminclientview(request, client_id):
    x = client.objects.get(client_id=client_id)

    return render(request, 'adminclientview.html',{'clientlist':x})


def adminclient_updatesuccess(request, client_id):
    if request.method == 'POST':
        i = request.POST['txtclientid']
        n = request.POST['txtclientname']
        g = request.POST['gender']
        m = request.POST['txtmobilenumber']
        e = request.POST['txtemailid']
        a = request.POST['txtabout']
        p = request.POST['txtprojectname']
        im = request.POST['image']
        l = request.POST['txtlink']

        x = client.objects.get(client_id=client_id)


        x.client_name = n
        x.client_gender = g
        x.client_mobile = m
        x.client_email = e
        x.client_about = a
        x.client_projectname = p
        x.client_img = im
        x.client_link = l

        x.save()

        return render(request, 'adminclient_updatesuccess.html')


def adminclient_deletesuccess(request, client_id):
    if request.method == 'POST':
        x = client.objects.get(client_id=client_id)

        x.delete()

        return render(request, 'adminclient_deletesuccess.html')


def userproject_addsuccess(request):
    if request.method == 'POST':
        u = request.POST['txtusername']
        i = request.POST['txtprojectid']
        n = request.POST['txtprojectname']
        c = request.POST['txtclientname']
        t = request.POST['txttechnology']
        tm = request.POST['txtteam']
        pi = request.POST['txtprojectinfo']
        pt = request.POST['txtprojecttype']
        im = request.POST['projectimg']
        pl = request.POST['txtlink']
        sd = request.POST['txtdatestart']
        ed = request.POST['txtdateend']
        y = request.POST['txtyear']
        dc = request.POST['txtcostdev']
        rc = request.POST['txtcostren']

        x = Project(request.POST)

        x.project_username = u
        x.project_id = i
        x.project_name = n
        x.project_clientname = c
        x.project_technology = t
        x.project_team = tm
        x.project_info = pi
        x.project_type = pt
        x.project_image = im
        x.project_link = pl
        x.project_startdate = sd
        x.project_enddate = ed
        x.project_validity = y
        x.project_dcost = dc
        x.project_rcost = rc

        x.save()

        return render(request, 'userproaddsuccess.html')


def admin_userreg(request):
    x = User.objects.all()

    return render(request, 'admin_userreg.html',{'userlist': x})

def admin_userview(request,user_id ):
    x = client.objects.get(client_id=user_id)

    return render(request, 'admin_userview.html',{'userlist':x})


def adminuser_updatesuccess(request):
    return render(request, 'adminuser_updatesuccess.html')

def adminuser_deletesuccess(request):
    return render(request, 'adminuser_deletesuccess.html')

def messagepage(request):
    x = msgbox.objects.all()

    return render(request, 'message.html', {'messagelist': x})

def messageaddsuccessfully(request):
    return render(request, 'messageaddsuccess.html')

def payment(request) :
    return render(request,'payment.html')

def qrcode(request) :
    return render(request,'payment_qrcode.html')