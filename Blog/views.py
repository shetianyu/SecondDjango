from django.shortcuts import render
from django.shortcuts import render
from django.template import loader , Context
from django.http import  *
from Blog.models import *
from Blog.postxml import SendRtx
from django.shortcuts import *

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = Context( {'posts':posts})
    return  HttpResponse(t.render(c))
# Create your views here.

def archiveh2(request):
    return render_to_response('H2.html' ,context_instance = RequestContext(request))

def archiveh3(request):
    SendRtx("JOB35","Repo_SHSVR9638BOTST2");
    return render_to_response('H3.html')

def wyethlist(request):
    return render_to_response('Wyeth.html' ,context_instance = RequestContext(request))

def wyethdone(request):
    SendRtx("WYETH_GET_AF_DATA_0001","Repo_SHSVR9163DS");
    return render_to_response('H3.html')


def loreallist(request):
    return render_to_response('Loreal.html' ,context_instance = RequestContext(request))
def lorealdone(request):
    SendRtx("LOREAL_JOB_0001v01","Repo_SHSVR9163DS");
    return render_to_response('LorealDone.html')
