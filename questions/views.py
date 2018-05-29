# Create your views here.
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

import logging

class TopicForm(forms.Form):
    interest = forms.BooleanField(label="Do you have a topic you are interested in studying?")
    supervisor = forms.BooleanField(label="Will someone supervise a thesis on this topic?")
    
class AreaForm(forms.Form):
    publications = forms.BooleanField(label="Is there a substantial amount of literature in your field?")
    open_questions = forms.BooleanField(label="Are there multiple open questions in your field?")
    recent_discovery = forms.BooleanField(label="Was there a major discovery in the field in recent years?")
    
class SupervisorForm(forms.Form):
    communicative = forms.BooleanField(label="Is your supervisor communicative?")
    organised = forms.BooleanField(label="Is your supervisor organised?")
    
class CareerForm(forms.Form):
    academia = forms.BooleanField(label="Do you want a career in academia?")

NUM_PAGES = 4

def topic_questions(request):
    logging.debug("method: %s"%request.method)
    
    if request.method == 'GET':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/area/')
    return render(request, 'questions.html',{'form':form,
                                             'page':1,
                                             'NUM_PAGES':NUM_PAGES})
        
def area_questions(request):
    if request.method == 'GET':
        form = AreaForm()
    else:
        form = AreaForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/supervisor/')
    return render(request, 'questions.html',{'form':form,
                                             'page':2,
                                             'NUM_PAGES':NUM_PAGES})
    
def supervisor_questions(request):
    if request.method == 'GET':
        form = SupervisorForm()
    else:
        form = SupervisorForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/career/')
    return render(request, 'questions.html',{'form':form,
                                             'page':3,
                                             'NUM_PAGES':NUM_PAGES})
    
def career_questions(request):
    if request.method == 'GET':
        form = CareerForm()
    else:
        form = CareerForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/yes/')
    return render(request, 'questions.html',{'form':form,
                                             'page':4,
                                             'NUM_PAGES':NUM_PAGES})
    