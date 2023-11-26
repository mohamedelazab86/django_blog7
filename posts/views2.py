
from django.shortcuts import render
from .models import Post



#======================================= creat crud opertions by clas based view   cbv
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

class Post_list(ListView):                # context in templates ---> loop        name of model _ list     post_list   object_list
    model=Post                            # name of templates           name of model_action      post_list


class Post_detail(DetailView):        # CONTEXT name of model      post or object
    model=Post                         # templates name      name of model_ action      post_detail
 

class Create_post(CreateView):
    model=Post
    fields='__all__'
    success_url='/posts/'
    template_name='posts/create.html'
class Update_post(UpdateView):
    model=Post
    fields='__all__'
    success_url='/posts/'
    template_name='posts/edit.html'
class Delete_post(DeleteView):
    model=Post
    template_name='posts/delete.html'
    success_url='/posts/'


 