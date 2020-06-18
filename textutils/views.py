# created by amandeep
from django.http import HttpResponse
from django.shortcuts import render



"""
def about(requsest):
    return HttpResponse("<h1> hii ia amandeep singh katnoria</h1>" )




def facebook(request):
    return HttpResponse('facebook k liye''<a href=https://www.facebook.com/ <h1> click hare</h1></a>')



def django(request):
    return HttpResponse('for django'' <a href =https://www.djangoproject.com/start/<h2> click hare</h2></a>')
    """
def index(request):
    return render(request, 'index.html')


def analyze(request):
    # ani={'name':'Amandeep','place':'Himachal Pardesh'}
    djtext = request.GET.get('text', 'default')
    Removepunc = request.GET.get('Removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    print(Removepunc)
    print(djtext)
    puntuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = " "
    if Removepunc == "on":
        for char in djtext:
            if char not in puntuations:
                analyzed = analyzed + char

        ani = {'purpose': 'removed punctuatio', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', ani)
    elif fullcaps == "on":
        analyzed = ' '
        for char in djtext:
            analyzed = analyzed + char.upper()
        ani = {'purpose': 'Capitalized text is:', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', ani)
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        ani = {'purpose': 'removed new line:', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', ani)
    elif spaceremover == "on":
        analyzed =''
        for index ,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:

                analyzed = analyzed + char

        ani = {'purpose': 'removed extra space:', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', ani)
    else:
        return HttpResponse("error")

    # return HttpResponse("remove punc")



def about(request):
    return render(request,'about.html')
    
    
# def Capitalizefirst(request):
#     return HttpResponse(" Capitalizefirst   <a href='/'  <h2>back</h2></a>")
#
#
#
#
# def newlineremover(request):
#     return HttpResponse("remove  newlineremover   <a href='/' <h2>back</h2></a>")
#
#
#
#
# def spaceremover(request):
#     return HttpResponse(" spaceremover  <h2>back</h2> <a href='/' <h2>back</h2></a>")
#
#
#
# def charcount1(request):
#     return HttpResponse("charectorcount  <a href='/' <h2>back</h2></a>")
#
#

