from django.shortcuts import render

index_dict = {'title':'Home', 'header':'Welcome!', 'text':'Hello World', 'number':100}
other_dict = {'title':'Other', 'header':'Welcome to Other!'}
relative_dict = {'title':'Relative', 'header':'Welcome to Relative!'}

# Create your views here.
def index(request):
    # context_dict = {'text':'Hello World', 'number':100}
    return render(request,'basic_app/index.html', context=index_dict)

def other(request):
    return render(request,'basic_app/other.html', context=other_dict)

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html', context=relative_dict)