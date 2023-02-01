from django.shortcuts import render
from blog.forms import ContactForm
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post
from static import data

def blog_list_view(request):
    
    posts = Post.published.all()
    return render(
        request, 
        'blog_list_view.html',
        {"posts": posts}
    )

def index(request):
    context = Post.published.all()
    # Instantiate the paginator class with 3 per post
    paginator = Paginator(context, 4)

    # Get the requested page number or use default value of 1 to load the first page
    page_number = request.GET.get('page', 1)

    try:
        # Obtain the objects for the desired page by calling page() 
        posts = paginator.page(page_number)
    except EmptyPage:

        # we page is an empty page, return the last page which is also the total num of pages
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:

        # If string is entered, return page 1
        posts = paginator.page(1)
    return render(
        request,
        'index.html',
        {"posts": posts, "data": data.data['landing_page']}
    )

def about_us(request):
    return render(request,
                "about.html", {})

def contact_us(request):
    '''
    Contact form using Gmail SMTP
    '''
    sent = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            subject = f"A new email from online contact form by f{data['name']}"
            send_mail(subject, data['message'], 'bilalkhan321@gmail.com',['bilalkhan321@gmail.com']
        )
        sent = True
    else:
        # Redisplay the form incase validation fails
        form = ContactForm()
    return render(request, 'contact_form.html', {
        "form": form,
        "sent": sent
    })