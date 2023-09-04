from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, ArticleCreate, ArticleUpdate, ArticleDelete


urlpatterns = [ path('', PostList.as_view(), name='post_list'),
                path('<int:pk>', PostDetail.as_view(), name='post_detail'),
                path('create/', PostCreate.as_view(), name='post_create'),
                path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
                path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
                path('articles/create/', ArticleCreate.as_view(), name='article_create'),
                path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_edit'),
                path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
            ]