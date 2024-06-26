from django.shortcuts import render
from django.views import View
from elasticsearch_dsl.query import MultiMatch
from .documents import BookDocument
from .models import Books


class SearchView(View):
    def get(self, request):
        q = request.GET.get('q')
        context = {}
        if q:
            #fuzziness - results similar words as well
            query = MultiMatch(query=q, fields=['title', 'description'], fuzziness="AUTO")
            search = BookDocument.search().query(query)
            context['books'] = search
        return render(request, 'index.html', context)
