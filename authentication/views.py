fr 
        if user is not None:
            login(request, user)
            attendance_records2 = sem2_subdet.objects.filter(user=user)
            attendance_records1 = sem1_subdet.objects.filter(user=user)
            
            context = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'profile_pic': user.profile.image.url,
                'email': user.email,
                'attendance_records2': attendance_records2,
                'attendance_records1': attendance_records1,
            }
            return render(request, "authentication/home.html", context)
        else:
            messages.error(request, "Wrong credentials")
            return render(request, "authentication/login page.html")
    else:
        return render(request, "authentication/login page.html")
def aums(request):
    global context
    return render(request,"authentication/home.html",context)
def attendance(request):
    global context
    return render(request,"authentication/attendance.html",context)
def grades(request):
    global context
    return render(request,"authentication/grades.html",context)
def marks(request):
    global context
    return render(request,"authentication/marks.html",context)
def profile(request):
    global context
    return render(request,"authentication/profile.html",context)
def signout(request):
   logout(request)
   messages.success(request,"Successfully logged out")
   return redirect("home")
def pass_reset(request):
   try:
    if request.method == "POST":
     username = request.POST['username']
     if not User.objects.filter(username=username).first():
        messages.success(request,'user not found')
        return redirect('pass_reset')
     user_obj= User.objects.get(username=username)
     token=str(uuid.uuid4())
     profile_obj= Profile.objects.get(user= user_obj) 
     profile_obj.forget_password_token= token
     profile_obj.save()
     send_forget_pass_mail(user_obj.email,token)
     messages.success(request,'An email is sent')
     return redirect('pass_reset')
   except Exception as e:
    print(e)
    
    
   return render(request,"authentication/pass_reset.html")
def pass_conf(request):
   return render(request,"authentication/pass_conf.html")
def tests(request, sub_code):
    global context
    context['sub_code'] = sub_code
    return render(request, "authentication/tests.html", context)


def change_pass(request,token):
   context={}
   try:
     profile_obj = Profile.objects.filter(forget_password_token=token).first()
     context={'user_id': profile_obj.user.id}
     if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        user_id = request.POST.get('user_id')
        if new_password != confirm_password:
           messages.success(request,'Both should be equal')
           return redirect(f'/change_pass/{token}/')
        
        user_obj = User.objects.get(id=user_id)
        user_obj.set_password(new_password)
        user_obj.save()
        return redirect('home')

     
   except Exception as e:
      print(e)
   return render(request,"authentication/change_pass.html",context)
