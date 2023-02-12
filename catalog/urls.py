from django.urls import path
from . import views
from catalog.views import BookCreate, BookDetail, SignUpView, CheckedOutBooksByUserView
app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('create-book/', BookCreate.as_view(), name='create_book'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('my_view/', views.my_view, name="my_view"),
    path('signup', SignUpView.as_view(), name="signup"),
    path('profile/', CheckedOutBooksByUserView.as_view(), name="profile")
]
