from django.shortcuts import redirect, render
from . models import *
import datetime
from django.contrib import messages




def homepage(request):
    all_location = place.objects.all()
    all_building=building_details.objects.all()
     


        
    data = {'all_location':all_location,'all_building':all_building}
    return render(request,'index.html',data)


def mybookings(request):
     uid=request.session["user_id"]
     user=user_details.objects.get(id=uid)
     book=booking.objects.filter(user_id=user)
     return render(request,'./user/mybookings.html',{'book':book})

def search(request):

    if request.method == 'POST':
        search_location = request.POST.get('search')
        cap = request.POST.get('capacity')
        print(cap)
        loc=place.objects.get(id=search_location)
        
       
        buildings = building_details.objects.filter(p_id=loc,capacity__gte=cap)
        
        
        context = {'buildings': buildings}
        return render(request, './user/search_results.html', context)
    return render(request,'./user/search_results.html')





def login(request):
    if request.method == 'POST':
        un=request.POST.get('username')
        pwd = request.POST.get('password')

        ul = user_details.objects.filter(username=un, password=pwd)
    
       
        #user_type = userlogin.objects.filter(user_type = 'user')
        if ul:
            request.session['user_name'] = ul[0].username
            request.session['user_id'] = ul[0].id
            request.session["email"]=ul[0].email
            return redirect("/")

        
        else:
            context ={ 'msg1':'Invalid username and password...!'}
            return render(request, './user/userlogsign.html',context)

    else:
        return render(request, './user/userlogsign.html')

def book_room(request, id):
    try:
        uname = request.session['user_id']
        print(uname)
    except:
        return login(request)
   

    if request.method == 'POST':
        # Get form data
        uid=request.session["user_id"]
        user=user_details.objects.get(id=uid)
        print(user)
        house_name = building_details.objects.get(id=id)
        owner_name = house_name.owner_id

        
        person = request.POST.get('person')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        aadhar = request.FILES.get('aadhar')
        covid = request.FILES.get('covid')
        price = request.POST.get('price')
        if booking.objects.filter(h_id=house_name,check_in=check_in):
            messages.info(request,"House Already Booked in this date")
            return redirect('/')


        # Save booking data to database
        booking_obj = booking(
            h_id=house_name,
            user_id=user,
            owner_id=owner_name,
            requested_date=datetime.date.today(),
            check_in=check_in,
            check_out=check_out,
            members=person,
            status="Not Approved",
            doc1=aadhar,
            doc2=covid,
        )
        booking_obj.save()

        # Redirect to success page
        messages.info(request,"Booked")
        return redirect('/')

    else:
        building = building_details.objects.get(id=id)
        
        context = {
            'build': building,
        }
        
        return render(request, './user/bookroom.html', context)
        


def signup(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        conf=request.POST["password2"]
        
        contact=request.POST["contact"]
        email=request.POST["email"]
        if pwd == conf:

            new=user_details.objects.create(username=un,password=pwd,contact=contact,email=email)
            new.save()
            print("usercreated")
            return redirect("http://127.0.0.1:8000/login")
        else:
            messages.info(request,"password not matching")
            return redirect("http://127.0.0.1:8000/signup")




       

    else:
        return render(request, './user/userlogsign.html')
    
def logout(request):

    try:
        del request.session['user_name']

        del request.session['user_id']
    except:
         return redirect("/")
    else:
        return redirect("/")
    
def cancel_booking(request, id):
    uid=request.session["user_id"]
    user=user_details.objects.get(id=uid)
    # Get the booking object
    try:
        book = booking.objects.get(id=id)
    except booking.DoesNotExist:
        messages.error(request, 'Invalid booking ID.')
        return redirect('mybook') # redirect to booking list view

    # Check if the user is authorized to cancel the booking
    if book.user_id != user:
        messages.error(request, 'You are not authorized to cancel this booking.')
        return redirect('mybook')

    # Set the booking status to "Cancelled"
    book.delete()

    messages.success(request, 'Booking cancelled successfully.')
    return redirect('mybook')


def owner_login(request):
    if request.method == 'POST':
        un = request.POST.get('email')
        pwd = request.POST.get('password')

        ul = owner_details.objects.filter(username=un, password=pwd).first()
        print(ul)
       
        #user_type = userlogin.objects.filter(user_type = 'user')
        if ul:
            if ul.is_approved == False:
                messages.info(request,'Not yet approved....')
                return redirect("http://127.0.0.1:8000/ownerlogin")
           
            request.session['oid'] = ul.id

            
            return redirect("http://127.0.0.1:8000/ownerhome")
        else:
            context ={ 'msg1':'Invalid username and password...!'}
            return render(request, './staff/stafflogsign.html',context)

    else:
        return render(request, './staff/stafflogsign.html')
    
def owner_signup(request):
    if request.method == 'POST':
       
        fname= request.POST.get('fname')
        lname = request.POST.get('lname')
        pwd = request.POST.get('password')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        file = request.FILES.get('vill')
        print(file)
        new=owner_details.objects.create(username=email,password=pwd,document=file,fname=fname,lname=lname,gender=gender,email=email,contact=contact)
        new.save()
        print("usercreated")
        return redirect("http://127.0.0.1:8000/ownerlogin")

    else:
        return render(request, './staff/stafflogsign.html')
    
def owner_logout(request):

    try:
        del request.session['oid']

        
    except:
         return redirect("http://127.0.0.1:8000/ownerlogin")
    else:
        return redirect("http://127.0.0.1:8000/ownerlogin")
    

def owner_home(request):
    id=request.session['oid'] 
    user=owner_details.objects.get(id=id)
    prp=building_details.objects.filter(owner_id=user)

    return render(request,'./staff/panel.html',{'buildings':prp})

def add_building(request):
    p=place.objects.all()
    if request.method == "POST":
        hid = request.POST["hid"]
        pid= request.POST["place"]
        hname = request.POST["housename"]
        descripton = request.POST["description"]
        capacity = request.POST["capacity"]
        img = request.FILES["image"]
        contact = request.POST["contact"]
        rental = request.POST["rental"]
        pl=place.objects.get(id=pid)
        id=request.session['oid'] 
        user=owner_details.objects.get(id=id)

        new=building_details.objects.create(h_id=hid,p_id=pl,owner_id=user,house_name=hname,description=descripton,capacity=capacity,picture=img,contact=contact,rental=rental)
        new.save()
        return redirect("http://127.0.0.1:8000/ownerhome")

    return render(request,'./staff/addroom.html',{'place':p})

def view_request(request):
    id=request.session['oid'] 
    ow=owner_details.objects.get(id=id)
    re=booking.objects.filter(owner_id=ow)
    return render(request, './staff/viewrequest.html',{'book':re})

def view_doc(request,id):
    b=booking.objects.get(id=id)
    context={'i':b}
    return render(request,'./staff/viewdoc.html',context)

def approve(request,id):
    b=booking.objects.get(id=id)
    b.status="Approved"
    b.save()
    return redirect("http://127.0.0.1:8000/viewrequest")

def reject(request,id):
    b=booking.objects.get(id=id)
    b.status="Rejected"
    b.save()
    return redirect("http://127.0.0.1:8000/viewrequest")
