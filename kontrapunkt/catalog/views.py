from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic


def index(request):
    """View function for home page of site."""

#     # Generate counts of some of the main objects
#     num_books = Book.objects.all().count()
#     num_instances = BookInstance.objects.all().count()
#     
#     # Available books (status = 'a')
#     num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_country = Country.objects.count()
    num_composer = Composer.objects.count()
    num_compositioncategory = CompositionCategory.objects.count()
    
#     # Number of visits to this view, as counted in the session variable.
#     num_visits = request.session.get('num_visits', 0)
#     request.session['num_visits'] = num_visits + 1

    context = {
#         'num_books': num_books,
#         'num_instances': num_instances,
#         'num_instances_available': num_instances_available,
        'num_country': num_country,
        'num_composer': num_composer,
        'num_compositioncategory': num_compositioncategory,
#         'num_visits': num_visits,
    }    
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# ===== Country =====
from catalog.models import Country

class CountryListView(generic.ListView):
    model = Country
#    paginate_by = 2
    
class CountryDetailView(generic.DetailView):
    model = Country    
    
class CountryCreate(CreateView):
    model = Country
    fields = '__all__'
#    initial = {'date_of_death': '05/01/2018'}

class CountryUpdate(UpdateView):
    model = Country
    fields = '__all__'
#    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class CountryDelete(DeleteView):
    model = Country
    success_url = reverse_lazy('country_list')

# ===== Compositioncategory ===== 
from catalog.models import CompositionCategory

# ===== Composer =====
from catalog.models import Composer

class ComposerListView(generic.ListView):
    model = Composer
#    paginate_by = 2
    
class ComposerDetailView(generic.DetailView):
    model = Composer    
    
class ComposerCreate(CreateView):
    model = Composer
    fields = '__all__'
#    initial = {'date_of_death': '05/01/2018'}

class ComposerUpdate(UpdateView):
    model = Composer
    fields = '__all__'
#    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class ComposerDelete(DeleteView):
    model = Composer
    success_url = reverse_lazy('composer_list')
    
# ===== Composition =====
from catalog.models import Composition

class CompositionListView(generic.ListView):
    model = Composition
#    paginate_by = 2
    
class CompositionDetailView(generic.DetailView):
    model = Composition    
    
class CompositionCreate(CreateView):
    model = Composition
    fields = '__all__'
#    initial = {'date_of_death': '05/01/2018'}

class CompositionUpdate(UpdateView):
    model = Composition
    fields = '__all__'
#    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class CompositionDelete(DeleteView):
    model = Composition
    success_url = reverse_lazy('composition_list')
    