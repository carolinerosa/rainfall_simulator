from django.urls import path
from .views import IndexView, VOListView
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(),name='inicio'),
    path('table/', VOListView.as_view(), name = 'table'),
    path('distribespacial/', views.DistribEspacialView.as_view(), name = 'table'),
    path('produtibilidade/', views.ProdutibilidadeView.as_view(), name = 'table'),
    path('regra/', views.RegraView.as_view(), name = 'table'),
    path('tablesJoin/', views.tablesJoin, name='tablesJoin'),
    path('hometeste/', views.hometeste, name='hometeste'),
    path('distribespacial/sendTable/', views.sendTable, name='sendTable'),
    path('produtibilidade/sendTableProdutibilidade/', views.sendTableProdutibilidade, name='sendTableProdutibilidade'),
    path('regra/sendTableRegra/', views.sendTableRegra, name='sendTableRegra'),
    
    
]
