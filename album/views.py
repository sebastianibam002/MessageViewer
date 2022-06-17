from django.shortcuts import render
from .forms import DateForm, LookDate, DateEditForm
from .models import DateIdeas

# Create your views here.
def main(request):
    show_third_form = "not-visible"
    date_idea = None 
    # if this is a POST request we need to process the form data
    # get all title names of django


    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DateForm(request.POST)
        # other option of form
        look_form = LookDate(request.POST)
        # date edit form
        edit_form = DateEditForm(request.POST, request.FILES)
        print(edit_form.errors)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            form.save()
            form = DateForm()
        elif look_form.is_valid():
            elements = DateIdeas.objects.filter(title=look_form.cleaned_data['title'])
            # retrieve all the information so that we can edit it if we want
            print(elements)
            if elements:
                show_third_form = ""
                date_idea = elements[0]
        if edit_form.is_valid():
            # edit the element and update it on the values
            # meaning that the title exits
            elements = DateIdeas.objects.filter(title=edit_form.cleaned_data['title'])
            date_idea = elements[0]
            print("Edit form is valid")
            print(date_idea)
            if date_idea is not None:
                date_idea.check_done = edit_form.cleaned_data['check_done']
                date_idea.review = edit_form.cleaned_data['review']
                date_idea.date_done = edit_form.cleaned_data['date_done']
                date_idea.image = request.FILES['image']
                # convert the image to a 64bit text fields
                date_idea.save()
                edit_form = LookDate()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DateForm()
        look_form = LookDate()
        edit_form = DateEditForm()

    return render(request, 'album/album.html', {'form': form, 
    'look_form': look_form, 
    'edit_form': edit_form,
    "show_form": show_third_form,
    "dates_collection": DateIdeas.objects.all()

    })
