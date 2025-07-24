#I am creating the file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def analyze(request):
    djtext = request.GET.get('text', 'default')

    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')

    if removepunc == "on":
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        #logic for removing punctuation
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params = {'purpose' : 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose' : ' Remove New Lines ', 'analyzed_text': analyzed}
    if(removepunc != "on" and newlineremover != "on" and fullcaps != "on"):
        return HttpResponse("Please Select Any Operation")
    return render(request, 'analyze.html', params)
