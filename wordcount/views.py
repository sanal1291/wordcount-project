from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']

    wordlist=fulltext.split()
    worddict={}
    for word in wordlist:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1
    sortdict=sorted(worddict.items(), key=operator.itemgetter(1),reverse=-1)
    return render(request,'count.html', {'fulltext':fulltext,'count':len(wordlist),'worddict':sortdict})
def aboutme(request):
    return render(request,'aboutme.html')