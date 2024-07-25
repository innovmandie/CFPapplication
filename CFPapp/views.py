from audioop import reverse
import datetime

from multiprocessing import context
from pyexpat.errors import messages
import time
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import CFPForm, LoginForm,  POSTFormA1_C1, POSTFormA1_C2, POSTFormA1_C3, POSTFormA2_C1, POSTFormA2_C2, POSTFormA2_C3, POSTFormA3_C1, POSTFormA3_C2, POSTFormA3_C3, POSTFormA4_C1, POSTFormA4_C2, POSTFormA4_C3, POSTFormA5_C1, POSTFormA5_C2, POSTFormA5_C3, POSTFormA6_C1, POSTFormA6_C2, POSTFormA6_C3, POSTFormB1_C1, POSTFormB1_C2, POSTFormB1_C3, POSTFormB2_C1, POSTFormB2_C2, POSTFormB2_C3, POSTFormB3_C1, POSTFormB3_C2, POSTFormB3_C3, POSTFormB4_C1, POSTFormB4_C2, POSTFormB4_C3, POSTFormC1_C1, POSTFormC1_C2, POSTFormC1_C3, POSTFormC2_C1, POSTFormC2_C2, POSTFormC2_C3, POSTFormC3_C1, POSTFormC3_C2, POSTFormC3_C3, POSTFormC4_C1, POSTFormC4_C2, POSTFormC4_C3,  UserForm,UtilisateurForm
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import POSTForm
from django.template import loader
from django.views.generic import TemplateView
from django.db.models import Count
from .models import User_infos

from django.template.loader import get_template
#from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from .utils import render_to_pdf
from django.db.models import Q

import plotly.express as px
import plotly.graph_objects as go
from itertools import cycle
import pandas as pd
import numpy as np
import io


from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

from itertools import chain


def user_login(request):
    if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request,
                                    username=cd['username'],
                                    mail=cd['mail'],
                                    password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        #return HttpResponse('Authenticated ','successfully')
                        current_user = request.user
                        user_id = current_user.id
                        context = { 'user_id' : user_id, 'current_user' : current_user}
                        return render(request, 'questions.html', context)
                    else:
                        return HttpResponse('Disabled account')
                else:
                    #return HttpResponse('Invalid login')
                    return render(request, 'invalid_login.html')
    else:
         form = LoginForm
         return render(request, 'account/login.html', {'form': form})



def index(request):
     return render(request, 'index.html')

def parcoursresultats(request):
    user_connected=request.user.id
    A1_C1 = PostA1_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A1_C2 = PostA1_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A1_C3 = PostA1_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A2_C1 = PostA2_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A2_C2 = PostA2_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A2_C3 = PostA3_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A3_C1 = PostA3_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A3_C2 = PostA3_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A3_C3 = PostA3_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A4_C1 = PostA4_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A4_C2 = PostA4_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A4_C3 = PostA4_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A5_C1 = PostA5_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A5_C2 = PostA5_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A5_C3 = PostA5_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A6_C1 = PostA6_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A6_C2 = PostA6_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    A6_C3 = PostA6_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]

    B1_C1 = PostB1_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    B1_C2 = PostB1_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    B1_C3 = PostB1_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]

    B2_C1 = PostB2_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    B2_C2 = PostB2_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    B2_C3 = PostB2_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]

    B3_C1 = PostB3_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    B3_C2 = PostB3_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    B3_C3 = PostB3_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]

    B4_C1 = PostB4_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    B4_C2 = PostB4_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    B4_C3 = PostB4_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]

    C1_C1 = PostC1_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    C1_C2 = PostC1_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    C1_C3 = PostC1_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    C2_C1 = PostC2_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    C2_C2 = PostC2_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    C2_C3 = PostC2_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    C3_C1 = PostC3_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    C3_C2 = PostC3_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    C3_C3 = PostC3_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    C4_C1 = PostC4_C1.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    C4_C2 = PostC4_C2.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    C4_C3 = PostC4_C3.objects.filter(created_by_id=user_connected).order_by('id').reverse()[:1]
    context = {'A1_C1': A1_C1, 'A1_C2': A1_C2,'A1_C3': A1_C3, 'A2_C1': A2_C1, 'A2_C2': A2_C2,'A2_C3': A2_C3,
    'A3_C1': A3_C1, 'A3_C2': A3_C2,'A3_C3': A3_C3,'A4_C1': A4_C1, 'A4_C2': A4_C2,'A4_C3': A4_C3,'A5_C1': A5_C1, 'A5_C2': A5_C2,'A5_C3': A5_C3,'A6_C1': A6_C1, 'A6_C2': A6_C2,'A6_C3': A6_C3,
    'B1_C1': B1_C1, 'B1_C2': B1_C2,'B1_C3': B1_C3,'B2_C1': B2_C1, 'B2_C2': B2_C2,'B2_C3': B2_C3, 'B3_C1': B3_C1,'B3_C2': B3_C2,'B3_C3': B3_C3,'B4_C1': B4_C1, 'B4_C2': B4_C2,'B4_C3': B4_C3,
    'C1_C1': C1_C1, 'C1_C2': C1_C2,'C1_C3': C1_C3,'C2_C1': C2_C1, 'C2_C2': C2_C2,'C2_C3': C2_C3,'C3_C1': C3_C1,'C3_C2': C3_C2,'C3_C3': C3_C3,'C4_C1': C4_C1, 'C4_C2': C4_C2,'C4_C3': C4_C3,}
    return render(request, 'questions/cartographieparcours.html', context)



@login_required
def accueil(request):
     current_user = request.user
     user_id = current_user.id
     context = { 'user_id' : user_id, 'current_user' : current_user}
     return render(request, 'accueil.html', context)

@user_passes_test(lambda u: u.is_superuser)
def administrateur(request):
     return render(request, 'administrateur.html')


@login_required
def logout_view(request):
     logout(request)
     return render(request, 'account/logout.html')
#############
def finished(request):
     return render(request, 'finished.html')

def finishedA1(request):
     user_connected=request.user.id
     if PostA1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA1_C3.objects.filter(created_by_id=user_connected).all().exists():
         resA1_C1 = pd.DataFrame(list(PostA1_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A1_C1').order_by('id').reverse()[:1]))
         resA1_C2 = pd.DataFrame(list(PostA1_C2.objects.filter(created_by_id=user_connected).values('A1_C2').order_by('id').reverse()[:1]))
         resA1_C3 = pd.DataFrame(list(PostA1_C3.objects.filter(created_by_id=user_connected).values('A1_C3', 'time').order_by('id').reverse()[:1]))
         resA1_C3['time'] = resA1_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
         resultsA1 = pd.merge(resA1_C1, resA1_C2, how='cross')
         resultsA1 = pd.merge(resultsA1, resA1_C3, how='cross')
         df_result_A1=resultsA1[["A1_C1", "A1_C2", "A1_C3",]]
         df_result_A1.columns=["A1_C1", "A1_C2", "A1_C3"]
         resultsA1 = resultsA1.to_dict(orient='records')
         context= {'resultsA1' : resultsA1}

     return render(request, 'questions/poleA/finishedA1.html', context)

def finishedA2(request):
    user_connected=request.user.id
    if PostA2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA2_C3.objects.filter(created_by_id=user_connected).all().exists():
        resA2_C1 = pd.DataFrame(list(PostA2_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A2_C1').order_by('id').reverse()[:1]))
        resA2_C2 = pd.DataFrame(list(PostA2_C2.objects.filter(created_by_id=user_connected).values('A2_C2').order_by('id').reverse()[:1]))
        resA2_C3 = pd.DataFrame(list(PostA2_C3.objects.filter(created_by_id=user_connected).values('A2_C3', 'time').order_by('id').reverse()[:1]))
        resA2_C3['time'] = resA2_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
        resultsA2 = pd.merge(resA2_C1, resA2_C2, how='cross')
        resultsA2 = pd.merge(resultsA2, resA2_C3, how='cross')
        df_result_A2=resultsA2[["A2_C1", "A2_C2", "A2_C3",]]
        df_result_A2.columns=["A2_C1", "A2_C2", "A2_C3"]
        resultsA2 = resultsA2.to_dict(orient='records')
        context= {'resultsA2' : resultsA2}
        return render(request, 'questions/poleA/finishedA2.html', context)

def finishedA3(request):
    user_connected=request.user.id
    if PostA3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA3_C3.objects.filter(created_by_id=user_connected).all().exists():
        resA3_C1 = pd.DataFrame(list(PostA3_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A3_C1').order_by('id').reverse()[:1]))
        resA3_C2 = pd.DataFrame(list(PostA3_C2.objects.filter(created_by_id=user_connected).values('A3_C2').order_by('id').reverse()[:1]))
        resA3_C3 = pd.DataFrame(list(PostA3_C3.objects.filter(created_by_id=user_connected).values('A3_C3', 'time').order_by('id').reverse()[:1]))
        resA3_C3['time'] = resA3_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
        resultsA3 = pd.merge(resA3_C1, resA3_C2, how='cross')
        resultsA3 = pd.merge(resultsA3, resA3_C3, how='cross')
        df_result_A3=resultsA3[["A3_C1", "A3_C2", "A3_C3",]]
        df_result_A3.columns=["A3_C1", "A3_C2", "A3_C3"]
        resultsA3 = resultsA3.to_dict(orient='records')
        context= {'resultsA3' : resultsA3}

        return render(request, 'questions/poleA/finishedA3.html', context)

def finishedA4(request):
    user_connected=request.user.id
    if PostA4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA4_C3.objects.filter(created_by_id=user_connected).all().exists():
        resA4_C1 = pd.DataFrame(list(PostA4_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A4_C1').order_by('id').reverse()[:1]))
        resA4_C2 = pd.DataFrame(list(PostA4_C2.objects.filter(created_by_id=user_connected).values('A4_C2').order_by('id').reverse()[:1]))
        resA4_C3 = pd.DataFrame(list(PostA4_C3.objects.filter(created_by_id=user_connected).values('A4_C3', 'time').order_by('id').reverse()[:1]))
        resA4_C3['time'] = resA4_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
        resultsA4 = pd.merge(resA4_C1, resA4_C2, how='cross')
        resultsA4 = pd.merge(resultsA4, resA4_C3, how='cross')
        df_result_A4=resultsA4[["A4_C1", "A4_C2", "A4_C3",]]
        df_result_A4.columns=["A4_C1", "A4_C2", "A4_C3"]
        resultsA4 = resultsA4.to_dict(orient='records')
        context= {'resultsA4' : resultsA4}
        return render(request, 'questions/poleA/finishedA4.html', context)

def finishedA5(request):
    user_connected=request.user.id
    if PostA5_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA5_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA5_C3.objects.filter(created_by_id=user_connected).all().exists():
        resA5_C1 = pd.DataFrame(list(PostA5_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A5_C1').order_by('id').reverse()[:1]))
        resA5_C2 = pd.DataFrame(list(PostA5_C2.objects.filter(created_by_id=user_connected).values('A5_C2').order_by('id').reverse()[:1]))
        resA5_C3 = pd.DataFrame(list(PostA5_C3.objects.filter(created_by_id=user_connected).values('A5_C3', 'time').order_by('id').reverse()[:1]))
        resA5_C3['time'] = resA5_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
        resultsA5 = pd.merge(resA5_C1, resA5_C2, how='cross')
        resultsA5 = pd.merge(resultsA5, resA5_C3, how='cross')
        df_result_A5=resultsA5[["A5_C1", "A5_C2", "A5_C3",]]
        df_result_A5.columns=["A5_C1", "A5_C2", "A5_C3"]
        resultsA5 = resultsA5.to_dict(orient='records')
        context= {'resultsA5' : resultsA5}
        return render(request, 'questions/poleA/finishedA5.html', context)

def finishedA6(request):
    user_connected=request.user.id
    if PostA6_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA6_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA6_C3.objects.filter(created_by_id=user_connected).all().exists():
        resA6_C1 = pd.DataFrame(list(PostA6_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A6_C1').order_by('id').reverse()[:1]))
        resA6_C2 = pd.DataFrame(list(PostA6_C2.objects.filter(created_by_id=user_connected).values('A6_C2').order_by('id').reverse()[:1]))
        resA6_C3 = pd.DataFrame(list(PostA6_C3.objects.filter(created_by_id=user_connected).values('A6_C3', 'time').order_by('id').reverse()[:1]))
        resA6_C3['time'] = resA6_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
        resultsA6 = pd.merge(resA6_C1, resA6_C2, how='cross')
        resultsA6 = pd.merge(resultsA6, resA6_C3, how='cross')
        df_result_A6=resultsA6[["A6_C1", "A6_C2", "A6_C3",]]
        df_result_A6.columns=["A6_C1", "A6_C2", "A6_C3"]
        resultsA6 = resultsA6.to_dict(orient='records')
        context= {'resultsA6' : resultsA6}
        return render(request, 'questions/poleA/finishedA6.html', context)


####################
def finishedB1(request):
    user_connected=request.user.id
    if PostB1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB1_C3.objects.filter(created_by_id=user_connected).all().exists():
        resB1_C1 = pd.DataFrame(list(PostB1_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'B1_C1').order_by('id').reverse()[:1]))
        resB1_C2 = pd.DataFrame(list(PostB1_C2.objects.filter(created_by_id=user_connected).values('B1_C2').order_by('id').reverse()[:1]))
        resB1_C3 = pd.DataFrame(list(PostB1_C3.objects.filter(created_by_id=user_connected).values('B1_C3', 'time').order_by('id').reverse()[:1]))
        resB1_C3['time'] = resB1_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
        resultsB1 = pd.merge(resB1_C1, resB1_C2, how='cross')
        resultsB1 = pd.merge(resultsB1, resB1_C3, how='cross')
        df_result_B1=resultsB1[["B1_C1", "B1_C2", "B1_C3",]]
        df_result_B1.columns=["B1_C1", "B1_C2", "B1_C3"]
        resultsB1 = resultsB1.to_dict(orient='records')
        context= {'resultsB1' : resultsB1}
        return render(request, 'questions/poleB/finishedB1.html', context)
def finishedB2(request):
    user_connected=request.user.id
    if PostB2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB2_C3.objects.filter(created_by_id=user_connected).all().exists():
        resB2_C1 = pd.DataFrame(list(PostB2_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'B2_C1').order_by('id').reverse()[:1]))
        resB2_C2 = pd.DataFrame(list(PostB2_C2.objects.filter(created_by_id=user_connected).values('B2_C2').order_by('id').reverse()[:1]))
        resB2_C3 = pd.DataFrame(list(PostB2_C3.objects.filter(created_by_id=user_connected).values('B2_C3', 'time').order_by('id').reverse()[:1]))
        resB2_C3['time'] = resB2_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
        resultsB2 = pd.merge(resB2_C1, resB2_C2, how='cross')
        resultsB2 = pd.merge(resultsB2, resB2_C3, how='cross')
        df_result_B2=resultsB2[["B2_C1", "B2_C2", "B2_C3",]]
        df_result_B2.columns=["B2_C1", "B2_C2", "B2_C3"]
        resultsB2 = resultsB2.to_dict(orient='records')
        context= {'resultsB2' : resultsB2}
        return render(request, 'questions/poleB/finishedB2.html', context)

def finishedB3(request):
    user_connected=request.user.id
    if PostB3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB3_C3.objects.filter(created_by_id=user_connected).all().exists():
        resB3_C1 = pd.DataFrame(list(PostB3_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'B3_C1').order_by('id').reverse()[:1]))
        resB3_C2 = pd.DataFrame(list(PostB3_C2.objects.filter(created_by_id=user_connected).values('B3_C2').order_by('id').reverse()[:1]))
        resB3_C3 = pd.DataFrame(list(PostB3_C3.objects.filter(created_by_id=user_connected).values('B3_C3', 'time').order_by('id').reverse()[:1]))
        resB3_C3['time'] = resB3_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
        resultsB3 = pd.merge(resB3_C1, resB3_C2, how='cross')
        resultsB3 = pd.merge(resultsB3, resB3_C3, how='cross')
        df_result_B3=resultsB3[["B3_C1", "B3_C2", "B3_C3",]]
        df_result_B3.columns=["B3_C1", "B3_C2", "B3_C3"]
        resultsB3 = resultsB3.to_dict(orient='records')
        context= {'resultsB3' : resultsB3}
        return render(request, 'questions/poleB/finishedB3.html', context)

def finishedB4(request):
    user_connected=request.user.id
    if PostB4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB4_C3.objects.filter(created_by_id=user_connected).all().exists():
        resB4_C1 = pd.DataFrame(list(PostB4_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'B4_C1').order_by('id').reverse()[:1]))
        resB4_C2 = pd.DataFrame(list(PostB4_C2.objects.filter(created_by_id=user_connected).values('B4_C2').order_by('id').reverse()[:1]))
        resB4_C3 = pd.DataFrame(list(PostB4_C3.objects.filter(created_by_id=user_connected).values('B4_C3', 'time').order_by('id').reverse()[:1]))
        resB4_C3['time'] = resB4_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
        resultsB4 = pd.merge(resB4_C1, resB4_C2, how='cross')
        resultsB4 = pd.merge(resultsB4, resB4_C3, how='cross')
        df_result_B4=resultsB4[["B4_C1", "B4_C2", "B4_C3",]]
        df_result_B4.columns=["B4_C1", "B4_C2", "B4_C3"]
        resultsB4 = resultsB4.to_dict(orient='records')
        context= {'resultsB4' : resultsB4}
        return render(request, 'questions/poleB/finishedB4.html', context)

####################
def finishedC1(request):
    user_connected=request.user.id
    if PostC1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC1_C3.objects.filter(created_by_id=user_connected).all().exists():
        resC1_C1 = pd.DataFrame(list(PostC1_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'C1_C1').order_by('id').reverse()[:1]))
        resC1_C2 = pd.DataFrame(list(PostC1_C2.objects.filter(created_by_id=user_connected).values('C1_C2').order_by('id').reverse()[:1]))
        resC1_C3 = pd.DataFrame(list(PostC1_C3.objects.filter(created_by_id=user_connected).values('C1_C3', 'time').order_by('id').reverse()[:1]))
        resC1_C3['time'] = resC1_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
        resultsC1 = pd.merge(resC1_C1, resC1_C2, how='cross')
        resultsC1 = pd.merge(resultsC1, resC1_C3, how='cross')
        df_result_C1=resultsC1[["C1_C1", "C1_C2", "C1_C3",]]
        df_result_C1.columns=["C1_C1", "C1_C2", "C1_C3"]
        resultsC1 = resultsC1.to_dict(orient='records')
        context= {'resultsC1' : resultsC1}
        return render(request, 'questions/poleC/finishedC1.html', context)

def finishedC2(request):
    user_connected=request.user.id
    if PostC2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC2_C3.objects.filter(created_by_id=user_connected).all().exists():
        resC2_C1 = pd.DataFrame(list(PostC2_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'C2_C1').order_by('id').reverse()[:1]))
        resC2_C2 = pd.DataFrame(list(PostC2_C2.objects.filter(created_by_id=user_connected).values('C2_C2').order_by('id').reverse()[:1]))
        resC2_C3 = pd.DataFrame(list(PostC2_C3.objects.filter(created_by_id=user_connected).values('C2_C3', 'time').order_by('id').reverse()[:1]))
        resC2_C3['time'] = resC2_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
        resultsC2 = pd.merge(resC2_C1, resC2_C2, how='cross')
        resultsC2 = pd.merge(resultsC2, resC2_C3, how='cross')
        df_result_C2=resultsC2[["C2_C1", "C2_C2", "C2_C3",]]
        df_result_C2.columns=["C2_C1", "C2_C2", "C2_C3"]
        resultsC2 = resultsC2.to_dict(orient='records')
        context= {'resultsC2' : resultsC2}
        return render(request, 'questions/poleC/finishedC2.html', context)

def finishedC3(request):
    user_connected=request.user.id
    if PostC3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC3_C3.objects.filter(created_by_id=user_connected).all().exists():
        resC3_C1 = pd.DataFrame(list(PostC3_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'C3_C1').order_by('id').reverse()[:1]))
        resC3_C2 = pd.DataFrame(list(PostC3_C2.objects.filter(created_by_id=user_connected).values('C3_C2').order_by('id').reverse()[:1]))
        resC3_C3 = pd.DataFrame(list(PostC3_C3.objects.filter(created_by_id=user_connected).values('C3_C3', 'time').order_by('id').reverse()[:1]))
        resC3_C3['time'] = resC3_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
        resultsC3 = pd.merge(resC3_C1, resC3_C2, how='cross')
        resultsC3 = pd.merge(resultsC3, resC3_C3, how='cross')
        df_result_C3=resultsC3[["C3_C1", "C3_C2", "C3_C3",]]
        df_result_C3.columns=["C3_C1", "C3_C2", "C3_C3"]
        resultsC3 = resultsC3.to_dict(orient='records')
        context= {'resultsC3' : resultsC3}
        return render(request, 'questions/poleC/finishedC3.html', context)

def finishedC4(request):
    user_connected=request.user.id
    if PostC4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC4_C3.objects.filter(created_by_id=user_connected).all().exists():
        resC4_C1 = pd.DataFrame(list(PostC4_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'C4_C1').order_by('id').reverse()[:1]))
        resC4_C2 = pd.DataFrame(list(PostC4_C2.objects.filter(created_by_id=user_connected).values('C4_C2').order_by('id').reverse()[:1]))
        resC4_C3 = pd.DataFrame(list(PostC4_C3.objects.filter(created_by_id=user_connected).values('C4_C3', 'time').order_by('id').reverse()[:1]))
        resC4_C3['time'] = resC4_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
        resultsC4 = pd.merge(resC4_C1, resC4_C2, how='cross')
        resultsC4 = pd.merge(resultsC4, resC4_C3, how='cross')
        df_result_C4=resultsC4[["C4_C1", "C4_C2", "C4_C3",]]
        df_result_C4.columns=["C4_C1", "C4_C2", "C4_C3"]
        resultsC4 = resultsC4.to_dict(orient='records')
        context= {'resultsC4' : resultsC4}
        return render(request, 'questions/poleC/finishedC4.html', context)

def contact(request):
     return render(request, 'contact.html')

@login_required
def question(request):
     if request.method == 'POST':
            details = POSTForm(request.POST)
            if details.is_valid():
                   post = details.save(commit=False)
                   post.save()
                   user_connected=request.user.id
                   user_result=Post.objects.filter(created_by_id=user_connected).values()
                   result=user_result.order_by('time').reverse()[0]
                   #mydata = Post.objects.all().values()
                   context = { 'utilisateur': user_connected, 'question_A' : result}
                   return render(request, "data_A_user.html", context)
            else :
                   #return HttpResponse("choose the right user")
                   return render(request, "questions.html", {'form':details})

     else:
        form_post =POSTForm(None)
        return render(request, 'questions.html', {'form_post': form_post})
     return render(request, 'questions.html')

@login_required
def userview(request):
     user_connected=request.user.id
     if Post.objects.filter(created_by_id=user_connected).all().exists():
          userdata = User_infos.objects.filter(created_by_id=user_connected).values().order_by('-id').reverse()[:1]
          template = loader.get_template('userview_alone.html')
          context = { 'Utilisateur_liste' : userdata,}
          return HttpResponse(template.render(context,request))
     userdata = User_infos.objects.filter(created_by_id=user_connected).values().order_by('-id').reverse()[:1]
     return render(request, 'userview_alone.html',{'Utilisateur_liste': userdata})




@user_passes_test(lambda u: u.is_superuser)
def reponse(request):
    mydata = Post.objects.all().values()
    return render(request, "data_A.html", { 'question_A' : mydata})

@login_required
def dashboard(request):
    if request.method == 'POST':
            details = POSTForm(request.POST)
            if details.is_valid():
                   post = details.save(commit=False)
                   post.save()
                   user_connected=request.user.id
                   user_result=Post.objects.filter(created_by_id=user_connected).values()
                   result=user_result.order_by('time').reverse()[0]
                   #mydata = Post.objects.all().values()
                   context = { 'utilisateur': user_connected, 'question_A' : result}
                   return render(request, "data_A_user.html", context)
            else :
                   #return HttpResponse("choose the right user")
                   return render(request, "account/dasboard.html", {'form':details})

    else:
        form_post =POSTForm(None)
        return render(request, 'account/dashboard.html', {'form_post': form_post})
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


@login_required
def utilisateurs(request):
     if request.method == 'POST':
        details = UtilisateurForm(request.POST)
        if details.is_valid():
                 post = details.save(commit=False)
                 post.save()
                 user_connected=request.user.id
                 user_result =Utilisateur_infos.objects.filter(created_by_id=user_connected).values()[:1]
                 template = loader.get_template('finishedprofil.html')
                 context = { 'Utilisateur_liste' : user_result,}
                 return render(request, 'finishedprofil.html',context)
        else :
               return HttpResponse('Les données utilisateur ne sont pas conformes')
     else:
        form_user =UtilisateurForm(None)
        return render(request, 'account/utilisateur.html', {'form_user': form_user})

@login_required
def utilisateursinfos(request):
     if request.method == 'POST':
          details = UserForm(request.POST)
          if details.is_valid():
               post = details.save(commit=False)
               post.save()
               user_connected=request.user.id
               user_result =User_infos.objects.filter(created_by_id=user_connected).values().order_by('id').reverse()[:1]
               context = { 'Utilisateur_liste' : user_result,}
               return render(request,'finishedprofil.html', context)
     else:
          form_userinfos =UserForm()
          context= {'form_userinfos': form_userinfos}
     return render(request, 'account/utilisateur.html', context )

@login_required
def cfpinfos(request):
     if request.method == 'POST':
          details = CFPForm(request.POST)
          if details.is_valid():
               post = details.save(commit=False)
               post.save()
               return render(request,'finishedprofil.html')
     else:
          form_cfpinfos = CFPForm()
          context= {'form_cfpinfos': form_cfpinfos}
     return render(request, 'account/utilisateur.html', context )

@user_passes_test(lambda u: u.is_superuser)
def all_userview(request):
    Utilisateur_liste = CFP_infos.objects.all().values()
    context = { 'Utilisateur_liste' : Utilisateur_liste}
    return render(request, 'cfp_liste.html', context )

@user_passes_test(lambda u: u.is_superuser)
def all_cfp(request):
     cfp_liste = CFP_infos.objects.all().values()
     context = {'cfp_liste': cfp_liste}
     return render(request, 'cfp_liste.html', context)







@login_required
def chart_result(request):

     ###########for All get response########################################
     user_connected=request.user.id
     if Post.objects.filter(created_by_id=user_connected).all().exists():
          df_result=pd.DataFrame(list(Post.objects.filter(created_by_id=user_connected).values().order_by('time').reverse()[:1]))
     ########for A reponses ######################
          df_result=pd.DataFrame(df_result)
          df_result_A=df_result[["A2_CO_01", "A2_CO_02", "A2_CO_03",]]
          df_result_A.columns=["A2_CO_01", "A2_CO_02", "A2_CO_03",]
          df_result_A = df_result_A.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r=df_result_A.iloc[0]
          fig_A= px.line_polar(df_result_A,r=r, theta=["A2_CO_01", "A2_CO_02", "A2_CO_03"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360,)
          fig_A.update_traces(fill='toself')
          chart_A = fig_A.to_html()
     #####################################
          df_result_A1=df_result[["A1_CO_01", "A1_CO_02", "A1_CO_03",]]
          df_result_A1.columns=["A1_CO_01", "A1_CO_02", "A1_CO_03"]
          df_result_A1= df_result_A1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r=df_result_A1.iloc[0]
          fig_A1= px.line_polar(df_result_A,r=r, theta=["A1_CO_01", "A1_CO_02", "A1_CO_03"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360,)
          fig_A1.update_traces(fill='toself')
          chart_A1 = fig_A1.to_html()
     #####################################
          df_result_A3=df_result[["A3_C1", "A3_C2", "A3_C3",]]
          df_result_A3.columns=["A3_C1", "A3_C2", "A3_C3"]
          df_result_A3 = df_result_A3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r=df_result_A3.iloc[0]
          fig_A3= px.line_polar(df_result_A,r=r, theta=["A3_C1 ", "A3_C2", "A3_C3"], direction='clockwise', start_angle=40, line_close=True,width=360, height=360, color_discrete_sequence=["#009081","#98585f6", "#313178"])
          fig_A3.update_traces(fill='toself')
          chart_A3 = fig_A3.to_html()

          #####################################
          df_result_A4=df_result[["A4_C1", "A4_C2", "A4_C3",]]
          df_result_A4.columns=["A4_C1", "A4_C2", "A4_C3"]
          df_result_A4 = df_result_A4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r=df_result_A4.iloc[0]
          fig_A4= px.line_polar(df_result_A,r=r, theta=["A4_C1", "A4_C2", "A4_C3"], direction='clockwise', start_angle=70, line_close=True,width=360, height=360, color_discrete_sequence=["#21AB8E","#98585f6", "#1a2624"])
          fig_A4.update_traces(fill='toself')
          chart_A4 = fig_A4.to_html()

          #####################################
          df_result_A5=df_result[["A5_C1", "A5_C2", "A5_C3",]]
          df_result_A5.columns=["A5_C1", "A5_C2", "A5_C3"]
          df_result_A5 = df_result_A5.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r=df_result_A5.iloc[0]
          fig_A5= px.line_polar(df_result_A,r=r, theta=["A5_C1", "A5_C2", "A5_C3"], direction='clockwise', start_angle=70, line_close=True,width=360, height=360, color_discrete_sequence=["#CE70CC","#A558A0", "#1a2624"])
          fig_A5.update_traces(fill='toself')
          chart_A5 = fig_A5.to_html()

          #####################################
          df_result_A6=df_result[["A6_C1", "A6_C2", "A6_C3",]]
          df_result_A6.columns=["A6_C1", "A6_C2", "A6_C3"]
          df_result_A6 = df_result_A6.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r=df_result_A6.iloc[0]
          fig_A6= px.line_polar(df_result_A,r=r, theta=["A6_C1", "A6_C2", "A6_C3"], direction='clockwise', start_angle=70, line_close=True,width=360, height=360, color_discrete_sequence=["#CE70CC","#A558A0", "#502e4d"])
          fig_A6.update_traces(fill='toself')
          chart_A6 = fig_A6.to_html()



          resultallA=pd.concat([df_result_A1, df_result_A2, df_result_A3, df_result_A4, df_result_A5, df_result_A6], axis=1)
          df_result_all = resultallA.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r_all=df_result_All.iloc[0]

          fig_all= px.line_polar(df_result_all,r=r_all,theta=["A1_C1", "A1_C2", "A1_C3","A2_C1", "A2_C2", "A2_C3","A3_C1", "A3_C2", "A3_C3","A4_C1", "A4_C2", "A4_C3","A5_C1", "A5_C2", "A5_C3","A6_C1", "A6_C2", "A6_C3"], direction='clockwise', start_angle=70, line_close=True, color_discrete_sequence=["#000091","#9898f8", "#e3e3fd"],line_shape='spline', width=420, height=420)
          fig_all.update_traces(fill='toself')
          chart_all = fig_all.to_html()

          A1 = go.Scatterpolar(
               r = df_result_all[["A2_C1", "A2_C2", "A2_C3",]].iloc[0], theta = ["A2_C1", "A2_C2", "A2_C3",], mode = 'lines',   name = 'A1')
          A2 = go.Scatterpolar(
               r =df_result_all[["A1_C1", "A1_C2", "A1_C3",]].iloc[0], theta = ["A1_C1", "A1_C2", "A1_C3",], mode = 'lines', name = 'A2')
          A3 = go.Scatterpolar(
               r = df_result_all[["A3_C1", "A3_C2", "A3_C3",]].iloc[0], theta = ["A3_C1", "A3_C2", "A3_C3",], mode = 'lines',  name = 'A3')
          A4 = go.Scatterpolar(
               r =df_result_all[["A4_C1", "A4_C2", "A4_C3",]].iloc[0], theta = ["A4_C1", "A4_C2", "A4_C3",], mode = 'lines', name = 'A4')
          A5 = go.Scatterpolar(
               r =df_result_all[["A5_C1", "A5_C2", "A5_C3",]].iloc[0], theta = ["A5_C1", "A5_C2", "A5_C3",], mode = 'lines', name = 'A5')
          A6 = go.Scatterpolar(
               r =df_result_all[["A6_C1", "A6_C2", "A6_C3",]].iloc[0], theta = ["A6_C1", "A6_C2", "A6_C3",], mode = 'lines', name = 'A6')
          data = [A1,A2,A3,A4,A5,A6]
          fig = go.Figure(data = data)
          chart_all2 = fig.to_html()

          return render(request, 'questions/poleA/resultsA.html', { 'resultsA1' : resultsA1, 'chart_A1' : chart_A1, 'resultsA2' : resultsA2, 'chart_A2' : chart_A2, 'resultsA3' : resultsA3, 'chart_A3' : chart_A3,
                                                              'resultsA4' : resultsA4, 'chart_A4' : chart_A4, 'resultsA5' : resultsA5, 'chart_A5' : chart_A5, 'resultsA6' : resultsA6, 'chart_A6' : chart_A6, 'chart_all' : chart_all, 'chart_all2' : chart_all2,})

          ####################################################################
          return render(request, 'chart_result.html', context)
     else:
          return render(request, 'empty_data.html')

def error_404_view(request, exception):
     return render(request, '404.html')

def terms_of_use(request):
    return render(request, 'terms_of_use.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

@user_passes_test(lambda u: u.is_superuser)
def statistic(request):
     if PostC1_C1.objects.all().values().exists():
          list_nom=list(Utilisateur_infos.objects.values('nom'))
          list_age=list(Utilisateur_infos.objects.values('age'))
          list_anciennete=list(Utilisateur_infos.objects.values('anciennete').annotate(Count("nom")))
          list_commune=list(Utilisateur_infos.objects.values("commune").annotate(Count("nom")))
          ville_name=list(Utilisateur_infos.objects.only('commune').distinct())
          list_rattachement=list(Utilisateur_infos.objects.values("greta_rattachement").annotate(Count("nom")))
          df_all=pd.DataFrame(list(zip(list_nom, list_age, list_commune,list_rattachement)), columns=['nom', 'age', 'commune','Greta rattachement'])

          commune_dist=list(Utilisateur_infos.objects.only('commune').distinct())

          df_commune=pd.DataFrame(list_commune)
          df_rattachement=pd.DataFrame(list_rattachement)
          df_anciennete=pd.DataFrame(list_anciennete)

          palette=cycle(px.colors.sequential.PuBu)

          fig_bar=px.bar(df_commune, x='commune', y='nom__count', color_discrete_sequence=["#6a6af4","#000091", "#8585F6"])
          fig_anciennete=px.pie(df_anciennete, names='anciennete', values='nom__count', color_discrete_sequence=["#6a6af4","#000091", "#8585F6"])
          fig_rattachement=px.pie(df_rattachement, values='nom__count', names='greta_rattachement', color_discrete_sequence=["#6a6af4","#fddede", "#e3e3fd"])

          #chart_table=df_ville.to_html()
          chart_bar=fig_bar.to_html()
          chart_rattachement=fig_rattachement.to_html()
          chart_anciennete=fig_anciennete.to_html()

          context = {'chart_bar' : chart_bar, 'chart_rattachement' : chart_rattachement, 'chart_anciennete' : chart_anciennete}

          return render(request, 'statistic.html', context )
     else:
          info="Il n'y a aucune données"
          return render(request, 'statistic.html', {'info' : info} )


@user_passes_test(lambda u: u.is_superuser)
def test_view(request):

     user=Utilisateur_infos.objects.all().values()

     user_search=request.GET.get('nom')
     query=str(user_search.get("search_u"))

     context={'user': user, 'query' : query}
     return render(request, 'test_page.html', context)


@user_passes_test(lambda u: u.is_superuser)
def chart_view(request):
    searched_user=User.objects.all().values()


    #########
    user_search=request.GET
    query=str(user_search.get("search_u"))
    infos=Utilisateur_infos.objects.filter(nom=query).values_list('created_by_id')
    global infos_value
    infos_value = 0
    for el in infos:
         infos_value=el
    if Post.objects.filter(created_by_id=infos_value).all().exists():
         results=Post.objects.filter(created_by_id=infos_value).values().order_by('time').reverse()[:1]
         context={'searched_user' : searched_user, 'query' : query, 'infos' : infos, 'results' : results}
         return render(request, 'plotly_view.html',context)
    else:
     context={'searched_user' : searched_user,'infos_search' : infos,}
     return render(request, 'plotly_view.html',context)

@user_passes_test(lambda u: u.is_superuser)
def chart_view_user(request):
      if Post.objects.filter(created_by_id=infos_value).all().exists():
          df_result=pd.DataFrame(list(Post.objects.filter(created_by_id=infos_value).values().order_by('time').reverse()[:1]))
          df_result=pd.DataFrame(df_result)
          df_result_A=df_result[["A2_CO_01", "A2_CO_02", "A2_CO_03",]]
          df_result_A.columns=["A2_CO_01", "A2_CO_02", "A2_CO_03",]
          df_result_A = df_result_A.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r=df_result_A.iloc[0]
          fig_A= px.line_polar(df_result_A,r=r, theta=["A2_CO_01", "A2_CO_02", "A2_CO_03"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360)
          fig_A.update_traces(fill='toself')
          chart_A = fig_A.to_html()
     #####################################
          df_result_A1=df_result[["A1_CO_01", "A1_CO_02", "A1_CO_03",]]
          df_result_A1.columns=["A1_CO_01", "A1_CO_02", "A1_CO_03"]
          df_result_A1= df_result_A1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r=df_result_A1.iloc[0]
          fig_A1= px.line_polar(df_result_A,r=r, theta=["A1_CO_01", "A1_CO_02", "A1_CO_03"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360)
          fig_A1.update_traces(fill='toself')
          chart_A1 = fig_A1.to_html()
     #####################################
          df_result_A3=df_result[["A3_C1", "A3_C2", "A3_C3",]]
          df_result_A3.columns=["A3_C1", "A3_C2", "A3_C3"]
          df_result_A3 = df_result_A3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r=df_result_A3.iloc[0]
          fig_A3= px.line_polar(df_result_A,r=r, theta=["A3_C1 ", "A3_C2", "A3_C3"], direction='clockwise', start_angle=70, line_close=True,width=360, height=360)
          fig_A3.update_traces(fill='toself')
          chart_A3 = fig_A3.to_html()

          #####################################
          df_result_A4=df_result[["A4_C1", "A4_C2", "A4_C3",]]
          df_result_A4.columns=["A4_C1", "A4_C2", "A4_C3"]
          df_result_A4 = df_result_A4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r=df_result_A4.iloc[0]
          fig_A4= px.line_polar(df_result_A,r=r, theta=["A4_C1", "A4_C2", "A4_C3"], direction='clockwise', start_angle=70, line_close=True,width=360, height=360)
          fig_A4.update_traces(fill='toself')
          chart_A4 = fig_A4.to_html()

          #####################################
          df_result_A5=df_result[["A5_C1", "A5_C2", "A5_C3",]]
          df_result_A5.columns=["A5_C1", "A5_C2", "A5_C3"]
          df_result_A5 = df_result_A5.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r=df_result_A5.iloc[0]
          fig_A5= px.line_polar(df_result_A,r=r, theta=["A5_C1", "A5_C2", "A5_C3"], direction='clockwise', start_angle=70, line_close=True,width=360, height=360)
          fig_A5.update_traces(fill='toself')
          chart_A5 = fig_A5.to_html()

          #####################################
          df_result_A6=df_result[["A6_C1", "A6_C2", "A6_C3",]]
          df_result_A6.columns=["A6_C1", "A6_C2", "A6_C3"]
          df_result_A6 = df_result_A5.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r=df_result_A6.iloc[0]
          fig_A6= px.line_polar(df_result_A,r=r, theta=["A6_C1", "A6_C2", "A6_C3"], direction='clockwise', start_angle=70, line_close=True,width=360, height=360, color_discrete_sequence=["#6a6af4","#98585f6", "#313178"])
          fig_A6.update_traces(fill='toself')
          chart_A6 = fig_A6.to_html()






          return render(request, 'result_view.html', {'chart_A1': chart_A1,'chart_A_view': chart_A, 'chart_A3': chart_A3, 'chart_A4': chart_A4,'chart_A5': chart_A5, 'chart_A6': chart_A6})

      else:
           return render(request, 'plotly_view.html')










      ###################Step questions A1##########################################
@login_required
def step1_A1(request):
     initial={'A1_C1' :request.session.get('A1_C1', None)}
     if request.method == 'POST':
          form = POSTFormA1_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "A1_C1"]= form.cleaned_data["A1_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_A1')
     else:
          form = POSTFormA1_C1()
     return render(request, 'questions/poleA/step1_A1.html', {'form': form})
@login_required
def step2_A1(request):
     if request.method == 'POST':
          form = POSTFormA1_C2(request.POST or None)
          if form.is_valid():
               request.session[ "A1_C2"]= form.cleaned_data[ "A1_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_A1')
     else:
          form = POSTFormA1_C2()
     return render(request, 'questions/poleA/step2_A1.html', {'form': form})

@login_required
def step3_A1(request):
     if request.method == 'POST':
          form = POSTFormA1_C3(request.POST)
          if form.is_valid():
               request.session[ "A1_C3"]= form.cleaned_data[ "A1_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedA1')
     else:
          form = POSTFormA1_C3()
     return render(request, 'questions/poleA/step3_A1.html', {'form': form})

@login_required
def step1_A2(request):
     initial={'A2_C1' :request.session.get('A2_C1', None)}
     if request.method == 'POST':
          form = POSTFormA2_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "A2_C1"]= form.cleaned_data["A2_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_A2')
     else:
          form = POSTFormA2_C1()
     return render(request, 'questions/poleA/step1_A2.html', {'form': form})

@login_required
def step2_A2(request):
     if request.method == 'POST':
          form = POSTFormA2_C2(request.POST or None)
          if form.is_valid():
               request.session[ "A2_C2"]= form.cleaned_data[ "A2_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_A2')
     else:
          form = POSTFormA2_C2()
     return render(request, 'questions/poleA/step2_A2.html', {'form': form})

@login_required
def step3_A2(request):
     if request.method == 'POST':
          form = POSTFormA2_C3(request.POST)
          if form.is_valid():
               request.session[ "A2_C3"]= form.cleaned_data[ "A2_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedA2')
     else:
          form = POSTFormA2_C3()
     return render(request, 'questions/poleA/step3_A2.html', {'form': form})

@login_required
def step1_A3(request):
     initial={'A3_C1' :request.session.get('A3_C1', None)}
     if request.method == 'POST':
          form = POSTFormA3_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "A3_C1"]= form.cleaned_data["A3_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_A3')
     else:
          form = POSTFormA3_C1()
     return render(request, 'questions/poleA/step1_A3.html', {'form': form})

@login_required
def step2_A3(request):
     if request.method == 'POST':
          form = POSTFormA3_C2(request.POST or None)
          if form.is_valid():
               request.session[ "A3_C2"]= form.cleaned_data[ "A3_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_A3')
     else:
          form = POSTFormA3_C2()
     return render(request, 'questions/poleA/step2_A3.html', {'form': form})

@login_required
def step3_A3(request):
     if request.method == 'POST':
          form = POSTFormA3_C3(request.POST)
          if form.is_valid():
               request.session[ "A3_C3"]= form.cleaned_data[ "A3_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedA3')
     else:
          form = POSTFormA3_C3()
     return render(request, 'questions/poleA/step3_A3.html', {'form': form})
@login_required
def step1_A4(request):
     initial={'A4_C1' :request.session.get('A4_C1', None)}
     if request.method == 'POST':
          form = POSTFormA4_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "A4_C1"]= form.cleaned_data["A4_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_A4')
     else:
          form = POSTFormA4_C1()
     return render(request, 'questions/poleA/step1_A4.html', {'form': form})

@login_required
def step2_A4(request):
     if request.method == 'POST':
          form = POSTFormA4_C2(request.POST or None)
          if form.is_valid():
               request.session[ "A4_C2"]= form.cleaned_data[ "A4_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_A4')
     else:
          form = POSTFormA4_C2()
     return render(request, 'questions/poleA/step2_A4.html', {'form': form})

@login_required
def step3_A4(request):
     if request.method == 'POST':
          form = POSTFormA4_C3(request.POST)
          if form.is_valid():
               request.session[ "A4_C3"]= form.cleaned_data[ "A4_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedA4')
     else:
          form = POSTFormA4_C3()
     return render(request, 'questions/poleA/step3_A4.html', {'form': form})

@login_required
def step1_A5(request):
     initial={'A5_C1' :request.session.get('A5_C1', None)}
     if request.method == 'POST':
          form = POSTFormA5_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "A5_C1"]= form.cleaned_data["A5_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_A5')
     else:
          form = POSTFormA5_C1()
     return render(request, 'questions/poleA/step1_A5.html', {'form': form})

@login_required
def step2_A5(request):
     if request.method == 'POST':
          form = POSTFormA5_C2(request.POST or None)
          if form.is_valid():
               request.session[ "A5_C2"]= form.cleaned_data[ "A5_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_A5')
     else:
          form = POSTFormA5_C2()
     return render(request, 'questions/poleA/step2_A5.html', {'form': form})

@login_required
def step3_A5(request):
     if request.method == 'POST':
          form = POSTFormA5_C3(request.POST)
          if form.is_valid():
               request.session[ "A5_C3"]= form.cleaned_data[ "A5_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedA5')
     else:
          form = POSTFormA5_C3()
     return render(request, 'questions/poleA/step3_A5.html', {'form': form})

@login_required
def step1_A6(request):
     initial={'A6_C1' :request.session.get('A6_C1', None)}
     if request.method == 'POST':
          form = POSTFormA6_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "A6_C1"]= form.cleaned_data["A6_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_A6')
     else:
          form = POSTFormA6_C1()
     return render(request, 'questions/poleA/step1_A6.html', {'form': form})

@login_required
def step2_A6(request):
     if request.method == 'POST':
          form = POSTFormA6_C2(request.POST or None)
          if form.is_valid():
               request.session[ "A6_C2"]= form.cleaned_data[ "A6_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_A6')
     else:
          form = POSTFormA6_C2()
     return render(request, 'questions/poleA/step2_A6.html', {'form': form})

@login_required
def step3_A6(request):
     if request.method == 'POST':
          form = POSTFormA6_C3(request.POST)
          if form.is_valid():
               request.session[ "A6_C3"]= form.cleaned_data[ "A6_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedA6')
     else:
          form = POSTFormA6_C3()
     return render(request, 'questions/poleA/step3_A6.html', {'form': form})

#################################################################

@login_required
def step1_B1(request):
     initial={'B1_C1' :request.session.get('B1_C1', None)}
     if request.method == 'POST':
          form = POSTFormB1_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "B1_C1"]= form.cleaned_data["B1_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_B1')
     else:
          form = POSTFormB1_C1()
     return render(request, 'questions/poleB/step1_B1.html', {'form': form})

@login_required
def step2_B1(request):
     if request.method == 'POST':
          form = POSTFormB1_C2(request.POST or None)
          if form.is_valid():
               request.session[ "B1_C2"]= form.cleaned_data[ "B1_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_B1')
     else:
          form = POSTFormB1_C2()
     return render(request, 'questions/poleB/step2_B1.html', {'form': form})

@login_required
def step3_B1(request):
     if request.method == 'POST':
          form = POSTFormB1_C3(request.POST)
          if form.is_valid():
               request.session[ "B1_C3"]= form.cleaned_data[ "B1_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedB1')
     else:
          form = POSTFormB1_C3()
     return render(request, 'questions/poleB/step3_B1.html', {'form': form})


def step1_B2(request):
     initial={'B2_C1' :request.session.get('B2_C1', None)}
     if request.method == 'POST':
          form = POSTFormB2_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "B2_C1"]= form.cleaned_data["B2_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_B2')
     else:
          form = POSTFormB2_C1()
     return render(request, 'questions/poleB/step1_B2.html', {'form': form})

@login_required
def step2_B2(request):
     if request.method == 'POST':
          form = POSTFormB2_C2(request.POST or None)
          if form.is_valid():
               request.session[ "B2_C2"]= form.cleaned_data[ "B2_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_B2')
     else:
          form = POSTFormB2_C2()
     return render(request, 'questions/poleB/step2_B2.html', {'form': form})

@login_required
def step3_B2(request):
     if request.method == 'POST':
          form = POSTFormB2_C3(request.POST)
          if form.is_valid():
               request.session[ "B2_C3"]= form.cleaned_data[ "B2_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedB2')
     else:
          form = POSTFormB2_C3()
     return render(request, 'questions/poleB/step3_B2.html', {'form': form})



def step1_B3(request):
     initial={'B3_C1' :request.session.get('B3_C1', None)}
     if request.method == 'POST':
          form = POSTFormB3_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "B3_C1"]= form.cleaned_data["B3_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_B3')
     else:
          form = POSTFormB3_C1()
     return render(request, 'questions/poleB/step1_B3.html', {'form': form})

@login_required
def step2_B3(request):
     if request.method == 'POST':
          form = POSTFormB3_C2(request.POST or None)
          if form.is_valid():
               request.session[ "B3_C2"]= form.cleaned_data[ "B3_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_B3')
     else:
          form = POSTFormB3_C2()
     return render(request, 'questions/poleB/step2_B3.html', {'form': form})

@login_required
def step3_B3(request):
     if request.method == 'POST':
          form = POSTFormB3_C3(request.POST)
          if form.is_valid():
               request.session[ "B3_C3"]= form.cleaned_data[ "B3_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedB3')
     else:
          form = POSTFormB3_C3()
     return render(request, 'questions/poleB/step3_B3.html', {'form': form})


def step1_B4(request):
     initial={'B4_C1' :request.session.get('B4_C1', None)}
     if request.method == 'POST':
          form = POSTFormB4_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "B4_C1"]= form.cleaned_data["B4_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_B4')
     else:
          form = POSTFormB4_C1()
     return render(request, 'questions/poleB/step1_B4.html', {'form': form})

@login_required
def step2_B4(request):
     if request.method == 'POST':
          form = POSTFormB4_C2(request.POST or None)
          if form.is_valid():
               request.session[ "B4_C2"]= form.cleaned_data[ "B4_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_B4')
     else:
          form = POSTFormB4_C2()
     return render(request, 'questions/poleB/step2_B4.html', {'form': form})

@login_required
def step3_B4(request):
     if request.method == 'POST':
          form = POSTFormB4_C3(request.POST)
          if form.is_valid():
               request.session[ "B4_C3"]= form.cleaned_data[ "B4_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedB4')
     else:
          form = POSTFormB4_C3()
     return render(request, 'questions/poleB/step3_B4.html', {'form': form})
###########################################################

@login_required
def step1_C1(request):
     initial={'C1_C1' :request.session.get('C1_C1', None)}
     if request.method == 'POST':
          form = POSTFormC1_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "C1_C1"]= form.cleaned_data["C1_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_C1')
     else:
          form = POSTFormC1_C1()
     return render(request, 'questions/poleC/step1_C1.html', {'form': form})

@login_required
def step2_C1(request):
     if request.method == 'POST':
          form = POSTFormC1_C2(request.POST or None)
          if form.is_valid():
               request.session[ "C1_C2"]= form.cleaned_data[ "C1_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_C1')
     else:
          form = POSTFormC1_C2()
     return render(request, 'questions/poleC/step2_C1.html', {'form': form})

@login_required
def step3_C1(request):
     if request.method == 'POST':
          form = POSTFormC1_C3(request.POST)
          if form.is_valid():
               request.session[ "C1_C3"]= form.cleaned_data[ "C1_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedC1')
     else:
          form = POSTFormC1_C3()
     return render(request, 'questions/poleC/step3_C1.html', {'form': form})


def step1_C2(request):
     initial={'C2_C1' :request.session.get('C2_C1', None)}
     if request.method == 'POST':
          form = POSTFormC2_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "C2_C1"]= form.cleaned_data["C2_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_C2')
     else:
          form = POSTFormC2_C1()
     return render(request, 'questions/poleC/step1_C2.html', {'form': form})

@login_required
def step2_C2(request):
     if request.method == 'POST':
          form = POSTFormC2_C2(request.POST or None)
          if form.is_valid():
               request.session[ "C2_C2"]= form.cleaned_data[ "C2_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_C2')
     else:
          form = POSTFormC2_C2()
     return render(request, 'questions/poleC/step2_C2.html', {'form': form})

@login_required
def step3_C2(request):
     if request.method == 'POST':
          form = POSTFormC2_C3(request.POST)
          if form.is_valid():
               request.session[ "C2_C3"]= form.cleaned_data[ "C2_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedC2')
     else:
          form = POSTFormC2_C3()
     return render(request, 'questions/poleC/step3_C2.html', {'form': form})



def step1_C3(request):
     initial={'C3_C1' :request.session.get('C3_C1', None)}
     if request.method == 'POST':
          form = POSTFormC3_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "C3_C1"]= form.cleaned_data["C3_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_C3')
     else:
          form = POSTFormC3_C1()
     return render(request, 'questions/poleC/step1_C3.html', {'form': form})

@login_required
def step2_C3(request):
     if request.method == 'POST':
          form = POSTFormC3_C2(request.POST or None)
          if form.is_valid():
               request.session[ "C3_C2"]= form.cleaned_data[ "C3_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_C3')
     else:
          form = POSTFormC3_C2()
     return render(request, 'questions/poleC/step2_C3.html', {'form': form})

@login_required
def step3_C3(request):
     if request.method == 'POST':
          form = POSTFormC3_C3(request.POST)
          if form.is_valid():
               request.session[ "C3_C3"]= form.cleaned_data[ "C3_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedC3')
     else:
          form = POSTFormC3_C3()
     return render(request, 'questions/poleC/step3_C3.html', {'form': form})


def step1_C4(request):
     initial={'C4_C1' :request.session.get('C4_C1', None)}
     if request.method == 'POST':
          form = POSTFormC4_C1(request.POST or None, initial=initial)
          if form.is_valid():
               request.session[ "C4_C1"]= form.cleaned_data["C4_C1"]
               post = form.save(commit=False)
               post.save()
               return redirect('step2_C4')
     else:
          form = POSTFormC4_C1()
     return render(request, 'questions/poleC/step1_C4.html', {'form': form})

@login_required
def step2_C4(request):
     if request.method == 'POST':
          form = POSTFormC4_C2(request.POST or None)
          if form.is_valid():
               request.session[ "C4_C2"]= form.cleaned_data[ "C4_C2"]
               post = form.save(commit=False)
               post.save()
               return redirect('step3_C4')
     else:
          form = POSTFormC4_C2()
     return render(request, 'questions/poleC/step2_C4.html', {'form': form})

@login_required
def step3_C4(request):
     if request.method == 'POST':
          form = POSTFormC4_C3(request.POST)
          if form.is_valid():
               request.session[ "C4_C3"]= form.cleaned_data[ "C4_C3"]
               post = form.save(commit=False)
               post.save()
               return redirect('finishedC4')
     else:
          form = POSTFormC4_C3()
     return render(request, 'questions/poleC/step3_C4.html', {'form': form})








###########################################################
@login_required
def resultatsA(request):
     user_connected=request.user.id
     if PostA1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA1_C3.objects.filter(created_by_id=user_connected).all().exists() and PostA2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA2_C3.objects.filter(created_by_id=user_connected).all().exists() \
          and PostA3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA3_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostA4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA4_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostA4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA5_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA5_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostA6_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA6_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA6_C3.objects.filter(created_by_id=user_connected).all().exists():

          resA1_C1 = pd.DataFrame(list(PostA1_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A1_C1').order_by('id').reverse()[:1]))
          resA1_C2 = pd.DataFrame(list(PostA1_C2.objects.filter(created_by_id=user_connected).values('A1_C2').order_by('id').reverse()[:1]))
          resA1_C3 = pd.DataFrame(list(PostA1_C3.objects.filter(created_by_id=user_connected).values('A1_C3', 'time').order_by('id').reverse()[:1]))
          resA1_C3['time'] = resA1_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
          resultsA1 = pd.merge(resA1_C1, resA1_C2, how='cross')
          resultsA1 = pd.merge(resultsA1, resA1_C3, how='cross')
          df_result_A1=resultsA1[["A1_C1", "A1_C2", "A1_C3",]]
          df_result_A1.columns=["A1_C1", "A1_C2", "A1_C3"]
          df_result_A1 = df_result_A1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rA1=df_result_A1.iloc[0]
          fig_A1= px.line_polar(df_result_A1,r=rA1, theta=["A1_C1", "A1_C2", "A1_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360,)
          fig_A1.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A1.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))

          chart_A1 = fig_A1.to_html(config = {'displayModeBar': False})
          resultsA1 = resultsA1.to_dict(orient='records')

          resA2_C1 = pd.DataFrame(list(PostA2_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A2_C1').order_by('id').reverse()[:1]))
          resA2_C2 = pd.DataFrame(list(PostA2_C2.objects.filter(created_by_id=user_connected).values('A2_C2').order_by('id').reverse()[:1]))
          resA2_C3 = pd.DataFrame(list(PostA2_C3.objects.filter(created_by_id=user_connected).values('A2_C3', 'time').order_by('id').reverse()[:1]))
          resA2_C3['time'] = resA2_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
          resultsA2 = pd.merge(resA2_C1, resA2_C2, how='cross')
          resultsA2 = pd.merge(resultsA2, resA2_C3, how='cross')
          df_result_A2=resultsA2[["A2_C1", "A2_C2", "A2_C3",]]
          df_result_A2.columns=["A2_C1", "A2_C2", "A2_C3"]
          df_result_A2 = df_result_A2.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rA2=df_result_A2.iloc[0]
          fig_A2= px.line_polar(df_result_A2,r=rA2, theta=["A2_C1", "A2_C2", "A2_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360)
          fig_A2.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A2.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))

          chart_A2 = fig_A2.to_html(config = {'displayModeBar': False})
          resultsA2 = resultsA2.to_dict(orient='records')

          resA3_C1 = pd.DataFrame(list(PostA3_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A3_C1').order_by('id').reverse()[:1]))
          resA3_C2 = pd.DataFrame(list(PostA3_C2.objects.filter(created_by_id=user_connected).values('A3_C2').order_by('id').reverse()[:1]))
          resA3_C3 = pd.DataFrame(list(PostA3_C3.objects.filter(created_by_id=user_connected).values('A3_C3','time').order_by('id').reverse()[:1]))
          resA3_C3['time'] = resA3_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
          resultsA3 = pd.merge(resA3_C1, resA3_C2, how='cross')
          resultsA3 = pd.merge(resultsA3, resA3_C3, how='cross')
          df_result_A3=resultsA3[["A3_C1", "A3_C2", "A3_C3",]]
          df_result_A3.columns=["A3_C1", "A3_C2", "A3_C3"]
          df_result_A3 = df_result_A3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rA3=df_result_A3.iloc[0]
          fig_A3= px.line_polar(df_result_A3,r=rA3, theta=["A3_C1", "A3_C2", "A3_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360)
          fig_A3.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A3.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))

          chart_A3 = fig_A3.to_html(config = {'displayModeBar': False})
          resultsA3 = resultsA3.to_dict(orient='records')




          resA4_C1 = pd.DataFrame(list(PostA4_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A4_C1').order_by('id').reverse()[:1]))
          resA4_C2 = pd.DataFrame(list(PostA4_C2.objects.filter(created_by_id=user_connected).values('A4_C2').order_by('id').reverse()[:1]))
          resA4_C3 = pd.DataFrame(list(PostA4_C3.objects.filter(created_by_id=user_connected).values('A4_C3', 'time').order_by('id').reverse()[:1]))
          resA4_C3['time'] = resA4_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
          resultsA4 = pd.merge(resA4_C1, resA4_C2, how='cross')
          resultsA4 = pd.merge(resultsA4, resA4_C3, how='cross')
          df_result_A4=resultsA4[["A4_C1", "A4_C2", "A4_C3",]]
          df_result_A4.columns=["A4_C1", "A4_C2", "A4_C3"]
          df_result_A4 = df_result_A4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rA4=df_result_A4.iloc[0]
          fig_A4= px.line_polar(df_result_A4,r=rA4, theta=["A4_C1", "A4_C2", "A4_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360)
          fig_A4.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A4.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))

          chart_A4 = fig_A4.to_html(config = {'displayModeBar': False})
          resultsA4 = resultsA4.to_dict(orient='records')

          resA5_C1 = pd.DataFrame(list(PostA5_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A5_C1').order_by('id').reverse()[:1]))
          resA5_C2 = pd.DataFrame(list(PostA5_C2.objects.filter(created_by_id=user_connected).values('A5_C2').order_by('id').reverse()[:1]))
          resA5_C3 = pd.DataFrame(list(PostA5_C3.objects.filter(created_by_id=user_connected).values('A5_C3', 'time').order_by('id').reverse()[:1]))
          resA5_C3['time'] = resA5_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
          resultsA5 = pd.merge(resA5_C1, resA5_C2, how='cross')
          resultsA5 = pd.merge(resultsA5, resA5_C3, how='cross')
          df_result_A5=resultsA5[["A5_C1", "A5_C2", "A5_C3",]]
          df_result_A5.columns=["A5_C1", "A5_C2", "A5_C3"]
          df_result_A5 = df_result_A5.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rA5=df_result_A5.iloc[0]
          fig_A5= px.line_polar(df_result_A5,r=rA5, theta=["A5_C1", "A5_C2", "A5_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360)
          fig_A5.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A5.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))

          chart_A5 = fig_A5.to_html(config = {'displayModeBar': False})
          resultsA5 = resultsA5.to_dict(orient='records')

          resA6_C1 = pd.DataFrame(list(PostA6_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A6_C1').order_by('id').reverse()[:1]))
          resA6_C2 = pd.DataFrame(list(PostA6_C2.objects.filter(created_by_id=user_connected).values('A6_C2').order_by('id').reverse()[:1]))
          resA6_C3 = pd.DataFrame(list(PostA6_C3.objects.filter(created_by_id=user_connected).values('A6_C3', 'time').order_by('id').reverse()[:1]))
          resA6_C3['time'] = resA6_C3['time'].dt.strftime('%d/%m/%Y %H:%M:%S')
          resultsA6 = pd.merge(resA6_C1, resA6_C2, how='cross')
          resultsA6 = pd.merge(resultsA6, resA6_C3, how='cross')
          df_result_A6=resultsA6[["A6_C1", "A6_C2", "A6_C3",]]
          df_result_A6.columns=["A6_C1", "A6_C2", "A6_C3"]
          df_result_A6 = df_result_A6.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rA6=df_result_A6.iloc[0]
          fig_A6= px.line_polar(df_result_A6,r=rA6, theta=["A6_C1", "A6_C2", "A6_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360)
          fig_A6.update_traces(fill='toself')

          rA6=df_result_A6.iloc[0]
          fig_A6= px.line_polar(df_result_A6,r=rA6, theta=["A6_C1", "A6_C2", "A6_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360)
          fig_A6.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A6.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))

          chart_A6 = fig_A6.to_html(config = {'displayModeBar': False})
          resultsA6 = resultsA6.to_dict(orient='records')

          resultallA=pd.concat([df_result_A1, df_result_A2, df_result_A3, df_result_A4, df_result_A5, df_result_A6], axis=1)
          df_result_all = resultallA.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r_all=df_result_all.iloc[0]

          fig_all= px.line_polar(df_result_all,r=r_all,theta=["A1_C1", "A1_C2", "A1_C3","A2_C1", "A2_C2", "A2_C3","A3_C1", "A3_C2", "A3_C3","A4_C1", "A4_C2", "A4_C3","A5_C1", "A5_C2", "A5_C3","A6_C1", "A6_C2", "A6_C3"], direction='clockwise', start_angle=70, line_close=True, color_discrete_sequence=["#000091","#9898f8", "#e3e3fd"],line_shape='spline', width=420, height=420)
          fig_all.update_traces(fill='toself')
          fig_all.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))

          chart_all = fig_all.to_html(config = {'displayModeBar': False})


          A2 = go.Scatterpolar(
              r = df_result_all[["A2_C1", "A2_C2", "A2_C3",]].iloc[0], theta = ["A2_C1", "A2_C2", "A2_C3",], mode = 'lines',   name = 'A2')
          A1 = go.Scatterpolar(
               r =df_result_all[["A1_C1", "A1_C2", "A1_C3",]].iloc[0], theta = ["A1_C1", "A1_C2", "A1_C3",], mode = 'lines', name = 'A1')
          A3 = go.Scatterpolar(
               r = df_result_all[["A3_C1", "A3_C2", "A3_C3",]].iloc[0], theta = ["A3_C1", "A3_C2", "A3_C3",], mode = 'lines',  name = 'A3')
          A4 = go.Scatterpolar(
               r =df_result_all[["A4_C1", "A4_C2", "A4_C3",]].iloc[0], theta = ["A4_C1", "A4_C2", "A4_C3",], mode = 'lines', name = 'A4')
          A5 = go.Scatterpolar(
               r =df_result_all[["A5_C1", "A5_C2", "A5_C3",]].iloc[0], theta = ["A5_C1", "A5_C2", "A5_C3",], mode = 'lines', name = 'A5')
          A6 = go.Scatterpolar(
               r =df_result_all[["A6_C1", "A6_C2", "A6_C3",]].iloc[0], theta = ["A6_C1", "A6_C2", "A6_C3",], mode = 'lines', name = 'A6')
          data = [A1,A2,A3,A4,A5,A6]
          fig = go.Figure(data = data)
          fig.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))
          chart_all2 = fig.to_html(config = {'responsive': True,'displayModeBar': False})



          return render(request, 'questions/poleA/resultsA.html', { 'resultsA1' : resultsA1, 'chart_A1' : chart_A1, 'resultsA2' : resultsA2, 'chart_A2' : chart_A2, 'resultsA3' : resultsA3, 'chart_A3' : chart_A3,
                                                              'resultsA4' : resultsA4, 'chart_A4' : chart_A4, 'resultsA5' : resultsA5, 'chart_A5' : chart_A5, 'resultsA6' : resultsA6, 'chart_A6' : chart_A6, 'chart_all' : chart_all, 'chart_all2' : chart_all2,})

     else :
          info = "Les résultats seront disponible après avoir remplie la section A"
          return render(request, 'questions/poleA/resultsA.html', {'info' : info})

@login_required
def resultatsB(request):
    user_connected=request.user.id
    if PostB1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB1_C3.objects.filter(created_by_id=user_connected).all().exists() and PostB2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB2_C3.objects.filter(created_by_id=user_connected).all().exists() \
    and PostB3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB3_C3.objects.filter(created_by_id=user_connected).all().exists() and \
    PostB4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB4_C3.objects.filter(created_by_id=user_connected).all().exists():
        resB1_C1 = pd.DataFrame(list(PostB1_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'B1_C1').order_by('id').reverse()[:1]))
        resB1_C2 = pd.DataFrame(list(PostB1_C2.objects.filter(created_by_id=user_connected).values('B1_C2').order_by('id').reverse()[:1]))
        resB1_C3 = pd.DataFrame(list(PostB1_C3.objects.filter(created_by_id=user_connected).values('B1_C3', 'time').order_by('id').reverse()[:1]))
        resB1_C3['time'] = resB1_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
        resultsB1 = pd.merge(resB1_C1, resB1_C2, how='cross')
        resultsB1 = pd.merge(resultsB1, resB1_C3, how='cross')
        df_result_B1=resultsB1[["B1_C1", "B1_C2", "B1_C3",]]
        df_result_B1.columns=["B1_C1", "B1_C2", "B1_C3"]
        df_result_B1 = df_result_B1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
        rB1=df_result_B1.iloc[0]
        fig_B1= px.line_polar(df_result_B1,r=rB1, theta=["B1_C1", "B1_C2", "B1_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360, color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"],)
        fig_B1.update_traces(fill='toself')
        value=[1,2,3,4,]
        max_value = max(value)
        fixed_axis_values = np.linspace(0, max_value, 5)
        fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
        fig_B1.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))
        chart_B1 = fig_B1.to_html(config = {'displayModeBar': False})
        resultsB1 = resultsB1.to_dict(orient='records')

        resB2_C1 = pd.DataFrame(list(PostB2_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'B2_C1').order_by('id').reverse()[:1]))
        resB2_C2 = pd.DataFrame(list(PostB2_C2.objects.filter(created_by_id=user_connected).values('B2_C2').order_by('id').reverse()[:1]))
        resB2_C3 = pd.DataFrame(list(PostB2_C3.objects.filter(created_by_id=user_connected).values('B2_C3', 'time').order_by('id').reverse()[:1]))
        resB2_C3['time'] = resB2_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
        resultsB2 = pd.merge(resB2_C1, resB2_C2, how='cross')
        resultsB2 = pd.merge(resultsB2, resB2_C3, how='cross')
        df_result_B2=resultsB2[["B2_C1", "B2_C2", "B2_C3",]]
        df_result_B2.columns=["B2_C1", "B2_C2", "B2_C3"]
        df_result_B2 = df_result_B2.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

        rB2=df_result_B2.iloc[0]
        fig_B2= px.line_polar(df_result_B2,r=rB2, theta=["B2_C1", "B2_C2", "B2_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360, color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"],)
        fig_B2.update_traces(fill='toself')
        value=[1,2,3,4,]
        max_value = max(value)
        fixed_axis_values = np.linspace(0, max_value, 5)
        fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
        fig_B2.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))
        chart_B2 = fig_B2.to_html(config = {'displayModeBar': False})
        resultsB2 = resultsB2.to_dict(orient='records')

        resB3_C1 = pd.DataFrame(list(PostB3_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'B3_C1').order_by('id').reverse()[:1]))
        resB3_C2 = pd.DataFrame(list(PostB3_C2.objects.filter(created_by_id=user_connected).values('B3_C2').order_by('id').reverse()[:1]))
        resB3_C3 = pd.DataFrame(list(PostB3_C3.objects.filter(created_by_id=user_connected).values('B3_C3','time').order_by('id').reverse()[:1]))
        resB3_C3['time'] = resB3_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
        resultsB3 = pd.merge(resB3_C1, resB3_C2, how='cross')
        resultsB3 = pd.merge(resultsB3, resB3_C3, how='cross')
        df_result_B3=resultsB3[["B3_C1", "B3_C2", "B3_C3",]]
        df_result_B3.columns=["B3_C1", "B3_C2", "B3_C3"]
        df_result_B3 = df_result_B3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

        rB3=df_result_B3.iloc[0]
        fig_B3= px.line_polar(df_result_B3,r=rB3, theta=["B3_C1", "B3_C2", "B3_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360, color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"])
        fig_B3.update_traces(fill='toself')
        value=[1,2,3,4,]
        max_value = max(value)
        fixed_axis_values = np.linspace(0, max_value, 5)
        fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
        fig_B3.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))
        chart_B3 = fig_B3.to_html(config = {'displayModeBar': False})
        resultsB3 = resultsB3.to_dict(orient='records')

        resB4_C1 = pd.DataFrame(list(PostB4_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'B4_C1').order_by('id').reverse()[:1]))
        resB4_C2 = pd.DataFrame(list(PostB4_C2.objects.filter(created_by_id=user_connected).values('B4_C2').order_by('id').reverse()[:1]))
        resB4_C3 = pd.DataFrame(list(PostB4_C3.objects.filter(created_by_id=user_connected).values('B4_C3', 'time').order_by('id').reverse()[:1]))
        resB4_C3['time'] = resB4_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
        resultsB4 = pd.merge(resB4_C1, resB4_C2, how='cross')
        resultsB4 = pd.merge(resultsB4, resB4_C3, how='cross')
        df_result_B4=resultsB4[["B4_C1", "B4_C2", "B4_C3",]]
        df_result_B4.columns=["B4_C1", "B4_C2", "B4_C3"]
        df_result_B4 = df_result_B4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

        rB4=df_result_B4.iloc[0]
        fig_B4= px.line_polar(df_result_B4,r=rB4, theta=["B4_C1", "B4_C2", "B4_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360, color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"],)
        fig_B4.update_traces(fill='toself')
        value=[1,2,3,4,]
        max_value = max(value)
        fixed_axis_values = np.linspace(0, max_value, 5)
        fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
        fig_B4.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))
        chart_B4 = fig_B4.to_html(config = {'displayModeBar': False})
        resultsB4 = resultsB4.to_dict(orient='records')

        resultallB=pd.concat([df_result_B1, df_result_B2, df_result_B3, df_result_B4], axis=1)
        df_result_all = resultallB.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
        r_all=df_result_all.iloc[0]

        fig_all= px.line_polar(df_result_all,r=r_all,theta=["B1_C1", "B1_C2", "B1_C3","B2_C1", "B2_C2", "B2_C3","B3_C1", "B3_C2", "B3_C3","B4_C1", "B4_C2", "B4_C3"], direction='clockwise', start_angle=70, line_close=True, line_shape='spline', width=420, height=420, color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"],)
        fig_all.update_traces(fill='toself')
        value=[1,2,3,4,]
        max_value = max(value)
        fixed_axis_values = np.linspace(0, max_value, 5)
        fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
        fig_all.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))
        chart_all = fig_all.to_html()

        B1 = go.Scatterpolar(
            r = df_result_all[["B2_C1", "B2_C2", "B2_C3",]].iloc[0], theta = ["B2_C1", "B2_C2", "B2_C3",], mode = 'lines',   name = 'B1')
        B2 = go.Scatterpolar(
            r =df_result_all[["B1_C1", "B1_C2", "B1_C3",]].iloc[0], theta = ["B1_C1", "B1_C2", "B1_C3",], mode = 'lines', name = 'B2')
        B3 = go.Scatterpolar(
            r = df_result_all[["B3_C1", "B3_C2", "B3_C3",]].iloc[0], theta = ["B3_C1", "B3_C2", "B3_C3",], mode = 'lines',  name = 'B3')
        B4 = go.Scatterpolar(
            r =df_result_all[["B4_C1", "B4_C2", "B4_C3",]].iloc[0], theta = ["B4_C1", "B4_C2", "B4_C3",], mode = 'lines', name = 'B4')
        data = [B1,B2,B3,B4]
        fig = go.Figure(data = data, )
        value=[1,2,3,4,]
        max_value = max(value)
        fixed_axis_values = np.linspace(0, max_value, 5)
        fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
        fig.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))
        chart_all2 = fig.to_html()

        return render(request, 'questions/poleB/resultsB.html', { 'resultsB1' : resultsB1, 'chart_B1' : chart_B1, 'resultsB2' : resultsB2,'chart_B2' : chart_B2,
        'resultsB3' : resultsB3,'chart_B3' : chart_B3, 'resultsB4' : resultsB4,'chart_B4' : chart_B4,'chart_all' : chart_all, 'chart_all2' : chart_all2})

    else :
        info = "Les résultats seront disponible après avoir remplie la section B"
        return render(request, 'questions/poleB/resultsB.html', {'info' : info})


@login_required
def resultatsC(request):
    user_connected=request.user.id
    if PostC1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC1_C3.objects.filter(created_by_id=user_connected).all().exists() and PostC2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC2_C3.objects.filter(created_by_id=user_connected).all().exists() \
    and PostC3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC3_C3.objects.filter(created_by_id=user_connected).all().exists() and \
    PostC4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC4_C3.objects.filter(created_by_id=user_connected).all().exists():
        resC1_C1 = pd.DataFrame(list(PostC1_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'C1_C1').order_by('id').reverse()[:1]))
        resC1_C2 = pd.DataFrame(list(PostC1_C2.objects.filter(created_by_id=user_connected).values('C1_C2').order_by('id').reverse()[:1]))
        resC1_C3 = pd.DataFrame(list(PostC1_C3.objects.filter(created_by_id=user_connected).values('C1_C3', 'time').order_by('id').reverse()[:1]))
        resC1_C3['time'] = resC1_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
        resultsC1 = pd.merge(resC1_C1, resC1_C2, how='cross')
        resultsC1 = pd.merge(resultsC1, resC1_C3, how='cross')
        df_result_C1=resultsC1[["C1_C1", "C1_C2", "C1_C3",]]
        df_result_C1.columns=["C1_C1", "C1_C2", "C1_C3"]
        df_result_C1 = df_result_C1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
        rC1=df_result_C1.iloc[0]
        fig_C1= px.line_polar(df_result_C1,r=rC1, theta=["C1_C1", "C1_C2", "C1_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360, color_discrete_sequence=["green", "blue", "goldenrod", "magenta"],)
        fig_C1.update_traces(fill='toself')
        value=[1,2,3,4,]
        max_value = max(value)
        fixed_axis_values = np.linspace(0, max_value, 5)
        fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
        fig_C1.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))
        chart_C1 = fig_C1.to_html(config = {'displayModeBar': False})
        resultsC1 = resultsC1.to_dict(orient='records')

        resC2_C1 = pd.DataFrame(list(PostC2_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'C2_C1').order_by('id').reverse()[:1]))
        resC2_C2 = pd.DataFrame(list(PostC2_C2.objects.filter(created_by_id=user_connected).values('C2_C2').order_by('id').reverse()[:1]))
        resC2_C3 = pd.DataFrame(list(PostC2_C3.objects.filter(created_by_id=user_connected).values('C2_C3', 'time').order_by('id').reverse()[:1]))
        resC2_C3['time'] = resC2_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
        resultsC2 = pd.merge(resC2_C1, resC2_C2, how='cross')
        resultsC2 = pd.merge(resultsC2, resC2_C3, how='cross')
        df_result_C2=resultsC2[["C2_C1", "C2_C2", "C2_C3",]]
        df_result_C2.columns=["C2_C1", "C2_C2", "C2_C3"]
        df_result_C2 = df_result_C2.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

        rC2=df_result_C2.iloc[0]
        fig_C2= px.line_polar(df_result_C2,r=rC2, theta=["C2_C1", "C2_C2", "C2_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360, color_discrete_sequence=["green", "blue", "goldenrod", "magenta"],)
        fig_C2.update_traces(fill='toself')
        value=[1,2,3,4,]
        max_value = max(value)
        fixed_axis_values = np.linspace(0, max_value, 5)
        fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
        fig_C2.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))
        chart_C2 = fig_C2.to_html(config = {'displayModeBar': False})
        resultsC2 = resultsC2.to_dict(orient='records')

        resC3_C1 = pd.DataFrame(list(PostC3_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'C3_C1').order_by('id').reverse()[:1]))
        resC3_C2 = pd.DataFrame(list(PostC3_C2.objects.filter(created_by_id=user_connected).values('C3_C2').order_by('id').reverse()[:1]))
        resC3_C3 = pd.DataFrame(list(PostC3_C3.objects.filter(created_by_id=user_connected).values('C3_C3','time').order_by('id').reverse()[:1]))
        resC3_C3['time'] = resC3_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
        resultsC3 = pd.merge(resC3_C1, resC3_C2, how='cross')
        resultsC3 = pd.merge(resultsC3, resC3_C3, how='cross')
        df_result_C3=resultsC3[["C3_C1", "C3_C2", "C3_C3",]]
        df_result_C3.columns=["C3_C1", "C3_C2", "C3_C3"]
        df_result_C3 = df_result_C3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

        rC3=df_result_C3.iloc[0]
        fig_C3= px.line_polar(df_result_C3,r=rC3, theta=["C3_C1", "C3_C2", "C3_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360, color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
        fig_C3.update_traces(fill='toself')
        value=[1,2,3,4,]
        max_value = max(value)
        fixed_axis_values = np.linspace(0, max_value, 5)
        fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
        fig_C3.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))
        chart_C3 = fig_C3.to_html(config = {'displayModeBar': False})
        resultsC3 = resultsC3.to_dict(orient='records')

        resC4_C1 = pd.DataFrame(list(PostC4_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'C4_C1').order_by('id').reverse()[:1]))
        resC4_C2 = pd.DataFrame(list(PostC4_C2.objects.filter(created_by_id=user_connected).values('C4_C2').order_by('id').reverse()[:1]))
        resC4_C3 = pd.DataFrame(list(PostC4_C3.objects.filter(created_by_id=user_connected).values('C4_C3', 'time').order_by('id').reverse()[:1]))
        resC4_C3['time'] = resC4_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
        resultsC4 = pd.merge(resC4_C1, resC4_C2, how='cross')
        resultsC4 = pd.merge(resultsC4, resC4_C3, how='cross')
        df_result_C4=resultsC4[["C4_C1", "C4_C2", "C4_C3",]]
        df_result_C4.columns=["C4_C1", "C4_C2", "C4_C3"]
        df_result_C4 = df_result_C4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

        rC4=df_result_C4.iloc[0]
        fig_C4= px.line_polar(df_result_C4,r=rC4, theta=["C4_C1", "C4_C2", "C4_C3"], direction='clockwise', start_angle=70, line_close=True, width=360, height=360, color_discrete_sequence=["green", "blue", "goldenrod", "magenta"],)
        fig_C4.update_traces(fill='toself')
        value=[1,2,3,4,]
        max_value = max(value)
        fixed_axis_values = np.linspace(0, max_value, 5)
        fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
        fig_C4.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))
        chart_C4 = fig_C4.to_html(config = {'displayModeBar': False})
        resultsC4 = resultsC4.to_dict(orient='records')

        resultallC=pd.concat([df_result_C1, df_result_C2, df_result_C3, df_result_C4], axis=1)
        df_result_all = resultallC.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
        r_all=df_result_all.iloc[0]

        fig_all= px.line_polar(df_result_all,r=r_all,theta=["C1_C1", "C1_C2", "C1_C3","C2_C1", "C2_C2", "C2_C3","C3_C1", "C3_C2", "C3_C3","C4_C1", "C4_C2", "C4_C3"], direction='clockwise', start_angle=70, line_close=True, line_shape='spline', width=420, height=420, color_discrete_sequence=["green", "blue", "goldenrod", "magenta"],)
        fig_all.update_traces(fill='toself')
        value=[1,2,3,4,]
        max_value = max(value)
        fixed_axis_values = np.linspace(0, max_value, 5)
        fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
        fig_all.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))
        chart_all = fig_all.to_html(config = {'displayModeBar': False})

        C1 = go.Scatterpolar(
            r = df_result_all[["C2_C1", "C2_C2", "C2_C3",]].iloc[0], theta = ["C2_C1", "C2_C2", "C2_C3",], mode = 'lines',   name = 'C1')
        C2 = go.Scatterpolar(
            r =df_result_all[["C1_C1", "C1_C2", "C1_C3",]].iloc[0], theta = ["C1_C1", "C1_C2", "C1_C3",], mode = 'lines', name = 'C2')
        C3 = go.Scatterpolar(
            r = df_result_all[["C3_C1", "C3_C2", "C3_C3",]].iloc[0], theta = ["C3_C1", "C3_C2", "C3_C3",], mode = 'lines',  name = 'C3')
        C4 = go.Scatterpolar(
            r =df_result_all[["C4_C1", "C4_C2", "C4_C3",]].iloc[0], theta = ["C4_C1", "C4_C2", "C4_C3",], mode = 'lines', name = 'C4')
        data = [C1,C2,C3,C4]
        fig = go.Figure(data = data, )
        value=[1,2,3,4,]
        max_value = max(value)
        fixed_axis_values = np.linspace(0, max_value, 5)
        fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
        fig.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)
                         ))
        chart_all2 = fig.to_html(config = {'displayModeBar': False})

        return render(request, 'questions/poleC/resultsC.html', { 'resultsC1' : resultsC1, 'chart_C1' : chart_C1, 'resultsC2' : resultsC2,'chart_C2' : chart_C2,
        'resultsC3' : resultsC3,'chart_C3' : chart_C3, 'resultsC4' : resultsC4,'chart_C4' : chart_C4,'chart_all' : chart_all, 'chart_all2' : chart_all2})

    else :
        info = "Les résultats seront disponible après avoir remplie la section C"
        return render(request, 'questions/poleC/resultsC.html', {'info' : info})

##################################################################################

from io import BytesIO
import plotly.graph_objs as go
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.platypus import Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm



def generateB_pdf(request):
      user_connected=request.user.id
      if PostB1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB1_C3.objects.filter(created_by_id=user_connected).all().exists() and PostB2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB2_C3.objects.filter(created_by_id=user_connected).all().exists() \
          and PostB3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB3_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostB4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB4_C3.objects.filter(created_by_id=user_connected).all().exists():
          resB1_C1 = pd.DataFrame(list(PostB1_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'B1_C1').order_by('id').reverse()[:1]))
          resB1_C2 = pd.DataFrame(list(PostB1_C2.objects.filter(created_by_id=user_connected).values('B1_C2').order_by('id').reverse()[:1]))
          resB1_C3 = pd.DataFrame(list(PostB1_C3.objects.filter(created_by_id=user_connected).values('B1_C3', 'time').order_by('id').reverse()[:1]))
          resB1_C3['time'] = resB1_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsB1 = pd.merge(resB1_C1, resB1_C2, how='cross')
          resultsB1 = pd.merge(resultsB1, resB1_C3, how='cross')
          df_result_B1=resultsB1[["B1_C1", "B1_C2", "B1_C3",]]
          df_result_B1.columns=["B1_C1", "B1_C2", "B1_C3"]
          df_result_B1 = df_result_B1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])



          resB2_C1 = pd.DataFrame(list(PostB2_C1.objects.filter(created_by_id=user_connected).values('B2_C1').order_by('id').reverse()[:1]))
          resB2_C2 = pd.DataFrame(list(PostB2_C2.objects.filter(created_by_id=user_connected).values('B2_C2').order_by('id').reverse()[:1]))
          resB2_C3 = pd.DataFrame(list(PostB2_C3.objects.filter(created_by_id=user_connected).values('B2_C3', 'time').order_by('id').reverse()[:1]))
          resB2_C3['time'] = resB2_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsB2 = pd.merge(resB2_C1, resB2_C2, how='cross')
          resultsB2 = pd.merge(resultsB2, resB2_C3, how='cross')
          df_result_B2=resultsB2[["B2_C1", "B2_C2", "B2_C3",]]
          df_result_B2.columns=["B2_C1", "B2_C2", "B2_C3"]
          df_result_B2 = df_result_B2.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resB3_C1 = pd.DataFrame(list(PostB3_C1.objects.filter(created_by_id=user_connected).values('B3_C1').order_by('id').reverse()[:1]))
          resB3_C2 = pd.DataFrame(list(PostB3_C2.objects.filter(created_by_id=user_connected).values('B3_C2').order_by('id').reverse()[:1]))
          resB3_C3 = pd.DataFrame(list(PostB3_C3.objects.filter(created_by_id=user_connected).values('B3_C3','time').order_by('id').reverse()[:1]))
          resB3_C3['time'] = resB3_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsB3 = pd.merge(resB3_C1, resB3_C2, how='cross')
          resultsB3 = pd.merge(resultsB3, resB3_C3, how='cross')
          df_result_B3=resultsB3[["B3_C1", "B3_C2", "B3_C3",]]
          df_result_B3.columns=["B3_C1", "B3_C2", "B3_C3"]
          df_result_B3 = df_result_B3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resB4_C1 = pd.DataFrame(list(PostB4_C1.objects.filter(created_by_id=user_connected).values('B4_C1').order_by('id').reverse()[:1]))
          resB4_C2 = pd.DataFrame(list(PostB4_C2.objects.filter(created_by_id=user_connected).values('B4_C2').order_by('id').reverse()[:1]))
          resB4_C3 = pd.DataFrame(list(PostB4_C3.objects.filter(created_by_id=user_connected).values('B4_C3', 'time').order_by('id').reverse()[:1]))
          resB4_C3['time'] = resB4_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsB4 = pd.merge(resB4_C1, resB4_C2, how='cross')
          resultsB4 = pd.merge(resultsB4, resB4_C3, how='cross')
          df_result_B4=resultsB4[["B4_C1", "B4_C2", "B4_C3",]]
          df_result_B4.columns=["B4_C1", "B4_C2", "B4_C3"]
          df_result_B4 = df_result_B4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          rB1=df_result_B1.iloc[0]
          fig_B1= px.line_polar(df_result_B1,r=rB1, theta=["B1_C1", "B1_C2", "B1_C3"], direction='clockwise', start_angle=70, line_close=True, color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"],)
          fig_B1.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_B1.update_layout(
               xaxis_range=[0,4],
               title="Résultats B1",
               font=dict(
        family="Helvetica, sans-serif",
        size=22,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          rB2=df_result_B2.iloc[0]
          fig_B2= px.line_polar(df_result_B2,r=rB2, theta=["B2_C1", "B2_C2", "B2_C3"], direction='clockwise', start_angle=70, line_close=True, color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"],)
          fig_B2.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_B2.update_layout(
               xaxis_range=[0,4],
               title="Résultats B2",
               font=dict(
        family="Helvetica, sans-serif",
        size=22,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          rB3=df_result_B3.iloc[0]
          fig_B3= px.line_polar(df_result_B3,r=rB3, theta=["B3_C1", "B3_C2", "B3_C3"], direction='clockwise', start_angle=70, line_close=True, color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"],)
          fig_B3.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_B3.update_layout(
               xaxis_range=[0,4],
               title="Résultats B3",
               font=dict(
        family="Helvetica, sans-serif",
        size=22,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          rB4=df_result_B4.iloc[0]
          fig_B4= px.line_polar(df_result_B4,r=rB4, theta=["B4_C1", "B4_C2", "B4_C3"], direction='clockwise', start_angle=70, line_close=True, color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"],)
          fig_B4.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_B4.update_layout(
               xaxis_range=[0,4],
               title="Résultats B4",
               font=dict(
        family="Helvetica, sans-serif",
        size=22,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))




          resultallB=pd.concat([df_result_B1, df_result_B2, df_result_B3, df_result_B4], axis=1)
          df_result_all = resultallB.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r_all=df_result_all.iloc[0]
          fig_all= px.line_polar(df_result_all,r=r_all,theta=["B1_C1", "B1_C2", "B1_C3","B2_C1", "B2_C2", "B2_C3","B3_C1", "B3_C2", "B3_C3","B4_C1", "B4_C2", "B4_C3"], direction='clockwise', start_angle=70, line_close=True,line_shape='spline', color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"],)
          fig_all.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_all.update_layout(
               xaxis_range=[0,4],
               title="tous les Résultats",
               font=dict(
               family="Helvetica, sans-serif",size=22,color="black"),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)))
          B1 = go.Scatterpolar(
          r = df_result_all[["B2_C1", "B2_C2", "B2_C3",]].iloc[0], theta = ["B2_C1", "B2_C2", "B2_C3",], mode = 'lines',   name = 'B1')
          B2 = go.Scatterpolar(
          r =df_result_all[["B1_C1", "B1_C2", "B1_C3",]].iloc[0], theta = ["B1_C1", "B1_C2", "B1_C3",], mode = 'lines', name = 'B2')
          B3 = go.Scatterpolar(
          r = df_result_all[["B3_C1", "B3_C2", "B3_C3",]].iloc[0], theta = ["B3_C1", "B3_C2", "B3_C3",], mode = 'lines',  name = 'B3')
          B4 = go.Scatterpolar(
          r =df_result_all[["B4_C1", "B4_C2", "B4_C3",]].iloc[0], theta = ["B4_C1", "B4_C2", "B4_C3",], mode = 'lines', name = 'B4')
          data = [B1,B2,B3,B4]
          fig = go.Figure(data = data, )
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)))
          polar_charts = []
    # Add your Plotly polar charts here
          polar_charts.append(fig_B1)
          polar_charts.append(fig_B2)
          polar_charts.append(fig_B3)
          polar_charts.append(fig_B4)
          polar_charts.append(fig_all)
          polar_charts.append(fig)

           # Create a buffer to store the PDF
          buffer = BytesIO()
          height, width = A4
          # Create a PDF document
          doc = SimpleDocTemplate(buffer, pagesize=A4)
          styles = getSampleStyleSheet()
          elements = []

          elements.append(Paragraph("Les résultats enregistrés pour le Pôle B", styles['Title']))

          elements.append(Spacer(1, 10))  # Add some space

          cm_to_inches = 1 / 2.54  # 1 cm = 1/2.54 inches
          cm_to_pixels = 72 / 2.54  # 1 inch = 72 pixels
          width_in_pixels = int(10 * cm_to_pixels)
          height_in_pixels = int(7* cm_to_pixels)


          for chart in polar_charts:
               chart_bytes = chart.to_image(format="png")
               img = BytesIO(chart_bytes)
               elements.append(Image(img,  width=width_in_pixels, height=height_in_pixels))

          elements.append(Paragraph("B1 : Veille pédagogique et techno-pédagogique",styles['Normal']))
          elements.append(Paragraph("B2 : Analyse des demandes",styles['Normal']))
          elements.append(Paragraph("B3 : Conception de dispositifs de développement de compétences et d’accompagnement de parcours",styles['Normal']))
          elements.append(Paragraph("B4 : Formalisation d’offres de prestation",styles['Normal']))
          elements.append(Spacer(1, 10))
          elements.append(Spacer(1, 10))


          dataframes = [resultsB1,resultsB2, resultsB3, resultsB4]
          for df in dataframes:
               table_data = [df.columns.tolist()] + df.values.tolist()
               table = Table(table_data)
               table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightcoral),
                                             ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                             ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                             ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                             ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                             ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
               elements.append(table)
          doc.build(elements)

          # Close the PDF buffer and return the response with PDF content
          pdf = buffer.getvalue()
          buffer.close()
          response = HttpResponse(content_type='application/pdf')
          response['Content-Disposition'] = 'attachment; filename="exportpoleB.pdf"'
          response.write(pdf)
          return response

      else :
          info = "Les résultats seront disponible après avoir remplie la section B"
      return render(request, 'questions/poleA/resultsC.html', {'info' : info})

def generateC_pdf(request):
      user_connected=request.user.id
      if PostC1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC1_C3.objects.filter(created_by_id=user_connected).all().exists() and PostC2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC2_C3.objects.filter(created_by_id=user_connected).all().exists() \
          and PostC3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC3_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostC4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC4_C3.objects.filter(created_by_id=user_connected).all().exists():
          resC1_C1 = pd.DataFrame(list(PostC1_C1.objects.filter(created_by_id=user_connected).values('C1_C1').order_by('id').reverse()[:1]))
          resC1_C2 = pd.DataFrame(list(PostC1_C2.objects.filter(created_by_id=user_connected).values('C1_C2').order_by('id').reverse()[:1]))
          resC1_C3 = pd.DataFrame(list(PostC1_C3.objects.filter(created_by_id=user_connected).values('C1_C3', 'time').order_by('id').reverse()[:1]))
          resC1_C3['time'] = resC1_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsC1 = pd.merge(resC1_C1, resC1_C2, how='cross')
          resultsC1 = pd.merge(resultsC1, resC1_C3, how='cross')
          df_result_C1=resultsC1[["C1_C1", "C1_C2", "C1_C3",]]
          df_result_C1.columns=["C1_C1", "C1_C2", "C1_C3"]
          df_result_C1 = df_result_C1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])



          resC2_C1 = pd.DataFrame(list(PostC2_C1.objects.filter(created_by_id=user_connected).values('C2_C1').order_by('id').reverse()[:1]))
          resC2_C2 = pd.DataFrame(list(PostC2_C2.objects.filter(created_by_id=user_connected).values('C2_C2').order_by('id').reverse()[:1]))
          resC2_C3 = pd.DataFrame(list(PostC2_C3.objects.filter(created_by_id=user_connected).values('C2_C3', 'time').order_by('id').reverse()[:1]))
          resC2_C3['time'] = resC2_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsC2 = pd.merge(resC2_C1, resC2_C2, how='cross')
          resultsC2 = pd.merge(resultsC2, resC2_C3, how='cross')
          df_result_C2=resultsC2[["C2_C1", "C2_C2", "C2_C3",]]
          df_result_C2.columns=["C2_C1", "C2_C2", "C2_C3"]
          df_result_C2 = df_result_C2.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resC3_C1 = pd.DataFrame(list(PostC3_C1.objects.filter(created_by_id=user_connected).values('C3_C1').order_by('id').reverse()[:1]))
          resC3_C2 = pd.DataFrame(list(PostC3_C2.objects.filter(created_by_id=user_connected).values('C3_C2').order_by('id').reverse()[:1]))
          resC3_C3 = pd.DataFrame(list(PostC3_C3.objects.filter(created_by_id=user_connected).values('C3_C3','time').order_by('id').reverse()[:1]))
          resC3_C3['time'] = resC3_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsC3 = pd.merge(resC3_C1, resC3_C2, how='cross')
          resultsC3 = pd.merge(resultsC3, resC3_C3, how='cross')
          df_result_C3=resultsC3[["C3_C1", "C3_C2", "C3_C3",]]
          df_result_C3.columns=["C3_C1", "C3_C2", "C3_C3"]
          df_result_C3 = df_result_C3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resC4_C1 = pd.DataFrame(list(PostC4_C1.objects.filter(created_by_id=user_connected).values('C4_C1').order_by('id').reverse()[:1]))
          resC4_C2 = pd.DataFrame(list(PostC4_C2.objects.filter(created_by_id=user_connected).values('C4_C2').order_by('id').reverse()[:1]))
          resC4_C3 = pd.DataFrame(list(PostC4_C3.objects.filter(created_by_id=user_connected).values('C4_C3', 'time').order_by('id').reverse()[:1]))
          resC4_C3['time'] = resC4_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsC4 = pd.merge(resC4_C1, resC4_C2, how='cross')
          resultsC4 = pd.merge(resultsC4, resC4_C3, how='cross')
          df_result_C4=resultsC4[["C4_C1", "C4_C2", "C4_C3",]]
          df_result_C4.columns=["C4_C1", "C4_C2", "C4_C3"]
          df_result_C4 = df_result_C4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          rC1=df_result_C1.iloc[0]
          fig_C1= px.line_polar(df_result_C1,r=rC1, theta=["C1_C1", "C1_C2", "C1_C3"], direction='clockwise', start_angle=70, line_close=True,  color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
          fig_C1.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_C1.update_layout(
               xaxis_range=[0,4],
               title="Résultats C1",
               font=dict(
        family="Helvetica, sans-serif",
        size=22,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          rC2=df_result_C2.iloc[0]
          fig_C2= px.line_polar(df_result_C2,r=rC2, theta=["C2_C1", "C2_C2", "C2_C3"], direction='clockwise', start_angle=70, line_close=True,  color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
          fig_C2.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_C2.update_layout(
               xaxis_range=[0,4],
               title="Résultats C2",
               font=dict(
        family="Helvetica, sans-serif",
        size=22,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          rC3=df_result_C3.iloc[0]
          fig_C3= px.line_polar(df_result_C3,r=rC3, theta=["C3_C1", "C3_C2", "C3_C3"], direction='clockwise', start_angle=70, line_close=True,  color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
          fig_C3.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_C3.update_layout(
               xaxis_range=[0,4],
               title="Résultats C3",
               font=dict(
        family="Courier New, monospace",
        size=24,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          rC4=df_result_C4.iloc[0]
          fig_C4= px.line_polar(df_result_C4,r=rC4, theta=["C4_C1", "C4_C2", "C4_C3"], direction='clockwise', start_angle=70, line_close=True,  color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
          fig_C4.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_C4.update_layout(
               xaxis_range=[0,4],
               title="Résultats C4",
               font=dict(
        family="Courier New, monospace",
        size=24,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))




          resultallC=pd.concat([df_result_C1, df_result_C2, df_result_C3, df_result_C4], axis=1)
          df_result_all = resultallC.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r_all=df_result_all.iloc[0]
          fig_all= px.line_polar(df_result_all,r=r_all,theta=["C1_C1", "C1_C2", "C1_C3","C2_C1", "C2_C2", "C2_C3","C3_C1", "C3_C2", "C3_C3","C4_C1", "C4_C2", "C4_C3"], direction='clockwise', start_angle=70, line_close=True, color_discrete_sequence=["green", "blue", "goldenrod", "magenta"],line_shape='spline')
          fig_all.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_all.update_layout(
               xaxis_range=[0,4],
               title="tous les Résultats",
               font=dict(
               family="Helvetica, sans-serif",size=22,color="black"),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)))
          C1 = go.Scatterpolar(
          r = df_result_all[["C2_C1", "C2_C2", "C2_C3",]].iloc[0], theta = ["C2_C1", "C2_C2", "C2_C3",], mode = 'lines',   name = 'C1')
          C2 = go.Scatterpolar(
          r =df_result_all[["C1_C1", "C1_C2", "C1_C3",]].iloc[0], theta = ["C1_C1", "C1_C2", "C1_C3",], mode = 'lines', name = 'C2')
          C3 = go.Scatterpolar(
          r = df_result_all[["C3_C1", "C3_C2", "C3_C3",]].iloc[0], theta = ["C3_C1", "C3_C2", "C3_C3",], mode = 'lines',  name = 'C3')
          C4 = go.Scatterpolar(
          r =df_result_all[["C4_C1", "C4_C2", "C4_C3",]].iloc[0], theta = ["C4_C1", "C4_C2", "C4_C3",], mode = 'lines', name = 'C4')
          data = [C1,C2,C3,C4]
          fig = go.Figure(data = data, )
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)))
          polar_charts = []
    # Add your Plotly polar charts here
          polar_charts.append(fig_C1)
          polar_charts.append(fig_C2)
          polar_charts.append(fig_C3)
          polar_charts.append(fig_C4)
          polar_charts.append(fig_all)
          polar_charts.append(fig)

           # Create a buffer to store the PDF
          buffer = BytesIO()
          height, width = A4
          # Create a PDF document
          doc = SimpleDocTemplate(buffer, pagesize=A4)
          styles = getSampleStyleSheet()
          elements = []

          elements.append(Paragraph("Les résultats enregistrés pour le Pôle C", styles['Title']))

          elements.append(Spacer(1, 10))  # Add some space

          cm_to_inches = 1 / 2.54  # 1 cm = 1/2.54 inches
          cm_to_pixels = 72 / 2.54  # 1 inch = 72 pixels
          width_in_pixels = int(10 * cm_to_pixels)
          height_in_pixels = int(7* cm_to_pixels)


          for chart in polar_charts:
               chart_bytes = chart.to_image(format="png")
               img = BytesIO(chart_bytes)
               elements.append(Image(img,  width=width_in_pixels, height=height_in_pixels))

          elements.append(Paragraph("C1 : Management de projets",styles['Normal']))
          elements.append(Paragraph("C2 : Animation de collectifs de travail",styles['Normal']))
          elements.append(Paragraph("C3 : Animation de démarches partenariales",styles['Normal']))
          elements.append(Paragraph("C4 : Contribution à la démarche qualité",styles['Normal']))
          elements.append(Spacer(1, 10))
          elements.append(Spacer(1, 10))


          dataframes = [resultsC1,resultsC2, resultsC3, resultsC4]
          for df in dataframes:
               table_data = [df.columns.tolist()] + df.values.tolist()
               table = Table(table_data)
               table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lawngreen),
                                             ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                             ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                             ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                             ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                             ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
               elements.append(table)
          doc.build(elements)

          # Close the PDF buffer and return the response with PDF content
          pdf = buffer.getvalue()
          buffer.close()
          response = HttpResponse(content_type='application/pdf')
          response['Content-Disposition'] = 'attachment; filename="exportpoleC.pdf"'
          response.write(pdf)
          return response
      else :
          info = "Les résultats seront disponible après avoir remplie la section C"
      return render(request, 'questions/poleC/resultsC.html', {'info' : info})

def generateA_pdf(request):
      user_connected=request.user.id
      if PostA1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA1_C3.objects.filter(created_by_id=user_connected).all().exists() and PostA2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA2_C3.objects.filter(created_by_id=user_connected).all().exists() \
          and PostA3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA3_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostA4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA4_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostA5_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA5_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA5_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostA6_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA6_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA6_C3.objects.filter(created_by_id=user_connected).all().exists():


          resA1_C1 = pd.DataFrame(list(PostA1_C1.objects.filter(created_by_id=user_connected).values('A1_C1').order_by('id').reverse()[:1]))
          resA1_C2 = pd.DataFrame(list(PostA1_C2.objects.filter(created_by_id=user_connected).values('A1_C2').order_by('id').reverse()[:1]))
          resA1_C3 = pd.DataFrame(list(PostA1_C3.objects.filter(created_by_id=user_connected).values('A1_C3', 'time').order_by('id').reverse()[:1]))
          resA1_C3['time'] = resA1_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsA1 = pd.merge(resA1_C1, resA1_C2, how='cross')
          resultsA1 = pd.merge(resultsA1, resA1_C3, how='cross')
          df_result_A1=resultsA1[["A1_C1", "A1_C2", "A1_C3",]]
          df_result_A1.columns=["A1_C1", "A1_C2", "A1_C3"]
          df_result_A1 = df_result_A1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])



          resA2_C1 = pd.DataFrame(list(PostA2_C1.objects.filter(created_by_id=user_connected).values('A2_C1').order_by('id').reverse()[:1]))
          resA2_C2 = pd.DataFrame(list(PostA2_C2.objects.filter(created_by_id=user_connected).values('A2_C2').order_by('id').reverse()[:1]))
          resA2_C3 = pd.DataFrame(list(PostA2_C3.objects.filter(created_by_id=user_connected).values('A2_C3', 'time').order_by('id').reverse()[:1]))
          resA2_C3['time'] = resA2_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsA2 = pd.merge(resA2_C1, resA2_C2, how='cross')
          resultsA2 = pd.merge(resultsA2, resA2_C3, how='cross')
          df_result_A2=resultsA2[["A2_C1", "A2_C2", "A2_C3",]]
          df_result_A2.columns=["A2_C1", "A2_C2", "A2_C3"]
          df_result_A2 = df_result_A2.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resA3_C1 = pd.DataFrame(list(PostA3_C1.objects.filter(created_by_id=user_connected).values('A3_C1').order_by('id').reverse()[:1]))
          resA3_C2 = pd.DataFrame(list(PostA3_C2.objects.filter(created_by_id=user_connected).values('A3_C2').order_by('id').reverse()[:1]))
          resA3_C3 = pd.DataFrame(list(PostA3_C3.objects.filter(created_by_id=user_connected).values('A3_C3','time').order_by('id').reverse()[:1]))
          resA3_C3['time'] = resA3_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsA3 = pd.merge(resA3_C1, resA3_C2, how='cross')
          resultsA3 = pd.merge(resultsA3, resA3_C3, how='cross')
          df_result_A3=resultsA3[["A3_C1", "A3_C2", "A3_C3",]]
          df_result_A3.columns=["A3_C1", "A3_C2", "A3_C3"]
          df_result_A3 = df_result_A3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resA4_C1 = pd.DataFrame(list(PostA4_C1.objects.filter(created_by_id=user_connected).values('A4_C1').order_by('id').reverse()[:1]))
          resA4_C2 = pd.DataFrame(list(PostA4_C2.objects.filter(created_by_id=user_connected).values('A4_C2').order_by('id').reverse()[:1]))
          resA4_C3 = pd.DataFrame(list(PostA4_C3.objects.filter(created_by_id=user_connected).values('A4_C3', 'time').order_by('id').reverse()[:1]))
          resA4_C3['time'] = resA4_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsA4 = pd.merge(resA4_C1, resA4_C2, how='cross')
          resultsA4 = pd.merge(resultsA4, resA4_C3, how='cross')
          df_result_A4=resultsA4[["A4_C1", "A4_C2", "A4_C3",]]
          df_result_A4.columns=["A4_C1", "A4_C2", "A4_C3"]
          df_result_A4 = df_result_A4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resA5_C1 = pd.DataFrame(list(PostA5_C1.objects.filter(created_by_id=user_connected).values('A5_C1').order_by('id').reverse()[:1]))
          resA5_C2 = pd.DataFrame(list(PostA5_C2.objects.filter(created_by_id=user_connected).values('A5_C2').order_by('id').reverse()[:1]))
          resA5_C3 = pd.DataFrame(list(PostA5_C3.objects.filter(created_by_id=user_connected).values('A5_C3', 'time').order_by('id').reverse()[:1]))
          resA5_C3['time'] = resA5_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsA5 = pd.merge(resA5_C1, resA5_C2, how='cross')
          resultsA5 = pd.merge(resultsA5, resA5_C3, how='cross')
          df_result_A5=resultsA5[["A5_C1", "A5_C2", "A5_C3",]]
          df_result_A5.columns=["A5_C1", "A5_C2", "A5_C3"]
          df_result_A5 = df_result_A4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resA6_C1 = pd.DataFrame(list(PostA6_C1.objects.filter(created_by_id=user_connected).values('A6_C1').order_by('id').reverse()[:1]))
          resA6_C2 = pd.DataFrame(list(PostA6_C2.objects.filter(created_by_id=user_connected).values('A6_C2').order_by('id').reverse()[:1]))
          resA6_C3 = pd.DataFrame(list(PostA6_C3.objects.filter(created_by_id=user_connected).values('A6_C3', 'time').order_by('id').reverse()[:1]))
          resA6_C3['time'] = resA6_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsA6 = pd.merge(resA6_C1, resA6_C2, how='cross')
          resultsA6 = pd.merge(resultsA6, resA6_C3, how='cross')
          df_result_A6=resultsA6[["A6_C1", "A6_C2", "A6_C3",]]
          df_result_A6.columns=["A6_C1", "A6_C2", "A6_C3"]
          df_result_A6 = df_result_A4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          rA1=df_result_A1.iloc[0]
          fig_A1= px.line_polar(df_result_A1,r=rA1, theta=["A1_C1", "A1_C2", "A1_C3"], direction='clockwise', start_angle=70, line_close=True,)
          fig_A1.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A1.update_layout(
               xaxis_range=[0,4],
               title="Résultats A1",
               font=dict(
        family="Helvetica, sans-serif",
        size=22,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          rA2=df_result_A2.iloc[0]
          fig_A2= px.line_polar(df_result_A2,r=rA2, theta=["A2_C1", "A2_C2", "A2_C3"], direction='clockwise', start_angle=70, line_close=True, )
          fig_A2.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A2.update_layout(
               xaxis_range=[0,4],
               title="Résultats A2",
               font=dict(
        family="Helvetica, sans-serif",
        size=22,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          rA3=df_result_A3.iloc[0]
          fig_A3= px.line_polar(df_result_A3,r=rA3, theta=["A3_C1", "A3_C2", "A3_C3"], direction='clockwise', start_angle=70, line_close=True,)
          fig_A3.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A3.update_layout(
               xaxis_range=[0,4],
               title="Résultats A3",
               font=dict(
        family="Helvetica, sans-serif",
        size=22,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          rA4=df_result_A4.iloc[0]
          fig_A4= px.line_polar(df_result_A4,r=rA4, theta=["A4_C1", "A4_C2", "A4_C3"], direction='clockwise', start_angle=70, line_close=True,)
          fig_A4.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A4.update_layout(
               xaxis_range=[0,4],
               title="Résultats A4",
               font=dict(
        family="Helvetica, sans-serif",
        size=22,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          rA5=df_result_A5.iloc[0]
          fig_A5= px.line_polar(df_result_A4,r=rA4, theta=["A5_C1", "A5_C2", "A5_C3"], direction='clockwise', start_angle=70, line_close=True,)
          fig_A5.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A5.update_layout(
               xaxis_range=[0,4],
               title="Résultats A5",
               font=dict(
        family="Helvetica, sans-serif",
        size=22,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          rA6=df_result_A6.iloc[0]
          fig_A6= px.line_polar(df_result_A4,r=rA4, theta=["A6_C1", "A6_C2", "A6_C3"], direction='clockwise', start_angle=70, line_close=True,)
          fig_A6.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A6.update_layout(
               xaxis_range=[0,4],
               title="Résultats A6",
               font=dict(
        family="Helvetica, sans-serif",
        size=22,
        color="black"
    ),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))





          resultallA=pd.concat([df_result_A1, df_result_A2, df_result_A3, df_result_A4, df_result_A5, df_result_A6], axis=1)
          df_result_all = resultallA.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r_all=df_result_all.iloc[0]
          fig_all= px.line_polar(df_result_all,r=r_all,theta=["A1_C1", "A1_C2", "A1_C3","A2_C1", "A2_C2", "A2_C3","A3_C1", "A3_C2", "A3_C3","A4_C1", "A4_C2", "A4_C3", "A5_C1", "A5_C2", "A5_C3", "A6_C1", "A6_C2", "A6_C3"], direction='clockwise', start_angle=70, line_close=True,line_shape='spline',)
          fig_all.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_all.update_layout(
               xaxis_range=[0,4],
               title="tous les Résultats",
               font=dict(
               family="Helvetica, sans-serif",size=22,color="black"),
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None)))

          polar_charts = []
    # Add your Plotly polar charts here
          polar_charts.append(fig_A1)
          polar_charts.append(fig_A2)
          polar_charts.append(fig_A3)
          polar_charts.append(fig_A4)
          polar_charts.append(fig_A5)
          polar_charts.append(fig_A6)
          polar_charts.append(fig_all)


           # Create a buffer to store the PDF
          buffer = BytesIO()
          doc = SimpleDocTemplate(buffer, pagesize=letter)
          styles = getSampleStyleSheet()
          elements = []

          elements.append(Paragraph("Les résultats enregistrés pour le Pôle A", styles['Title']))

          elements.append(Spacer(1, 12))  # Add some space

          cm_to_inches = 1 / 2.54  # 1 cm = 1/2.54 inches
          cm_to_pixels = 72 / 2.54  # 1 inch = 72 pixels
          width_in_pixels = int(10 * cm_to_pixels)
          height_in_pixels = int(7* cm_to_pixels)


          for chart in polar_charts:
               chart_bytes = chart.to_image(format="png")
               img = BytesIO(chart_bytes)
               elements.append(Image(img,  width=width_in_pixels, height=height_in_pixels))

          elements.append(Paragraph("A1 : Veille socio-économique, réglementaire, concurrentielle et commerciale",styles['Normal']))
          elements.append(Paragraph("A2 : Diagnostic et analyse des besoins territoriaux et/ou sectoriels",styles['Normal']))
          elements.append(Paragraph("A3 : Contribution à la définition de la politique de l’organisation",styles['Normal']))
          elements.append(Paragraph("A4 : Conseil aux décideurs",styles['Normal']))
          elements.append(Paragraph("A5 : Représentation institutionnelle sur les territoires",styles['Normal']))
          elements.append(Paragraph("A6 : Commercialisation de l’offre de prestations et recherche de marchés",styles['Normal']))
          elements.append(Spacer(1, 12))  # Add some space
          dataframes = [resultsA1,resultsA2, resultsA3, resultsA4, resultsA5, resultsA6]
          for df in dataframes:
               table_data = [df.columns.tolist()] + df.values.tolist()
               table = Table(table_data)
               table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.blue),
                                             ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                             ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                             ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                             ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                             ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
               elements.append(table)
          doc.build(elements)

          # Close the PDF buffer and return the response with PDF content
          pdf = buffer.getvalue()
          buffer.close()
          response = HttpResponse(content_type='application/pdf')
          response['Content-Disposition'] = 'attachment; filename="exportpoleA.pdf"'
          response.write(pdf)
          return response

      else :
          info = "Les résultats seront disponible après avoir remplie la section A"
      return render(request, 'questions/poleA/resultsA.html', {'info' : info})

################################################################Test
def resultatsA1(request):
     user_connected=request.user.id
     if PostA1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA1_C3.objects.filter(created_by_id=user_connected).all().exists():
          resA1_C1 = pd.DataFrame(list(PostA1_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A1_C1').order_by('id').reverse()[:1]))
          resA1_C2 = pd.DataFrame(list(PostA1_C2.objects.filter(created_by_id=user_connected).values('A1_C2').order_by('id').reverse()[:1]))
          resA1_C3 = pd.DataFrame(list(PostA1_C3.objects.filter(created_by_id=user_connected).values('A1_C3', 'time').order_by('id').reverse()[:1]))
          resA1_C3['time'] = resA1_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsA1 = pd.merge(resA1_C1, resA1_C2, how='cross')
          resultsA1 = pd.merge(resultsA1, resA1_C3, how='cross')
          df_result_A1=resultsA1[["A1_C1", "A1_C2", "A1_C3",]]
          df_result_A1.columns=["A1_C1", "A1_C2", "A1_C3"]
          df_result_A1 = df_result_A1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rA1=df_result_A1.iloc[0]
          fig_A1= px.line_polar(df_result_A1,r=rA1, theta=["A1_C1", "A1_C2", "A1_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=px.colors.sequential.Agsunset)
          fig_A1.update_traces(fill='toself',)
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A1.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))



          chart_A1 = fig_A1.to_html(config = {'displayModeBar': False})
          resultsA1 = resultsA1.to_dict(orient='records')
          return render(request, 'questions/poleA/resultsAdetails.html', { 'resultsA1' : resultsA1, 'chart_A1' : chart_A1})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleA/resultsAdetails.html', {'info' : info})


def resultatsA2(request):
     user_connected=request.user.id
     if PostA2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA2_C3.objects.filter(created_by_id=user_connected).all().exists():
          resA2_C1 = pd.DataFrame(list(PostA2_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A2_C1').order_by('id').reverse()[:1]))
          resA2_C2 = pd.DataFrame(list(PostA2_C2.objects.filter(created_by_id=user_connected).values('A2_C2').order_by('id').reverse()[:1]))
          resA2_C3 = pd.DataFrame(list(PostA2_C3.objects.filter(created_by_id=user_connected).values('A2_C3', 'time').order_by('id').reverse()[:1]))
          resA2_C3['time'] = resA2_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsA2 = pd.merge(resA2_C1, resA2_C2, how='cross')
          resultsA2 = pd.merge(resultsA2, resA2_C3, how='cross')
          df_result_A2=resultsA2[["A2_C1", "A2_C2", "A2_C3",]]
          df_result_A2.columns=["A2_C1", "A2_C2", "A2_C3"]
          df_result_A2 = df_result_A2.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rA2=df_result_A2.iloc[0]
          fig_A2= px.line_polar(df_result_A2,r=rA2, theta=["A2_C1", "A2_C2", "A2_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=px.colors.sequential.Agsunset)
          fig_A2.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A2.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          chart_A2 = fig_A2.to_html(config = {'displayModeBar': False})
          resultsA2 = resultsA2.to_dict(orient='records')
          return render(request, 'questions/poleA/resultsAdetails.html', { 'resultsA2' : resultsA2, 'chart_A2' : chart_A2})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleA/resultsAdetails.html', {'info' : info})



def resultatsA3(request):
     user_connected=request.user.id
     if PostA3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA3_C3.objects.filter(created_by_id=user_connected).all().exists():
          resA3_C1 = pd.DataFrame(list(PostA3_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A3_C1').order_by('id').reverse()[:1]))
          resA3_C2 = pd.DataFrame(list(PostA3_C2.objects.filter(created_by_id=user_connected).values('A3_C2').order_by('id').reverse()[:1]))
          resA3_C3 = pd.DataFrame(list(PostA3_C3.objects.filter(created_by_id=user_connected).values('A3_C3', 'time').order_by('id').reverse()[:1]))
          resA3_C3['time'] = resA3_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsA3 = pd.merge(resA3_C1, resA3_C2, how='cross')
          resultsA3 = pd.merge(resultsA3, resA3_C3, how='cross')
          df_result_A3=resultsA3[["A3_C1", "A3_C3", "A3_C3",]]
          df_result_A3.columns=["A3_C1", "A3_C3", "A3_C3"]
          df_result_A3 = df_result_A3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rA3=df_result_A3.iloc[0]
          fig_A3= px.line_polar(df_result_A3,r=rA3, theta=["A3_C1", "A3_C2", "A3_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=px.colors.sequential.Agsunset)
          fig_A3.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A3.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          chart_A3 = fig_A3.to_html(config = {'displayModeBar': False})
          resultsA3 = resultsA3.to_dict(orient='records')
          return render(request, 'questions/poleA/resultsAdetails.html', { 'resultsA3' : resultsA3, 'chart_A3' : chart_A3})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleA/resultsAdetails.html', {'info' : info})

def resultatsA4(request):
     user_connected=request.user.id
     if PostA4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA4_C3.objects.filter(created_by_id=user_connected).all().exists():
          resA4_C1 = pd.DataFrame(list(PostA4_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A4_C1').order_by('id').reverse()[:1]))
          resA4_C2 = pd.DataFrame(list(PostA4_C2.objects.filter(created_by_id=user_connected).values('A4_C2').order_by('id').reverse()[:1]))
          resA4_C3 = pd.DataFrame(list(PostA4_C3.objects.filter(created_by_id=user_connected).values('A4_C3', 'time').order_by('id').reverse()[:1]))
          resA4_C3['time'] = resA4_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsA4 = pd.merge(resA4_C1, resA4_C2, how='cross')
          resultsA4 = pd.merge(resultsA4, resA4_C3, how='cross')
          df_result_A4=resultsA4[["A4_C1", "A4_C2", "A4_C3",]]
          df_result_A4.columns=["A4_C1", "A4_C2", "A4_C3"]
          df_result_A4 = df_result_A4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rA4=df_result_A4.iloc[0]
          fig_A4= px.line_polar(df_result_A4,r=rA4, theta=["A4_C1", "A4_C2", "A4_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=px.colors.sequential.Agsunset)
          fig_A4.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A4.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          chart_A4 = fig_A4.to_html(config = {'displayModeBar': False})
          resultsA4 = resultsA4.to_dict(orient='records')
          return render(request, 'questions/poleA/resultsAdetails.html', { 'resultsA4' : resultsA4, 'chart_A4' : chart_A4})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleA/resultsAdetails.html', {'info' : info})



def resultatsA5(request):
     user_connected=request.user.id
     if PostA5_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA5_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA5_C3.objects.filter(created_by_id=user_connected).all().exists():
          resA5_C1 = pd.DataFrame(list(PostA5_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A5_C1').order_by('id').reverse()[:1]))
          resA5_C2 = pd.DataFrame(list(PostA5_C2.objects.filter(created_by_id=user_connected).values('A5_C2').order_by('id').reverse()[:1]))
          resA5_C3 = pd.DataFrame(list(PostA5_C3.objects.filter(created_by_id=user_connected).values('A5_C3', 'time').order_by('id').reverse()[:1]))
          resA5_C3['time'] = resA5_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsA5 = pd.merge(resA5_C1, resA5_C2, how='cross')
          resultsA5 = pd.merge(resultsA5, resA5_C3, how='cross')
          df_result_A5=resultsA5[["A5_C1", "A5_C2", "A5_C3",]]
          df_result_A5.columns=["A5_C1", "A5_C2", "A5_C3"]
          df_result_A5 = df_result_A5.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rA5=df_result_A5.iloc[0]
          fig_A5= px.line_polar(df_result_A5,r=rA5, theta=["A5_C1", "A5_C2", "A5_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=px.colors.sequential.Agsunset)
          fig_A5.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A5.update_layout(
               xaxis_range=[0,5],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          chart_A5 = fig_A5.to_html(config = {'displayModeBar': False})
          resultsA5 = resultsA5.to_dict(orient='records')
          return render(request, 'questions/poleA/resultsAdetails.html', { 'resultsA5' : resultsA5, 'chart_A5' : chart_A5})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleA/resultsAdetails.html', {'info' : info})

def resultatsA6(request):
     user_connected=request.user.id
     if PostA6_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA6_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA6_C3.objects.filter(created_by_id=user_connected).all().exists():
          resA6_C1 = pd.DataFrame(list(PostA6_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'A6_C1').order_by('id').reverse()[:1]))
          resA6_C2 = pd.DataFrame(list(PostA6_C2.objects.filter(created_by_id=user_connected).values('A6_C2').order_by('id').reverse()[:1]))
          resA6_C3 = pd.DataFrame(list(PostA6_C3.objects.filter(created_by_id=user_connected).values('A6_C3', 'time').order_by('id').reverse()[:1]))
          resA6_C3['time'] = resA6_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsA6 = pd.merge(resA6_C1, resA6_C2, how='cross')
          resultsA6 = pd.merge(resultsA6, resA6_C3, how='cross')
          df_result_A6=resultsA6[["A6_C1", "A6_C2", "A6_C3",]]
          df_result_A6.columns=["A6_C1", "A6_C2", "A6_C3"]
          df_result_A6 = df_result_A6.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rA6=df_result_A6.iloc[0]
          fig_A6= px.line_polar(df_result_A6,r=rA6, theta=["A6_C1", "A6_C2", "A6_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=px.colors.sequential.Agsunset)
          fig_A6.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 6 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_A6.update_layout(
               xaxis_range=[0,6],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          chart_A6 = fig_A6.to_html(config = {'displayModeBar': False})
          resultsA6 = resultsA6.to_dict(orient='records')
          return render(request, 'questions/poleA/resultsAdetails.html', { 'resultsA6' : resultsA6, 'chart_A6' : chart_A6})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleA/resultsAdetails.html', {'info' : info})

###############################################################
def resultatsB1(request):
     user_connected=request.user.id
     if PostB1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB1_C3.objects.filter(created_by_id=user_connected).all().exists():
          resB1_C1 = pd.DataFrame(list(PostB1_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'B1_C1').order_by('id').reverse()[:1]))
          resB1_C2 = pd.DataFrame(list(PostB1_C2.objects.filter(created_by_id=user_connected).values('B1_C2').order_by('id').reverse()[:1]))
          resB1_C3 = pd.DataFrame(list(PostB1_C3.objects.filter(created_by_id=user_connected).values('B1_C3', 'time').order_by('id').reverse()[:1]))
          resB1_C3['time'] = resB1_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsB1 = pd.merge(resB1_C1, resB1_C2, how='cross')
          resultsB1 = pd.merge(resultsB1, resB1_C3, how='cross')
          df_result_B1=resultsB1[["B1_C1", "B1_C2", "B1_C3",]]
          df_result_B1.columns=["B1_C1", "B1_C2", "B1_C3"]
          df_result_B1 = df_result_B1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rB1=df_result_B1.iloc[0]
          fig_B1= px.line_polar(df_result_B1,r=rB1, theta=["B1_C1", "B1_C2", "B1_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"])
          fig_B1.update_traces(fill='toself',)
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Bdjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_B1.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))



          chart_B1 = fig_B1.to_html(config = {'displayModeBar': False})
          resultsB1 = resultsB1.to_dict(orient='records')
          return render(request, 'questions/poleB/resultsBdetails.html', { 'resultsB1' : resultsB1, 'chart_B1' : chart_B1})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleB/resultsBdetails.html', {'info' : info})


def resultatsB2(request):
     user_connected=request.user.id
     if PostB2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB2_C3.objects.filter(created_by_id=user_connected).all().exists():
          resB2_C1 = pd.DataFrame(list(PostB2_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'B2_C1').order_by('id').reverse()[:1]))
          resB2_C2 = pd.DataFrame(list(PostB2_C2.objects.filter(created_by_id=user_connected).values('B2_C2').order_by('id').reverse()[:1]))
          resB2_C3 = pd.DataFrame(list(PostB2_C3.objects.filter(created_by_id=user_connected).values('B2_C3', 'time').order_by('id').reverse()[:1]))
          resB2_C3['time'] = resB2_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsB2 = pd.merge(resB2_C1, resB2_C2, how='cross')
          resultsB2 = pd.merge(resultsB2, resB2_C3, how='cross')
          df_result_B2=resultsB2[["B2_C1", "B2_C2", "B2_C3",]]
          df_result_B2.columns=["B2_C1", "B2_C2", "B2_C3"]
          df_result_B2 = df_result_B2.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rB2=df_result_B2.iloc[0]
          fig_B2= px.line_polar(df_result_B2,r=rB2, theta=["B2_C1", "B2_C2", "B2_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"])
          fig_B2.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_B2.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          chart_B2 = fig_B2.to_html(config = {'displayModeBar': False})
          resultsB2 = resultsB2.to_dict(orient='records')
          return render(request, 'questions/poleB/resultsBdetails.html', { 'resultsB2' : resultsB2, 'chart_B2' : chart_B2})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleB/resultsBdetails.html', {'info' : info})



def resultatsB3(request):
     user_connected=request.user.id
     if PostB3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB3_C3.objects.filter(created_by_id=user_connected).all().exists():
          resB3_C1 = pd.DataFrame(list(PostB3_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'B3_C1').order_by('id').reverse()[:1]))
          resB3_C2 = pd.DataFrame(list(PostB3_C2.objects.filter(created_by_id=user_connected).values('B3_C2').order_by('id').reverse()[:1]))
          resB3_C3 = pd.DataFrame(list(PostB3_C3.objects.filter(created_by_id=user_connected).values('B3_C3', 'time').order_by('id').reverse()[:1]))
          resB3_C3['time'] = resB3_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsB3 = pd.merge(resB3_C1, resB3_C2, how='cross')
          resultsB3 = pd.merge(resultsB3, resB3_C3, how='cross')
          df_result_B3=resultsB3[["B3_C1", "B3_C3", "B3_C3",]]
          df_result_B3.columns=["B3_C1", "B3_C3", "B3_C3"]
          df_result_B3 = df_result_B3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rB3=df_result_B3.iloc[0]
          fig_B3= px.line_polar(df_result_B3,r=rB3, theta=["B3_C1", "B3_C2", "B3_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"])
          fig_B3.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_B3.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          chart_B3 = fig_B3.to_html(config = {'displayModeBar': False})
          resultsB3 = resultsB3.to_dict(orient='records')
          return render(request, 'questions/poleB/resultsBdetails.html', { 'resultsB3' : resultsB3, 'chart_B3' : chart_B3})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleB/resultsBdetails.html', {'info' : info})

def resultatsB4(request):
     user_connected=request.user.id
     if PostB4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB4_C3.objects.filter(created_by_id=user_connected).all().exists():
          resB4_C1 = pd.DataFrame(list(PostB4_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'B4_C1').order_by('id').reverse()[:1]))
          resB4_C2 = pd.DataFrame(list(PostB4_C2.objects.filter(created_by_id=user_connected).values('B4_C2').order_by('id').reverse()[:1]))
          resB4_C3 = pd.DataFrame(list(PostB4_C3.objects.filter(created_by_id=user_connected).values('B4_C3', 'time').order_by('id').reverse()[:1]))
          resB4_C3['time'] = resB4_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsB4 = pd.merge(resB4_C1, resB4_C2, how='cross')
          resultsB4 = pd.merge(resultsB4, resB4_C3, how='cross')
          df_result_B4=resultsB4[["B4_C1", "B4_C2", "B4_C3",]]
          df_result_B4.columns=["B4_C1", "B4_C2", "B4_C3"]
          df_result_B4 = df_result_B4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rB4=df_result_B4.iloc[0]
          fig_B4= px.line_polar(df_result_B4,r=rB4, theta=["B4_C1", "B4_C2", "B4_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=["orange", "green", "blue", "goldenrod", "magenta"])
          fig_B4.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_B4.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          chart_B4 = fig_B4.to_html(config = {'displayModeBar': False})
          resultsB4 = resultsB4.to_dict(orient='records')
          return render(request, 'questions/poleB/resultsBdetails.html', { 'resultsB4' : resultsB4, 'chart_B4' : chart_B4})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleB/resultsBdetails.html', {'info' : info})



###############################################################
def resultatsC1(request):
     user_connected=request.user.id
     if PostC1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC1_C3.objects.filter(created_by_id=user_connected).all().exists():
          resC1_C1 = pd.DataFrame(list(PostC1_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'C1_C1').order_by('id').reverse()[:1]))
          resC1_C2 = pd.DataFrame(list(PostC1_C2.objects.filter(created_by_id=user_connected).values('C1_C2').order_by('id').reverse()[:1]))
          resC1_C3 = pd.DataFrame(list(PostC1_C3.objects.filter(created_by_id=user_connected).values('C1_C3', 'time').order_by('id').reverse()[:1]))
          resC1_C3['time'] = resC1_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsC1 = pd.merge(resC1_C1, resC1_C2, how='cross')
          resultsC1 = pd.merge(resultsC1, resC1_C3, how='cross')
          df_result_C1=resultsC1[["C1_C1", "C1_C2", "C1_C3",]]
          df_result_C1.columns=["C1_C1", "C1_C2", "C1_C3"]
          df_result_C1 = df_result_C1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rC1=df_result_C1.iloc[0]
          fig_C1= px.line_polar(df_result_C1,r=rC1, theta=["C1_C1", "C1_C2", "C1_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
          fig_C1.update_traces(fill='toself',)
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Cdjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_C1.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))



          chart_C1 = fig_C1.to_html(config = {'displayModeBar': False})
          resultsC1 = resultsC1.to_html()
          return render(request, 'questions/poleC/resultsCdetails.html', { 'resultsC1' : resultsC1, 'chart_C1' : chart_C1})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleC/resultsCdetails.html', {'info' : info})


def resultatsC2(request):
     user_connected=request.user.id
     if PostC2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC2_C3.objects.filter(created_by_id=user_connected).all().exists():
          resC2_C1 = pd.DataFrame(list(PostC2_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'C2_C1').order_by('id').reverse()[:1]))
          resC2_C2 = pd.DataFrame(list(PostC2_C2.objects.filter(created_by_id=user_connected).values('C2_C2').order_by('id').reverse()[:1]))
          resC2_C3 = pd.DataFrame(list(PostC2_C3.objects.filter(created_by_id=user_connected).values('C2_C3', 'time').order_by('id').reverse()[:1]))
          resC2_C3['time'] = resC2_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsC2 = pd.merge(resC2_C1, resC2_C2, how='cross')
          resultsC2 = pd.merge(resultsC2, resC2_C3, how='cross')
          df_result_C2=resultsC2[["C2_C1", "C2_C2", "C2_C3",]]
          df_result_C2.columns=["C2_C1", "C2_C2", "C2_C3"]
          df_result_C2 = df_result_C2.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rC2=df_result_C2.iloc[0]
          fig_C2= px.line_polar(df_result_C2,r=rC2, theta=["C2_C1", "C2_C2", "C2_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
          fig_C2.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_C2.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          chart_C2 = fig_C2.to_html(config = {'displayModeBar': False})
          resultsC2 = resultsC2.to_html()
          return render(request, 'questions/poleC/resultsCdetails.html', { 'resultsC2' : resultsC2, 'chart_C2' : chart_C2})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleC/resultsCdetails.html', {'info' : info})



def resultatsC3(request):
     user_connected=request.user.id
     if PostC3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC3_C3.objects.filter(created_by_id=user_connected).all().exists():
          resC3_C1 = pd.DataFrame(list(PostC3_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'C3_C1').order_by('id').reverse()[:1]))
          resC3_C2 = pd.DataFrame(list(PostC3_C2.objects.filter(created_by_id=user_connected).values('C3_C2').order_by('id').reverse()[:1]))
          resC3_C3 = pd.DataFrame(list(PostC3_C3.objects.filter(created_by_id=user_connected).values('C3_C3', 'time').order_by('id').reverse()[:1]))
          resC3_C3['time'] = resC3_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsC3 = pd.merge(resC3_C1, resC3_C2, how='cross')
          resultsC3 = pd.merge(resultsC3, resC3_C3, how='cross')
          df_result_C3=resultsC3[["C3_C1", "C3_C3", "C3_C3",]]
          df_result_C3.columns=["C3_C1", "C3_C3", "C3_C3"]
          df_result_C3 = df_result_C3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rC3=df_result_C3.iloc[0]
          fig_C3= px.line_polar(df_result_C3,r=rC3, theta=["C3_C1", "C3_C2", "C3_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
          fig_C3.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_C3.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          chart_C3 = fig_C3.to_html(config = {'displayModeBar': False})
          resultsC3 = resultsC3.to_html()
          return render(request, 'questions/poleC/resultsCdetails.html', { 'resultsC3' : resultsC3, 'chart_C3' : chart_C3})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleC/resultsCdetails.html', {'info' : info})

def resultatsC4(request):
     user_connected=request.user.id
     if PostC4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC4_C3.objects.filter(created_by_id=user_connected).all().exists():
          resC4_C1 = pd.DataFrame(list(PostC4_C1.objects.filter(created_by_id=user_connected).values('created_by_id', 'C4_C1').order_by('id').reverse()[:1]))
          resC4_C2 = pd.DataFrame(list(PostC4_C2.objects.filter(created_by_id=user_connected).values('C4_C2').order_by('id').reverse()[:1]))
          resC4_C3 = pd.DataFrame(list(PostC4_C3.objects.filter(created_by_id=user_connected).values('C4_C3', 'time').order_by('id').reverse()[:1]))
          resC4_C3['time'] = resC4_C3['time'].dt.strftime('%Y/%m/%d %H:%M:%S')
          resultsC4 = pd.merge(resC4_C1, resC4_C2, how='cross')
          resultsC4 = pd.merge(resultsC4, resC4_C3, how='cross')
          df_result_C4=resultsC4[["C4_C1", "C4_C2", "C4_C3",]]
          df_result_C4.columns=["C4_C1", "C4_C2", "C4_C3"]
          df_result_C4 = df_result_C4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          rC4=df_result_C4.iloc[0]
          fig_C4= px.line_polar(df_result_C4,r=rC4, theta=["C4_C1", "C4_C2", "C4_C3"], direction='clockwise', start_angle=70, line_close=True, width=460, height=460,color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
          fig_C4.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_C4.update_layout(
               xaxis_range=[0,4],
               polar=dict(
                    radialaxis=dict(range=[0, 4],
                         visible=True,
                         tickvals=fixed_axis_values,
                         ticktext=fixed_axis_labels,
                         autorange = None

            )
        ))

          chart_C4 = fig_C4.to_html(config = {'displayModeBar': False})
          resultsC4 = resultsC4.to_html()
          return render(request, 'questions/poleC/resultsCdetails.html', { 'resultsC4' : resultsC4, 'chart_C4' : chart_C4})
     else :
          info = "Les résultats seront disponible après avoir remplie la section correspondante"
          return render(request, 'questions/poleC/resultsCdetails.html', {'info' : info})


###################Admin#############################################

@user_passes_test(lambda u: u.is_superuser)
def all_userview(request):
    userdata = Utilisateur_infos.objects.all().values()
    template = loader.get_template('userview.html')
    context = { 'Utilisateur_liste' : userdata}
    return HttpResponse(template.render(context,request))

@user_passes_test(lambda u: u.is_superuser)
def resultats_all(request):
    if PostA1_C1.objects.all().exists() and PostA1_C2.objects.all().exists() and PostA1_C3.objects.all().exists() and PostA2_C1.objects.all().exists() and PostA2_C2.objects.all().exists() and PostA2_C3.objects.all().exists() \
     and PostA3_C1.objects.all().exists() and PostA3_C2.objects.all().exists() and PostA3_C3.objects.all().exists() and \
     PostA4_C1.objects.all().exists() and PostA4_C2.objects.all().exists() and PostA4_C3.objects.all().exists() and \
     PostA4_C1.objects.all().exists() and PostA5_C2.objects.all().exists() and PostA5_C3.objects.all().exists() and \
     PostA6_C1.objects.all().exists() and PostA6_C2.objects.all().exists() and PostA6_C3.objects.all().exists():
         resA1_C1 = pd.DataFrame(list(PostA1_C1.objects.all().values('created_by', 'A1_C1')))
         resA1_C2 = pd.DataFrame(list(PostA1_C2.objects.all().values('A1_C2')))
         resA1_C3 = pd.DataFrame(list(PostA1_C3.objects.all().values('A1_C3')))
         resultsA1 = pd.merge(resA1_C1, resA1_C2, how='cross')
         resultsA1 = pd.merge(resultsA1, resA1_C3, how='cross')

         resultsallA1 = resultsA1.to_dict(orient='records')

         resA2_C1 = pd.DataFrame(list(PostA2_C1.objects.all().values('created_by', 'A2_C1')))
         resA2_C2 = pd.DataFrame(list(PostA2_C2.objects.all().values('A2_C2')))
         resA2_C3 = pd.DataFrame(list(PostA2_C3.objects.all().values('A2_C3')))
         resultsA2 = pd.merge(resA2_C1, resA2_C2, how='cross')
         resultsA2 = pd.merge(resultsA2, resA2_C3, how='cross')

         resultsallA2 = resultsA2.to_dict(orient='records')



         return render(request, 'data_A.html', {'resultsallA1' : resultsallA1,'resultsallA2' : resultsallA2})
    else :
        info = "Les résultats seront disponible après avoir intégrer des données"
        return render(request, 'data_A.html', {'info' : info})


####################PDF tous les résultats##################################
def generate_All_pdf(request):
     user_connected=request.user.id
     if PostA1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA1_C3.objects.filter(created_by_id=user_connected).all().exists() and PostA2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA2_C3.objects.filter(created_by_id=user_connected).all().exists() \
          and PostA3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA3_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostA4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA4_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostA5_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA5_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA5_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostA6_C1.objects.filter(created_by_id=user_connected).all().exists() and PostA6_C2.objects.filter(created_by_id=user_connected).all().exists() and PostA6_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostB1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB1_C3.objects.filter(created_by_id=user_connected).all().exists() and PostB2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB2_C3.objects.filter(created_by_id=user_connected).all().exists() \
          and PostB3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB3_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostB4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostB4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostB4_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostC1_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC1_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC1_C3.objects.filter(created_by_id=user_connected).all().exists() and PostC2_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC2_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC2_C3.objects.filter(created_by_id=user_connected).all().exists() \
          and PostC3_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC3_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC3_C3.objects.filter(created_by_id=user_connected).all().exists() and \
          PostC4_C1.objects.filter(created_by_id=user_connected).all().exists() and PostC4_C2.objects.filter(created_by_id=user_connected).all().exists() and PostC4_C3.objects.filter(created_by_id=user_connected).all().exists():


          resA1_C1 = pd.DataFrame(list(PostA1_C1.objects.filter(created_by_id=user_connected).values('A1_C1').order_by('id').reverse()[:1]))
          resA1_C2 = pd.DataFrame(list(PostA1_C2.objects.filter(created_by_id=user_connected).values('A1_C2').order_by('id').reverse()[:1]))
          resA1_C3 = pd.DataFrame(list(PostA1_C3.objects.filter(created_by_id=user_connected).values('A1_C3',).order_by('id').reverse()[:1]))

          resultsA1 = pd.merge(resA1_C1, resA1_C2, how='cross')
          resultsA1 = pd.merge(resultsA1, resA1_C3, how='cross')
          df_result_A1=resultsA1[["A1_C1", "A1_C2", "A1_C3",]]
          df_result_A1.columns=["A1_C1", "A1_C2", "A1_C3"]
          df_result_A1 = df_result_A1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resA2_C1 = pd.DataFrame(list(PostA2_C1.objects.filter(created_by_id=user_connected).values('A2_C1').order_by('id').reverse()[:1]))
          resA2_C2 = pd.DataFrame(list(PostA2_C2.objects.filter(created_by_id=user_connected).values('A2_C2').order_by('id').reverse()[:1]))
          resA2_C3 = pd.DataFrame(list(PostA2_C3.objects.filter(created_by_id=user_connected).values('A2_C3',).order_by('id').reverse()[:1]))
          resultsA2 = pd.merge(resA2_C1, resA2_C2, how='cross')
          resultsA2 = pd.merge(resultsA2, resA2_C3, how='cross')
          df_result_A2=resultsA2[["A2_C1", "A2_C2", "A2_C3",]]
          df_result_A2.columns=["A2_C1", "A2_C2", "A2_C3"]
          df_result_A2 = df_result_A2.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resA3_C1 = pd.DataFrame(list(PostA3_C1.objects.filter(created_by_id=user_connected).values('A3_C1').order_by('id').reverse()[:1]))
          resA3_C2 = pd.DataFrame(list(PostA3_C2.objects.filter(created_by_id=user_connected).values('A3_C2').order_by('id').reverse()[:1]))
          resA3_C3 = pd.DataFrame(list(PostA3_C3.objects.filter(created_by_id=user_connected).values('A3_C3',).order_by('id').reverse()[:1]))
          resultsA3 = pd.merge(resA3_C1, resA3_C2, how='cross')
          resultsA3 = pd.merge(resultsA3, resA3_C3, how='cross')
          df_result_A3=resultsA3[["A3_C1", "A3_C2", "A3_C3",]]
          df_result_A3.columns=["A3_C1", "A3_C2", "A3_C3"]
          df_result_A3 = df_result_A3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resA4_C1 = pd.DataFrame(list(PostA4_C1.objects.filter(created_by_id=user_connected).values('A4_C1').order_by('id').reverse()[:1]))
          resA4_C2 = pd.DataFrame(list(PostA4_C2.objects.filter(created_by_id=user_connected).values('A4_C2').order_by('id').reverse()[:1]))
          resA4_C3 = pd.DataFrame(list(PostA4_C3.objects.filter(created_by_id=user_connected).values('A4_C3',).order_by('id').reverse()[:1]))
          resultsA4 = pd.merge(resA4_C1, resA4_C2, how='cross')
          resultsA4 = pd.merge(resultsA4, resA4_C3, how='cross')
          df_result_A4=resultsA4[["A4_C1", "A4_C2", "A4_C3",]]
          df_result_A4.columns=["A4_C1", "A4_C2", "A4_C3"]
          df_result_A4 = df_result_A4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resA5_C1 = pd.DataFrame(list(PostA5_C1.objects.filter(created_by_id=user_connected).values('A5_C1').order_by('id').reverse()[:1]))
          resA5_C2 = pd.DataFrame(list(PostA5_C2.objects.filter(created_by_id=user_connected).values('A5_C2').order_by('id').reverse()[:1]))
          resA5_C3 = pd.DataFrame(list(PostA5_C3.objects.filter(created_by_id=user_connected).values('A5_C3').order_by('id').reverse()[:1]))

          resultsA5 = pd.merge(resA5_C1, resA5_C2, how='cross')
          resultsA5 = pd.merge(resultsA5, resA5_C3, how='cross')
          df_result_A5=resultsA5[["A5_C1", "A5_C2", "A5_C3",]]
          df_result_A5.columns=["A5_C1", "A5_C2", "A5_C3"]
          df_result_A5 = df_result_A4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resA6_C1 = pd.DataFrame(list(PostA6_C1.objects.filter(created_by_id=user_connected).values('A6_C1').order_by('id').reverse()[:1]))
          resA6_C2 = pd.DataFrame(list(PostA6_C2.objects.filter(created_by_id=user_connected).values('A6_C2').order_by('id').reverse()[:1]))
          resA6_C3 = pd.DataFrame(list(PostA6_C3.objects.filter(created_by_id=user_connected).values('A6_C3').order_by('id').reverse()[:1]))
          resultsA6 = pd.merge(resA6_C1, resA6_C2, how='cross')
          resultsA6 = pd.merge(resultsA6, resA6_C3, how='cross')
          df_result_A6=resultsA6[["A6_C1", "A6_C2", "A6_C3",]]
          df_result_A6.columns=["A6_C1", "A6_C2", "A6_C3"]
          df_result_A6 = df_result_A4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])


          resultallA=pd.concat([df_result_A1, df_result_A2, df_result_A3, df_result_A4, df_result_A5, df_result_A6], axis=1)
          df_result_all = resultallA.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r_all=df_result_all.iloc[0]
          fig_all= px.line_polar(df_result_all,r=r_all,theta=["A1_C1", "A1_C2", "A1_C3","A2_C1", "A2_C2", "A2_C3","A3_C1", "A3_C2", "A3_C3","A4_C1", "A4_C2", "A4_C3", "A5_C1", "A5_C2", "A5_C3", "A6_C1", "A6_C2", "A6_C3"], direction='clockwise', start_angle=70, line_close=True,line_shape='spline',)
          fig_all.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_all.update_layout(
                    xaxis_range=[0,4],
                    title="Pôle A Conseiller / Développer",
                    margin=dict(t=110),
                    font=dict(
                    family="Helvetica, sans-serif",size=22,color="black"),
                    polar=dict(
                         radialaxis=dict(range=[0, 4],
                              visible=True,
                              tickvals=fixed_axis_values,
                              ticktext=fixed_axis_labels,
                              autorange = None)))

          resB1_C1 = pd.DataFrame(list(PostB1_C1.objects.filter(created_by_id=user_connected).values('B1_C1').order_by('id').reverse()[:1]))
          resB1_C2 = pd.DataFrame(list(PostB1_C2.objects.filter(created_by_id=user_connected).values('B1_C2').order_by('id').reverse()[:1]))
          resB1_C3 = pd.DataFrame(list(PostB1_C3.objects.filter(created_by_id=user_connected).values('B1_C3',).order_by('id').reverse()[:1]))

          resultsB1 = pd.merge(resB1_C1, resB1_C2, how='cross')
          resultsB1 = pd.merge(resultsB1, resB1_C3, how='cross')
          df_result_B1=resultsB1[["B1_C1", "B1_C2", "B1_C3",]]
          df_result_B1.columns=["B1_C1", "B1_C2", "B1_C3"]
          df_result_B1 = df_result_B1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resB2_C1 = pd.DataFrame(list(PostB2_C1.objects.filter(created_by_id=user_connected).values('B2_C1').order_by('id').reverse()[:1]))
          resB2_C2 = pd.DataFrame(list(PostB2_C2.objects.filter(created_by_id=user_connected).values('B2_C2').order_by('id').reverse()[:1]))
          resB2_C3 = pd.DataFrame(list(PostB2_C3.objects.filter(created_by_id=user_connected).values('B2_C3',).order_by('id').reverse()[:1]))
          resultsB2 = pd.merge(resB2_C1, resB2_C2, how='cross')
          resultsB2 = pd.merge(resultsB2, resB2_C3, how='cross')
          df_result_B2=resultsB2[["B2_C1", "B2_C2", "B2_C3",]]
          df_result_B2.columns=["B2_C1", "B2_C2", "B2_C3"]
          df_result_B2 = df_result_B2.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resB3_C1 = pd.DataFrame(list(PostB3_C1.objects.filter(created_by_id=user_connected).values('B3_C1').order_by('id').reverse()[:1]))
          resB3_C2 = pd.DataFrame(list(PostB3_C2.objects.filter(created_by_id=user_connected).values('B3_C2').order_by('id').reverse()[:1]))
          resB3_C3 = pd.DataFrame(list(PostB3_C3.objects.filter(created_by_id=user_connected).values('B3_C3',).order_by('id').reverse()[:1]))
          resultsB3 = pd.merge(resB3_C1, resB3_C2, how='cross')
          resultsB3 = pd.merge(resultsB3, resB3_C3, how='cross')
          df_result_B3=resultsB3[["B3_C1", "B3_C2", "B3_C3",]]
          df_result_B3.columns=["B3_C1", "B3_C2", "B3_C3"]
          df_result_B3 = df_result_B3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resB4_C1 = pd.DataFrame(list(PostB4_C1.objects.filter(created_by_id=user_connected).values('B4_C1').order_by('id').reverse()[:1]))
          resB4_C2 = pd.DataFrame(list(PostB4_C2.objects.filter(created_by_id=user_connected).values('B4_C2').order_by('id').reverse()[:1]))
          resB4_C3 = pd.DataFrame(list(PostB4_C3.objects.filter(created_by_id=user_connected).values('B4_C3',).order_by('id').reverse()[:1]))
          resultsB4 = pd.merge(resB4_C1, resB4_C2, how='cross')
          resultsB4 = pd.merge(resultsB4, resB4_C3, how='cross')
          df_result_B4=resultsB4[["B4_C1", "B4_C2", "B4_C3",]]
          df_result_B4.columns=["B4_C1", "B4_C2", "B4_C3"]
          df_result_B4 = df_result_B4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])


          resultallB=pd.concat([df_result_B1, df_result_B2, df_result_B3, df_result_B4], axis=1)
          df_result_allB = resultallB.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r_allB=df_result_allB.iloc[0]
          fig_allB= px.line_polar(df_result_allB,r=r_allB,theta=["B1_C1", "B1_C2", "B1_C3","B2_C1", "B2_C2", "B2_C3","B3_C1", "B3_C2", "B3_C3","B4_C1", "B4_C2", "B4_C3"], direction='clockwise', start_angle=70, line_close=True,line_shape='spline',color_discrete_sequence=["orange","green", "blue", "goldenrod", "magenta"])
          fig_allB.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_allB.update_layout(
                    xaxis_range=[0,4],
                    title="Pôle B Concevoir / Innover",
                    margin=dict(t=110),
                    font=dict(
                    family="Helvetica, sans-serif",size=22,color="black"),
                    polar=dict(
                         radialaxis=dict(range=[0, 4],
                              visible=True,
                              tickvals=fixed_axis_values,
                              ticktext=fixed_axis_labels,
                              autorange = None)))

          resC1_C1 = pd.DataFrame(list(PostC1_C1.objects.filter(created_by_id=user_connected).values('C1_C1').order_by('id').reverse()[:1]))
          resC1_C2 = pd.DataFrame(list(PostC1_C2.objects.filter(created_by_id=user_connected).values('C1_C2').order_by('id').reverse()[:1]))
          resC1_C3 = pd.DataFrame(list(PostC1_C3.objects.filter(created_by_id=user_connected).values('C1_C3',).order_by('id').reverse()[:1]))

          resultsC1 = pd.merge(resC1_C1, resC1_C2, how='cross')
          resultsC1 = pd.merge(resultsC1, resC1_C3, how='cross')
          df_result_C1=resultsC1[["C1_C1", "C1_C2", "C1_C3",]]
          df_result_C1.columns=["C1_C1", "C1_C2", "C1_C3"]
          df_result_C1 = df_result_C1.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resC2_C1 = pd.DataFrame(list(PostC2_C1.objects.filter(created_by_id=user_connected).values('C2_C1').order_by('id').reverse()[:1]))
          resC2_C2 = pd.DataFrame(list(PostC2_C2.objects.filter(created_by_id=user_connected).values('C2_C2').order_by('id').reverse()[:1]))
          resC2_C3 = pd.DataFrame(list(PostC2_C3.objects.filter(created_by_id=user_connected).values('C2_C3',).order_by('id').reverse()[:1]))
          resultsC2 = pd.merge(resC2_C1, resC2_C2, how='cross')
          resultsC2 = pd.merge(resultsC2, resC2_C3, how='cross')
          df_result_C2=resultsC2[["C2_C1", "C2_C2", "C2_C3",]]
          df_result_C2.columns=["C2_C1", "C2_C2", "C2_C3"]
          df_result_C2 = df_result_C2.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resC3_C1 = pd.DataFrame(list(PostC3_C1.objects.filter(created_by_id=user_connected).values('C3_C1').order_by('id').reverse()[:1]))
          resC3_C2 = pd.DataFrame(list(PostC3_C2.objects.filter(created_by_id=user_connected).values('C3_C2').order_by('id').reverse()[:1]))
          resC3_C3 = pd.DataFrame(list(PostC3_C3.objects.filter(created_by_id=user_connected).values('C3_C3',).order_by('id').reverse()[:1]))
          resultsC3 = pd.merge(resC3_C1, resC3_C2, how='cross')
          resultsC3 = pd.merge(resultsC3, resC3_C3, how='cross')
          df_result_C3=resultsC3[["C3_C1", "C3_C2", "C3_C3",]]
          df_result_C3.columns=["C3_C1", "C3_C2", "C3_C3"]
          df_result_C3 = df_result_C3.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resC4_C1 = pd.DataFrame(list(PostC4_C1.objects.filter(created_by_id=user_connected).values('C4_C1').order_by('id').reverse()[:1]))
          resC4_C2 = pd.DataFrame(list(PostC4_C2.objects.filter(created_by_id=user_connected).values('C4_C2').order_by('id').reverse()[:1]))
          resC4_C3 = pd.DataFrame(list(PostC4_C3.objects.filter(created_by_id=user_connected).values('C4_C3',).order_by('id').reverse()[:1]))
          resultsC4 = pd.merge(resC4_C1, resC4_C2, how='cross')
          resultsC4 = pd.merge(resultsC4, resC4_C3, how='cross')
          df_result_C4=resultsC4[["C4_C1", "C4_C2", "C4_C3",]]
          df_result_C4.columns=["C4_C1", "C4_C2", "C4_C3"]
          df_result_C4 = df_result_C4.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])

          resultallC=pd.concat([df_result_C1, df_result_C2, df_result_C3, df_result_C4], axis=1)
          df_result_allC = resultallC.replace(["N_S_P","Degre_1","Degre_2","Degre_3", "Degre_4"], [0, 1, 2, 3, 4])
          r_allC=df_result_allC.iloc[0]
          fig_allC= px.line_polar(df_result_allC,r=r_allC,theta=["C1_C1", "C1_C2", "C1_C3","C2_C1", "C2_C2", "C2_C3","C3_C1", "C3_C2", "C3_C3","C4_C1", "C4_C2", "C4_C3"], direction='clockwise', start_angle=70, line_close=True,line_shape='spline',color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
          fig_allC.update_traces(fill='toself')
          value=[1,2,3,4,]
          max_value = max(value)
          fixed_axis_values = np.linspace(0, max_value, 5)  # Adjust 5 to change the number of ticks
          fixed_axis_labels = [f'{val:.0f}' for val in fixed_axis_values]
          fig_allC.update_layout(
                    xaxis_range=[0,4],
                    title="Pôle C Piloter / Animer",
                    font=dict(
                    family="Helvetica, sans-serif",size=22,color="black"),
                    margin=dict(t=110),
                    polar=dict(
                         radialaxis=dict(range=[0, 4],
                              visible=True,
                              tickvals=fixed_axis_values,
                              ticktext=fixed_axis_labels,
                              autorange = None)))

          polar_charts = []
          polar_charts.append(fig_all)

          polar_charts.append(fig_allB)

          polar_charts.append(fig_allC)

          buffer = BytesIO()
          doc = SimpleDocTemplate(buffer, pagesize=letter)
          styles = getSampleStyleSheet()
          elements = []

          elements.append(Paragraph("Les résultats sous forme de diagrammes", styles['Title']))

          elements.append(Spacer(1, 12))  # Add some space

          cm_to_inches = 1 / 2.54  # 1 cm = 1/2.54 inches
          cm_to_pixels = 72 / 2.54  # 1 inch = 72 pixels
          width_in_pixels = int(10 * cm_to_pixels)
          height_in_pixels = int(7* cm_to_pixels)


          for chart in polar_charts:
               chart_bytes = chart.to_image(format="png")
               img = BytesIO(chart_bytes)
               elements.append(Image(img,  width=width_in_pixels, height=height_in_pixels))
          doc.build(elements)
          pdf = buffer.getvalue()
          buffer.close()
          response = HttpResponse(content_type='application/pdf')
          response['Content-Disposition'] = 'attachment; filename="exportallpoles.pdf"'
          response.write(pdf)
          return response
     else :

        return render(request, 'cartographieparcours.html',)



###################Delete Button##################################
from django.contrib.auth.models import User
@login_required
def erase_user_data(user_id):
    try:
        # Get the user object
        user = User.objects.get(id=user_id)

        # Optionally, delete related data (e.g., profile, related objects)
        # user.profile.delete() # If you have a related profile model

        # Delete the user
        user.delete()

        return True, "User data erased successfully."
    except User.DoesNotExist:
        return False, "User does not exist."
    except Exception as e:
        return False, f"An error occurred: {str(e)}"

#############################"
