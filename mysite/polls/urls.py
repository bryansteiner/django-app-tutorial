from django.urls import path
from . import views
from . import views_generic

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    # Generic views
    path('', views_generic.IndexView.as_view(), name='index'),
    path('<int:pk>/', views_generic.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views_generic.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views_generic.vote, name='vote') # not generic
]