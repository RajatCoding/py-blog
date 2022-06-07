from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import  render
from blog.models import Post
from django.views.generic import CreateView,ListView,UpdateView, DetailView,DeleteView


# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {'post':posts}
    return render(request, 'home.html', context)

#About Us
def aboutus(request):
    posts = Post.objects.all()
    context = {'post':posts}
    return render(request, 'aboutus.html', context)


def dashboard(request):

    posts = Post.objects.filter(author_id = request.user.id) 
    context = {'posts':posts}

    return render(request, 'dashboard.html', context)


class CreatePost(CreateView):
    model = Post
    fields = ['title', 'description']
    template_name = 'createpost.html'
    success_url = '/dashboard'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)






class PostUpdate(SuccessMessageMixin, UpdateView):
    model = Post
    fields = ['title', 'description']
    template_name = 'updatepost.html'
    success_url = '/dashboard'
    success_message = 'Post updated successfully'



class PostDelete(SuccessMessageMixin,DeleteView):
    model = Post
    template_name = 'deletepost.html'
    context_object_name = 'object'
    success_url = '/dashboard'
    success_message = 'Post deleted successfully'



class PostDetail(DetailView):
    model = Post
    template_name = 'detailpost.html'
    context_object_name = 'post'