from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import CustomerForm, Customer
from django.views import generic


# Create your views here.

def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            customer = form.save(commit=False)
            customer.created = timezone.now()
            customer.save()
            return HttpResponseRedirect('thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomerForm()
    return render(request, 'form/index.html', {'form': form})


class ThanksView(generic.ListView):
    template_name = 'form/thanks.html'
    context_object_name = 'latest_data'

    def get_queryset(self):
        """Return the last form."""
        return Customer.objects.order_by('-created')[:1]
