from django.shortcuts import render
from blog.forms import CreatePostForm
from blog.models import BlogModel
from django.http import HttpResponseRedirect

def index(request):
    val = BlogModel.objects.order_by('title')
    context = {'key':val}
    return render(request,'blog/index.html',context)

def createPostView(request):
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print('Error')
    index(request)
    return render(request,'blog/create.html',{'key':form})
