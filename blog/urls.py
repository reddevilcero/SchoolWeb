from django.urls import path
from . import views

urlpatterns = [
    # url path for services app
    path('', views.PostListView.as_view(), name="blog"),
    path('<int:pk>/<slug:post_slug>/', views.PostCountHitDetailView.as_view(),
         name="post"),
    path('category/<int:category_id>/<slug:category_slug>', views.category,
         name='category'),
]

