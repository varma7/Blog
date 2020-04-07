from django.shortcuts import render
from blog.forms import CreatePostForm

def index(request):
    return render(request,'blog/index.html')

def createPostView(request):
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error')
    return render(request,'blog/create.html',{'key':form})
