from django.views import generic
from .models import Visitation
from django.core.urlresolvers import resolve
import datetime

url_names = ['index', 'treatment', 'voksne', 'prices', 'about', 'contact', 'fastsittende', 'retensjon', 'ganeplate', 'nattboyle', 'vekstplate']
visitation_names = ['Home', 'Behandling', 'Voksne', 'Priser', 'Om Oss', 'Kontakt', 'Fastsittende', 'Retensjon', 'Ganeplate', 'Nattboyle', 'Vekstplate']
headers = ['Reguleringstannlegene', 'Behandling', 'Voksne', 'Priser', 'Om oss', 'Kontakt']

def newVisitation(page_name):

    new_visitation = Visitation(date_visited=datetime.datetime.now(), page_name=page_name)
    new_visitation.save()

class IndexView(generic.ListView):

    model = Visitation
    template_name = 'home/index.html'

    id = 5
    context_object_name = 'query_set'

    def get_queryset(self):

        #newVisitation(visitation_names[url_names.index(resolve(self.request.path_info).url_name)])
        #return Visitation.objects
        return [headers[url_names.index(resolve(self.request.path_info).url_name)]]

class TreatmentView(IndexView):

    template_name = 'home/treatment.html'
    id = 0


class VoksneView(IndexView):

    template_name = 'home/voksne.html'
    id = 1


class PriceView(IndexView):

    template_name = 'home/prices.html'
    id = 2


class AboutView(IndexView):

    template_name = 'home/about.html'
    id = 3


class ContactView(IndexView):

    template_name = 'home/contact.html'
    id = 4

