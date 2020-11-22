from django.shortcuts import render
from django.http import Http404
from markdown2 import Markdown

from . import util


def index(request):
    return render(
        request, "encyclopedia/index.html", {"entries": util.list_entries()}
    )


def wiki(request, entry):
    if entry not in util.list_entries():
        raise Http404
    content = util.get_entry(entry)
    return render(
        request,
        "encyclopedia/wiki.html",
        {"title": entry, "content": Markdown().convert(content)},
    )


def handler404(request, *args):
    return render(request, "404.html", {})
