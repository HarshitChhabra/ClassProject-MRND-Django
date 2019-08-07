from django.views import View
from onlineapp.models import *
from django.views.generic import ListView
from onlineapp.forms import AddCollege
from django.http import HttpResponseRedirect

from django.shortcuts import render,get_object_or_404,redirect
from django.urls import resolve
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


class CollegeView(LoginRequiredMixin,View):

    login_url = '/login/'

    def get(self,request,*args,**kwargs):

        #if not request.user.is_authenticated:
        #    return redirect("onlineapp:login")

        if kwargs:
            college = get_object_or_404(College,**kwargs)
            #print('YES')
            #print(kwargs,*kwargs)
            students = list(college.student_set.order_by("-mocktest1__total"))
            print(students[0])
            return render(
                request,
                template_name= 'student_details.html',
                context={
                    'clgName' : college.name,
                    'details' : students,
                    'clgId' : college.id,
                    'permissions':request.user.get_all_permissions()
                }
            )

        colleges = College.objects.all()
        print('HELLO')
        print(request.user.get_all_permissions())
        return render(
            request,
            template_name="college_details_disp.html",
            context={
                'clgs':College.objects.all(),
                'title':'All Colleges | Class Project',
                'permissions':request.user.get_all_permissions()
            }
        )
#Same as above, but using ListView
class CollegeView_List(ListView):

    template_name = 'college_details_disp.html'
    queryset = College.objects.all()
    context_object_name = 'clgs'


class ChangeCollegeView(LoginRequiredMixin,View):

    login_url = '/login/'
    #permission_denied_message = 'Access Denied'
    #permission_required = []

    def get(self,request,**kwargs):

        #if not request.user.is_authenticated:
        #    return redirect("onlineapp:login")

        #if not request.user.is_superuser:
        #    return redirect("/colleges")

        if resolve(request.path_info).url_name == 'deleteCollege':

            if 'onlineapp.change_college' not in request.user.get_all_permissions(): #Return 403 Response
                return redirect("/colleges")

            College.objects.get(pk=kwargs.get('pk')).delete()
            return HttpResponseRedirect('/colleges')

        #if 'onlineapp.add_college' not in request.user.get_all_permissions():
        #    return redirect("/colleges")

        title=''
        if kwargs:

            if 'onlineapp.change_college' not in request.user.get_all_permissions():
                return redirect("/colleges")

            college = get_object_or_404(College,**kwargs)
            form = AddCollege(instance=college)
            title = 'Edit College'
        else:

            if 'onlineapp.add_college' not in request.user.get_all_permissions():
                return redirect("/colleges")

            form = AddCollege()
            title = 'Add College'
        exclude = ['id']
        return render(
            request,
            template_name="Add_College.html",
            context={
                'form':form,
                'title': title
            }
        )

    def post(self, request, *args, **kwargs):

        #if not request.user.is_authenticated:
        #    return redirect("onlineapp:login")

        #if not request.user.is_superuser:
        #    return redirect("/colleges")

        if resolve(request.path_info).url_name == 'editCollege':

            if 'onlineapp.change_college' not in request.user.get_all_permissions():
                return redirect("/colleges")

            college = College.objects.get(pk=kwargs.get('pk'))
            form = AddCollege(request.POST,instance = college)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/colleges')
            else:
                #error handle
                pass

        if 'onlineapp.add_college' not in request.user.get_all_permissions():
            return redirect("/colleges")

        form = AddCollege(request.POST)

        if form.is_valid():

            form.save()
            return HttpResponseRedirect('/colleges')
        else:
            return render(
                request,
                template_name="Add_College.html",
                context={
                    'form':form
                }
            )