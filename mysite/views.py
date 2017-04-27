from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import MySQLdb
import datetime
from django.core.mail import send_mail
from booklist.models import Book

def hello(request):
    return HttpResponse("hell world")


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    c = Context({'Title': "Display the time", 'offset': offset, 'date': dt})
    return render_to_response('hours_ahead.html', c)


def date(request):
    now = datetime.datetime.now()
    t = get_template('date.html')
    c = Context({"Title": "Display the date ", "date": now})
    return render_to_response('date.html', c)


def testDB(request):
    db = MySQLdb.connect(user="me", db="mydb", password="pwd", host='localhost')
    cursor = db.cursor()


def displayhttpheader(request):
    values = request.GET
    c = Context({'values': values})
    return render_to_response('displayHeaderInfo.html', c)
def search_form(request):
    return render_to_response('search_form.html')
def search(request):
    errors=[]
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append('Please enter a search form')
        elif len(q)>20:
            errors.append('Please enter at not exceed 20characters!')
        else:
            books=Book.objects.filter(title__contains=q)
            return render_to_response('search_results.html',
                                  {'books':books,'query':q})

    return render_to_response('search_form.html', {'error': True})
def contact(request):
    errors=[]
    if request.method=='POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject')
        if not request.POST.get('message',''):
            errors.append('Enter a message')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid email address')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email','noreply@example.com'),
                ['135326531@qq.com'],
            )
            return HttpResponseRedirect('thanks.html')
    return render_to_response('contact-form.html', {'errors': errors})
