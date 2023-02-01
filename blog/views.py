from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, ContactForm
from django.core.mail import send_mail

def post_share(request, post_id):
        '''
        Post share using Gmail SMTP
        '''
        post = get_object_or_404(Post,
                                id=post_id,
                                status=Post.Status.PUBLISHED
                                )
        # Flag to display success message when the email is successfully sent
        sent = False
     
        if request.method == "POST":
            form = EmailPostForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data

                # Retrieve and build absolute URL path of the post
                post_url = request.build_absolute_uri(
                    post.get_absolute_url()
                )
                subject = f"{cd['name']} recommends you read {post.title}"
                message = f"Read {post.title} at {post_url}\n\n" \
                            f"{cd['name']}\'s (email: f{cd['email']}) \n\n" f"comments: {cd['comments']}"
                send_mail(subject, message, 'user@example-email.com', [cd['email']], fail_silently=False)
                sent = True
        else:
            # Redisplay the form incase validation fails
            form = EmailPostForm()
        return render(request, 'share.html', {
            "post": post,
            "form": form,
            "sent": sent
        })                        



def index(request):
    '''
    Homepage
    '''
    context = Post.published.all()
    return render(
        request,
        'index.html',
        { "posts": context}
    )



def post_list(request):
    '''
    Get all the blogs with published status using the published manager
    '''
    context = Post.published.all()
    # Instantiate the paginator class with 3 per post
    paginator = Paginator(context, 3)

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
        'list.html',
        {"posts": posts}
    )

def post_detail(request, year, month, day, post):
    '''
    Retrieves an object that matches the given parameters
    or an HTTP 404 exception  

    '''

    # Implementing canoical url with post title
    context = get_object_or_404(Post, 
                                status=Post.Status.PUBLISHED, 
                                slug=post,
                                publish__year=year,
                                publish__month=month,
                                publish__day=day
                                )
    return render(
        request,
        'detail.html',
        {"post": context}
    )


        