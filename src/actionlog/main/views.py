from traceback import format_exc

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.base import View
from django.shortcuts import render_to_response, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import auth
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

import datetime
import time
from pprint import pprint, pformat

import models

def index(request):
    entries = list(models.LogEntry.objects.order_by("-date_entry"))

    entry_first = entries[-1] if len(entries) else None

    print entries
    
    return render(request, 'index.html', {
        "entry_first": entry_first,
        "entry_count": len(entries),
        "entries": entries
    })
