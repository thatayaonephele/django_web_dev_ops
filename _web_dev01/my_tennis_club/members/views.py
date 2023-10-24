from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

"""
Using internal entered data created by me...
def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))
"""

"""
Printing out data stored from a django db connected to a website
def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

"""

"""
def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'greeting': 1,
  }
  return HttpResponse(template.render(context, request))
"""

"""Define a section in a master template that should be replaced by a section in a child template
def testing(request):
  template = loader.get_template('childtemplate.html')
  return HttpResponse(template.render())
"""

"""Insert a comment in the Django code
def testing(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())
"""

"""
def testing(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())
"""



"""An example of the use of a parent loop counter
def testing(request):
    template = loader.get_template('template.html')
    context = {
        'cars': ['Ford', 'Volvo', 'BMW'],
        'colors': ['Red', 'Green', 'Blue']
    }
    return HttpResponse(template.render(context, request))
"""




"""Printing Out the data from the server db in table format


def testing(request):
    mydata = Member.objects.all().values()
    template = loader.get_template('output.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

# Check out template.html to see how the mymembers object
# was used in the HTML code.
"""

"""
Filtering out a specific record based on a 1st name search
def testing(request):
    mydata = Member.objects.filter(firstname='Thati').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

# Check out template.html to see how the mymembers object

"""

"""
Get all records where firstname starts with the letter "T":

def testing(request):
  mydata = Member.objects.filter(firstname__istartswith='T').values()
  template = loader.get_template('db_data_manipulation.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
"""

"""
Get all records where id is between 2 and 4:

def testing(request):
  mydata = Member.objects.filter(id__range=(2,4)).values()
  #mydata = Member.objects.filter(firstname__range=('A','M').values()
  template = loader.get_template('db_data_manipulation.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
"""



    #Examples of field look_up syntax uses: All Field lookup keywords must be specified with the fieldname, followed by two(!) underscore characters
    # mydata = Member.objects.filter(id__lte=3).values()
    # mydata = Member.objects.filter(firstname__range=('A','M').values()
    #mydata = Member.objects.filter(id__lt=3).values()
    #mydata = Member.objects.filter(id__gte=3).values()
    #mydata = Member.objects.filter(id__gt=3).values()
    #mydata = Member.objects.filter(firstname__in=['Tobias', 'Lerato', 'Thati']).values()
    #mydata = Member.objects.filter(firstname__iexact='thati').values() #the case insensitive exact match:Still returns Thati
    #mydata = Member.objects.filter(firstname__exact='thati').values() #The case sensitive exact match :Doesnt return Thati
    #mydata = Member.objects.filter(firstname__iendswith='o').values()
    #mydata = Member.objects.filter(firstname__endswith='O').values() #Functions do not show case sensitivity...
    #mydata = Member.objects.filter(lastname__icontains='ma').values()#Functions do not show case sensitivity...
    #mydata = Member.objects.filter(lastname__icontains='ma').values()
    #non field look_ups
    #mydata = Member.objects.filter(lastname='Phele', id=2).values() #So if you not using contains...make sure you enter the exact name...Aan example of a specific row...
    #mydata = Member.objects.filter(firstname='thato').values() | Member.objects.filter(firstname='Thati').values() #logical or. Using this shows firstname is case sensitive
    #mydata = Member.objects.filter(Q(firstname='Thati') | Q(firstname='thato')).values() #logical or using q expressions
    #mydata = Member.objects.all().order_by('firstname').values() #default order set as ascending
    #mydata = Member.objects.all().order_by('-firstname').values() #reversed order(descending)
    #mydata = Member.objects.all().order_by('lastname', '-id').values() #combination of more than 1 arg inside order_by...
    #mydata = Member.objects.values_list('phone') Prints out a single colunm...
"""
def testing(request):
    mydata = Member.objects.values_list('phone')
    template = loader.get_template('db_data_manipulation.html')

    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

"""


def testing(request):
  template = loader.get_template('template.html')
