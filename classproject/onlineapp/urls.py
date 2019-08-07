from django.urls import path,include
import debug_toolbar
import onlineapp.views_backup as views

from onlineapp.views import *
from rest_framework.authtoken.models import Token


app_name="onlineapp"

urlpatterns = [
        # path('debug/', include(debug_toolbar.urls)),
         path('hello/',views.hello_world),
        # path('get_my_clg/<str:clg>',views.get_my_clg),
        # path('get_all_colleges/',views.get_all_colleges),
        # path('college_student_details/<int:id>',views.studentDetails),

        path('testView/',views.test_view_debugger),

        path('colleges/',CollegeView.as_view(),name='colleges_html'),
        path('colleges/<int:pk>',CollegeView.as_view(),name='college_details'),
        path('colleges/<str:acronym>',CollegeView.as_view(),name='college_details'),

        path('college/add',ChangeCollegeView.as_view(),name='addCollege'),
        path('college/<int:pk>/edit',ChangeCollegeView.as_view(),name='editCollege'),
        path('college/<int:pk>/delete',ChangeCollegeView.as_view(),name='deleteCollege'),

        path('college/<int:pk>/addStudent',ChangeStudent.as_view(),name='addStudent'),
        path('college/<int:pk>/editStudent/<int:studentId>',ChangeStudent.as_view(),name='editStudent'),
        path('college/<int:pk>/deleteStudent/<int:studentId>', ChangeStudent.as_view(), name='deleteStudent'),

        path('login/',LoginView.as_view(),name='login'),
        path('signup/',SignUpView.as_view(),name='signup'),
        path('logout/',LogOut,name='logout'),


        path('colleges_rest/',College_Rest,name='colleges_all_rest'), #GET
        path('colleges_rest/<int:pk>/',College_Rest,name='college_detail_rest'), #GET
        path('colleges_rest/add/',College_Rest,name='colleges_add_rest'), #POST
        path('colleges_rest/<int:pk>/edit/',College_Rest,name='college_edit_rest'), #PUT
        path('colleges_rest/<int:pk>/delete/',College_Rest,name='college_delete_rest'), #DELETE

        path('colleges_rest/<int:pk>/students/',College_Students_Rest.as_view(),name='college_students_list'),
        path('colleges_rest/<int:pk>/student/<int:studentId>/',Student_View_Rest.as_view(),name = 'student_detail'),
        path('colleges_rest/<int:pk>/addStudent/',Student_View_Rest.as_view(),name='student_add_rest'),
        path('colleges_rest/<int:pk>/student/<int:studentId>/edit/',Student_View_Rest.as_view(),name='student_edit_rest'),
        path('colleges_rest/<int:pk>/student/<int:studentId>/delete/',Student_View_Rest.as_view(),name='student_delete_rest'),


]

from rest_framework.authtoken import views
urlpatterns.extend([
    url(r'^api-token-auth/', views.obtain_auth_token)
])