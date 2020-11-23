from django.shortcuts import render, redirect
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


def search(request):
    query = request.GET.get("q", "")
    if query is None or query == "":
        return render(
            request,
            "encyclopedia/search.html",
            {"found_entries": "", "query": query},
        )

    entries = util.list_entries()

    found_entries = [
        valid_entry
        for valid_entry in entries
        if query.lower() in valid_entry.lower()
    ]
    if len(found_entries) == 1:
        return redirect("wiki", found_entries[0])

    return render(
        request,
        "encyclopedia/search.html",
        {"found_entries": found_entries, "query": query},
    )


def handler404(request, *args):
    return render(request, "404.html", {})
