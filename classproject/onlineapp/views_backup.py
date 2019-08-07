from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
from .models import *
from django.shortcuts import render_to_response
import logging

def hello_world(request):
    print(request)
    logger = logging.getLogger('onlineapp')
    logger.info('Test Info Log')
    logger.error('Test error log')
    htmlCode = '''
        <html>
            <head></head>
            <body>
                <b>Hello world</b>
            </body>
        </html>
    '''
    return HttpResponse(htmlCode)

def test_view_debugger(request):

    return HttpResponse("First View")

def get_my_clg(request,clg):
    #return HttpResponse(College.objects.get(acronym=clg).name)
    return render(request,'college_details_disp.html',{'clgName' : College.objects.get(acronym=clg).name})

def get_all_colleges(request):
    # clgs = College.objects.all()
    # result = '<table border=1><tr><th>Acronym</th><th>College</th></tr>'
    # for clg in clgs:
    #     result+='<tr>'
    #     result+='<td>'+clg.acronym+'</td>'
    #     result+='<td>'+clg.name+'</td>'
    #     result+='</tr>'
    # result+='</table>'

    return render(request,'college_details_disp.html',{'clgs':College.objects.all()})
    #return HttpResponse(result)

def studentDetails(request,id):
    clg = College.objects.get(id=id)
    details = Student.objects.filter(college=clg).values('id','name','mocktest1__total')
    print(details)
    return render(request,'student_details.html',{'clgName':clg.name,'details':details})

def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

def handler500(request, exception, template_name="500.html"):
    response = render_to_response("500.html")
    response.status_code = 500
    return response