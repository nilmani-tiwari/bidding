from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate ,logout#add this
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from . models import *
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
# Create your views here.
def check(email):
    if(re.fullmatch(regex, email)):
        print("Valid Email")
        return True
    else:
        print("Invalid Email")
        return False

def is_admin(user):
    try:
        user_exist=user.groups.filter(name='admin').exists()
        print("user_exist",user_exist)
        return user.is_authenticated and user_exist
    except Exception as e:
        return False

def is_vender(user):
    try:
        user_exist=user.groups.filter(name='vender').exists()
        print("user_exist",user_exist)
        return user.is_authenticated and user_exist
    except Exception as e:
        return False



def logoutUser(request):
    logout(request)
    return redirect('/')

def register_user(request):
    context={}
    if request.method == "POST":
        username=request.POST.get("username")
        name=request.POST.get("name")
        email=request.POST.get("email")
        passs=request.POST.get("pass")
        re_pass=request.POST.get("re_pass")
        temp={"name":name,"username":username,"email":email,"passs":passs,"re_pas":re_pass}
        print(temp)
        context.update(temp)
        if not check(email) :
            messages.info(request, f"invailed email {email}")
            return render(request,"register.html",context)
        if passs!=re_pass:
            messages.info(request, f"Password mismatch")
            return render(request,"register.html",context)
        
        if username.isdigit() and len(username)==10:
            username=int(username)
        elif not check(username):
            messages.info(request, f"invailed email {email}")
            print("Please Enter a valied email or contact number")
            return render(request,"register.html",context)
        elif check(username):
            username=username
            
            
        admin=request.POST.get("admin")
        full_name=name.split()
        first_name=full_name[0]
        last_name=" ".join(full_name[1:])
        print(name,email,passs,re_pass)
        print(admin)
        
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.email=email
            user.first_name=first_name
            user.last_name=last_name
            if admin=="admin":
                user.groups.add(1)
            else:
                user.groups.add(2)
            user.set_password(passs)
            user.save()
            messages.success(request, f"User Successfully registered")
            context={}
            return render(request,"register.html",context)
        else:
            messages.info(request, f"User ID {username} Already exists")
            print("User by this email or contact Already exists")
            return render(request,"register.html",context)
        print(request,11111111111111111)
    
    return render(request,"register.html",context)

def login_user(request):
    if request.method == "POST":
        email=request.POST.get("email")
        passs=request.POST.get("pass")
        print(email,passs)
        
        user = authenticate(username=email, password=passs)
        if user is not None:
            login(request, user)
            messages.success(request, f"You are now logged in as {email}.")
            if is_admin(user):
                return redirect("home")
            elif is_vender(user):
                return redirect("vhome")
        else:
            messages.info(request,"Invalid username or password.")
		
        
    
    return render(request,"login.html")




###############################admin side code 


@user_passes_test(is_admin)
def home(request): 
    context={}
    user=request.user
         
    return render(request,'home.html',context )


@user_passes_test(is_admin)
def add_items(request): 
    context={}
    user=request.user
    if request.method == "POST":
        title=request.POST.get("title")
        desc=request.POST.get("desc")
        price=request.POST.get("price")
        exp_date=request.POST.get("exp_date")
        image=request.FILES["image"]
        
        print(title,desc,price,exp_date,image,222222222222222222)
        Item(user=user,name=title,image=image,description=desc,basePrice=price,exp_date=exp_date).save()
        
        messages.success(request, f"New project or contract items added successfully.")

         
    return render(request,'add_items.html',context )



@user_passes_test(is_admin)
def all_items(request): 
    context={}
    user=request.user
    all_items=Item.objects.filter(user=user)
    context.update({"all_items":all_items})    
    return render(request,'all_items.html',context )

@user_passes_test(is_admin)
def all_vender(request): 
    context={}
    user=request.user
    # all_items=Item.objects.filter(user=user)
    # context.update({"all_items":all_items})    
    return render(request,'all_vender.html',context )

from django.db.models import F
from django.db.models.query import QuerySet

@user_passes_test(is_admin)
def loest_vender(request,item_id): 
    context={}
    user=request.user
    item=Item.objects.get(id=item_id)
    context.update({"item":item})   
    
    mapping=ItemVenderMapping.objects.filter(item=item).order_by("price")
    # mapping.annotate(related_value=range(1,3))
    mapping.union()
    context.update({"mapping":enumerate(mapping,start=1)})
    
    loest_bidder=mapping.first()
    context.update({"loest_bidder":loest_bidder})
    #have to send all vender details from mapping with thair price
    ## and have to send loest vender details 
    return render(request,'loest_vender.html',context )





############vender side code ############################################

@user_passes_test(is_vender)
def vhome(request): 
    context={}
    user=request.user
    all_items=Item.objects.all()
    context.update({"all_items":all_items})      
    return render(request,'vendor/vhome.html',context )


@user_passes_test(is_vender)
def bid_item(request,item_id): 
    context={}
    user=request.user
    item=Item.objects.get(id=item_id)
    context.update({"item":item}) 
    
    item_map=ItemVenderMapping.objects.filter(item=item).order_by("price")  
    loest_obj=item_map.first()
    if loest_obj:
        last_loest_price=loest_obj.price
        print("**************",loest_obj.price)
    else:
        last_loest_price=None
        
    if last_loest_price is  None:
        last_loest_price=item.basePrice
    context.update({"last_loest_price":last_loest_price}) 
    
    if request.method == "POST":
        itemid=request.POST.get("item_id")
        price=request.POST.get("price") 
        item=Item.objects.get(id=itemid)
        print(itemid,price)
        map,created=ItemVenderMapping.objects.get_or_create(vender=user,item=item)
        map.price=price
        map.save()
        if created:
            messages.success(request, f"You have bidden successfully")
            print("You have bidden successfully")
        else:
            messages.success(request, f"Price updated successfully")
            print("Price updated successfully")
        
    return render(request,'vendor/bid_item.html',context )