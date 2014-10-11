from traceback import format_exc

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.base import View
from django.shortcuts import render_to_response, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import auth
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from main.models import *

import datetime
import time
from pprint import pprint, pformat

def index(request):
    return render(request, 'index.html')
