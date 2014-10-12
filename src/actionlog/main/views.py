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
    # Get statistical items: total-count, first entry, last entry
    num_entries = models.LogEntry.objects.count()

    entry_first = models.LogEntry.objects.order_by("date_entry")[0] if num_entries else None
    entry_most_recent = models.LogEntry.objects.order_by("-date_entry")[0] if num_entries else None

    # Get number of consecutive days with entries
    consecutive_entries = 0
    date_cursor = datetime.date.today()
    for entry in models.LogEntry.objects.order_by("-date_entry"):
        if entry.date_entry == date_cursor:
            consecutive_entries += 1
            date_cursor -= datetime.timedelta(days=1)
        else:
            break

    # Get items for this month
    today = datetime.date.today()
    first_this_month = datetime.date(today.year, today.month, 1)
    entries = list(models.LogEntry.objects.filter(date_entry__gte=first_this_month).order_by("-date_entry"))

    # Sort entries into action groups
    groups = {}
    for entry in entries:
        if entry.action in groups:
            groups[entry.action].append(entry)
        else:
            groups[entry.action] = [entry]

    return render(request, 'index.html', {
        "entry_first": entry_first,
        "entry_most_recent": entry_most_recent,
        "entry_count": num_entries,
        "consecutive_entries": consecutive_entries,
        "entries": entries
    })
