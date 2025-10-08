from django.shortcuts import render, redirect
from Card.models import *
# Create your views here.
from datetime import date



uid =''

def signup(request):
    if request.method == 'POST':
        pic = request.FILES['image']
        firstname = request.POST.get('first-name')
        lastname = request.POST.get('last-name')
        occupation= request.POST.get('occupation')
        loc=request.POST.get('location')
        goals=request.POST.get('goal')
        number=request.POST.get('num')
        since=date.today()
        print(since)
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            User_id.objects.create(dp=pic, First_Name=firstname,Last_Name=lastname,Occupation=occupation,location=loc,member_since=since,mobile=number,goal=goals,Email=email,Password=password)
            return redirect('../login/')

    return render(request,'signup.html')

def login(request):
    info = User_id.objects.all()

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        for i in info:
            if i.Email == email and i.Password == password:
                global uid
                uid = email
                return redirect('../dashbord/')
                pass

    return render(request,'login.html')

def dashbord(request):
    Course_name = Course_name_list.objects.all()
    print(Course_name[0].logo)
    data = {
        'UID':uid,
        'Course_name' : Course_name[:3],
        'num' : range(3)
    }
    return render(request, 'Dashbord.html',data)

def profile(request):
    print('------------')
    # print(uid)
    userinfo = User_id.objects.all()

    if request.method=='POST':

        pic = request.FILES['profileImage']
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        occupation= request.POST.get('occup')
        loc=request.POST.get('loc')
        goals=request.POST.get('goal')
        number=request.POST.get('num')

        updateid = User_id.objects.filter(Email=uid)[0]
        updateid.dp=pic
        updateid.First_Name = firstname
        updateid.Last_Name = lastname
        updateid.Occupation = occupation
        updateid.location = loc
        updateid.goal=goals
        updateid.mobile=number
        updateid.save()
        return render(request, 'profile.html',{'uid':uid,'IDdata':userinfo})

    return render(request, 'profile.html',{'uid':uid,'IDdata':userinfo})

def course_display(request):
    Course_name = Course_name_list.objects.all()
    return render(request, 'course.html',{'list':Course_name})

def course_detail(request,cname):
    Course_data = Course_name_list.objects.all()
    global courseName
    courseName = cname
    for i in Course_data:
        if i.Course_Title==cname:
            Course_data={
                'cTitle' : i.Course_Title,
                'syllabus':i.Course_syllabus,
                'intro':i.course_intro,
                'description':i.Course_description,
                'level':i.Course_level,
                'ctime':i.Course_time
            }
            break
    Module= Modules_list.objects.filter(course__Course_Title=cname)

    data = {
        'Course' : Course_data,
        'Module':Module,

    }
    print(data)

    return render(request, 'course_detail.html',data)

def card_lern(request,cname):
    # global courseName
    # print(cname)
    # module_index=Modules_list.objects.filter(course__Course_Title=cname).order_by('course__Course_Title','Module_Index')
    card_Data=Card.objects.filter(course__Course_Title=cname).order_by('module__Module_Index','Card_Index')
    # print(card_Data)

    cdata={'cdata':list(card_Data.values())}
    # cdata={'cdata':card_Data}


    # print(Data['CardData'][0].Card_Index)

    return render(request, 'card_lern.html',cdata)


