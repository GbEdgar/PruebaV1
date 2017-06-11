# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from __future__ import absolute_import

from django.shortcuts import render

# Create your views here.
def home(request):
     context=locals();
     template='home.html'
     return render(request,template,context)
