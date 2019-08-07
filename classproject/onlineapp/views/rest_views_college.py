from onlineapp.serialiser.Serializer import *
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from onlineapp.models import *
from rest_framework.views import APIView


class Custom_Token_Label(TokenAuthentication):
    keyword = 'MyKeyWord'

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes((SessionAuthentication, BasicAuthentication, Custom_Token_Label,))
@permission_classes((IsAuthenticated,))
def College_Rest(request,*args,**kwargs):

    if request.method == 'POST':
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            College.objects.get(id = kwargs.get('pk')).delete()
            return Response(data=None,status = status.HTTP_202_ACCEPTED)
        except:
            return Response(data=None,status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        college = College.objects.get(id=kwargs.get('pk'))
        serializer = CollegeSerializer(college,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)


    if kwargs:
        colleges = College.objects.get(**kwargs)
        serialized = CollegeSerializer(colleges)

    else:
        colleges = College.objects.all()
        serialized = CollegeSerializer(colleges,many=True)

    return Response(serialized.data)

# @api_view(['GET'])
# def College_Students_Rest(request,*args,**kwargs):
#
#     college = College.objects.get(kwargs.get('pk'))
#     students = list(college.student_set.order_by("-mocktest1__total"))
#     studentSerializer = StudentSerializer(students,many=True)
#     return Response(studentSerializer.data)


class College_Students_Rest(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication,)

    def get(self,request,*args,**kwargs):
        college = College.objects.get(id=kwargs.get('pk'))
        students = list(college.student_set.order_by("-mocktest1__total"))
        studentSerializer = StudentSerializer(students, many=True)
        return Response(studentSerializer.data)

class Student_View_Rest(APIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication,)

    def get(self,request,*args,**kwargs):
        student  = Student.objects.get(id=kwargs.get('studentId'))
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        student_serializer = StudentDetailSerializer(data=request.data,context={'pk':kwargs.get('pk')})
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_201_CREATED)
        return Response(student_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self,request,*args,**kwargs):
        student = Student.objects.get(id=kwargs.get('studentId'))
        serializer = StudentSerializer(data=request.data,instance=student)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        try:
            student = get_object_or_404(Student,id=kwargs.get('studentId'))
            student.delete()
            return Response(None,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(None,status=status.HTTP_400_BAD_REQUEST)


