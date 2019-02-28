from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from .models import Post, Category


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = "post_list"
    paginate_by = 3

    
class PostCountHitDetailView(HitCountDetailView):
    """
    Generic hitcount class based view that will also perform the hitcount
    logic.
    """
    model = Post
    template_name = 'blog/post_details.html'
    count_hit = True


def category(request, category_id, category_slug):
    category = get_object_or_404(Category, id=category_id)
    post_with_category = category.get_posts.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post_with_category, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/category.html',
                  {'posts': posts, 'category': category})
