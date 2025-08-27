from django.shortcuts import render
from .models import MadLibTemplate
from .forms import DynamicMadLibForm

# Create your views here.
def home(request):
    madlibs = MadLibTemplate.objects.all()
    return render(request, 'madlibs/home.html', {'madlibs': madlibs})


def madlib_form(request, id):
    madlib = MadLibTemplate.objects.get(pk=id)

    if request.method == "POST":
        form = DynamicMadLibForm(madlib.fields, request.POST)
        if form.is_valid():
            user_data = form.cleaned_data

            highlighted_data = {
                key: f'<span class="badge bg-primary fs-4 p-2">{value}</span>'
                for key, value in user_data.items()
            }

            story = madlib.text.format(**highlighted_data)
            return render(request, 'madlibs/story_result.html', {'story': story, "madlib": madlib})

    else:
        form = DynamicMadLibForm(madlib.fields)

    return render(request, 'madlibs/madlib_form.html', {'madlib': madlib, 'form': form})


def about(request):
    return render(request, 'madlibs/about.html')