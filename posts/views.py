from django.views.generic import(
    ListView,
    DetailView,
    CreateView
)
from django.views.generic.edit import(
    UpdateView,
    DeleteView
)
from .models import Post 
from django.urls import reverse_lazy

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name  = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "author", "subtitle", "body"]

class PostUpdateView(UpdateView):
    template_name ="posts/update.html"
    model = Post
    fields = ["title", "author", "subtitle", "body"]

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")

#update view class requires , at min 
# 1 template_name
# 2 model
#3 a list of fields that should be present on the generated form 

# update view will require specific url patter  which should include
#the PK of the instance of the model that we wish to modify

# delete view will also require a PK to be proviced through a url pattern 

#the delete view will need at a min
#template view
#model
#success_url thie should redirect our users after a successful delete