from django.views import View
from onlineapp.models import *
from django.views.generic import ListView
from onlineapp.forms import AddCollege,StudentForm,MockTestForm
from django.http import HttpResponseRedirect

from django.shortcuts import render,get_object_or_404,redirect
from django.urls import resolve
from django.contrib.auth.mixins import LoginRequiredMixin

class ChangeStudent(LoginRequiredMixin,View):

    login_url = '/login/'

    def get(self,request,**kwargs):

        #if not request.user.is_authenticated:
        #    return redirect("onlineapp:login")


        if not request.user.is_superuser:
            return redirect("/colleges/"+str(kwargs.get('pk')))

        mockTestForm = MockTestForm()
        studentForm = StudentForm()

        if resolve(request.path_info).url_name == 'deleteStudent':
            Student.objects.get(pk=kwargs.get('studentId')).delete()
            return HttpResponseRedirect('/colleges')
        title = ''
        if kwargs.get('studentId',-1)!=-1:
            student = get_object_or_404(Student, pk=kwargs.get('studentId'))
            mocktest = get_object_or_404(MockTest1,student=student)
            studentForm = StudentForm(instance=student)
            mockTestForm = MockTestForm(instance=mocktest)
            title = 'Edit Student'
        else:
            title = 'Add Student'
        return render(
            request,
            template_name= "Add_Student.html",
            context = {
                'student':studentForm,
                'mockTest':mockTestForm,
                'title':title
            }
        )

    def post(self,request,*args,**kwargs):

        if not request.user.is_superuser:
            return redirect("/colleges/"+str(kwargs.get('pk')))

        if not request.user.is_authenticated:
            return redirect("onlineapp:login")

        if resolve(request.path_info).url_name == 'editStudent':
            student = get_object_or_404(Student,pk=kwargs.get('studentId'))
            mock = MockTest1.objects.get(student=student)
            total = sum(list(map(int,[request.POST['problem'+str(i)] for i in range(1,5)])))
            #total = int(request.POST['problem1'])+int(request.POST['problem2'])+int(request.POST['problem3'])+int(request.POST['problem4'])
            mock.total=total
            studentForm = StudentForm(request.POST,instance=student)
            mockForm = MockTestForm(request.POST,instance=mock)
            if studentForm.is_valid() and mockForm.is_valid():
                studentForm.save()
                mockForm.save()
                return HttpResponseRedirect('/colleges')
            else:
                return render(
                    request,
                    template_name="Add_Student.html",
                    context={
                        'student': studentForm,
                        'mockTest': mockForm,
                        'title': 'Edit Student'
                    }
                )
        student = Student(college = College.objects.get(id=kwargs.get('pk')))
        mock = MockTest1()
        total = sum(list(map(int, [request.POST['problem' + str(i)] for i in range(1, 5)])))
        mock.total = total
        studentForm = StudentForm(request.POST, instance=student)
        if studentForm.is_valid():
            studentForm.save()
            mock.student = student
            mockForm = MockTestForm(request.POST, instance=mock)
            if mockForm.is_valid():
                mockForm.save()
            else:
                return render(
                    request,
                    template_name="Add_Student.html",
                    context={
                        'student': studentForm,
                        'mockTest': mockForm,
                        'title': 'Edit Student'
                    }
                )
        else:
            mockForm = MockTestForm(request.POST,instance=mock)
            return render(
                request,
                template_name="Add_Student.html",
                context={
                    'student': studentForm,
                    'mockTest': mockForm,
                    'title': 'Add Student'
                }
            )
        return HttpResponseRedirect('/colleges')

