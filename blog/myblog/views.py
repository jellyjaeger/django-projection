from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
myposts = []
def home(request):
    return render(request,"myblog/index.html",
    {
        "posts":Post.objects.all(),
        "title":"myblog"
    })
class PostListView(ListView):
    model = Post
    template_name = 'myblog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_time']
    paginate_by = 3 
class PostDetailView(DetailView):
    model = Post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url='/blog/'
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False
class UserPostListView(ListView):
    model = Post
    template_name = 'myblog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_time']
    paginate_by = 3 
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)

def about(request):
    return render(request,"myblog/about.html")

