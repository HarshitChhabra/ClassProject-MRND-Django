import click
import openpyxl
import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE',"classproject.settings")
django.setup()

from onlineapp.models import College,Student,MockTest1


wb = openpyxl.load_workbook(filename="students.xlsx")

c = College.objects.all()
for i in c:
    print(i)

#INSERTING COLLEGE DETAILS
'''
ws = wb['Colleges']
flag=0
for row in ws.rows:
    if flag==0:
        flag=1
        continue
    vals = [cell.value for cell in row]
    data = College(name=vals[0].lower(),acronym=vals[1].lower(),location=vals[2].lower(),contact=vals[3].lower())
    data.save()

'''

#Populating Students Database
'''
ws = wb['Current']
flag=0
for row in ws.rows:
    if flag==0:
        flag=1
        continue
    vals = [cell.value for cell in row]
    clg = College.objects.get(acronym=vals[1].lower())

    data = Student(name=vals[0],email=vals[2] , db_folder=vals[3].lower() , college= clg, dropped_out = False)
    data.save()
    
    
#Dropped Out Students

ws = wb['Deletions']
flag=0
for row in ws.rows:
    if flag==0:
        flag=1
        continue
    vals = [cell.value for cell in row]
    clg = College.objects.get(acronym = vals[1].lower())

    data = Student(name=vals[0],email=vals[2] , db_folder=vals[3].lower() , college= clg, dropped_out = True)
    data.save()

'''


#Entering sutdent Marks
'''
wb = openpyxl.load_workbook(filename='dumped.xlsx')
ws = wb['mock_results']
flag=0
for row in ws.rows:
    if flag==0:
        flag=1
        continue
    vals = [cell.value for cell in row]
    temp = vals[0].split('_mock')
    temp = temp[0].split('_')
    db = temp[-1]
    student = Student.objects.get(db_folder=db)

    mock_student_result = MockTest1(problem1 = vals[1],problem2 = vals[2],problem3 = vals[3],problem4 = vals[4],total = vals[5],student = student)
    mock_student_result.save()
'''