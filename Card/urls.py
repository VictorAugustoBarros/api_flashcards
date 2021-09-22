"""Flashcards URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Card import views

urlpatterns = [
    path("getCards", views.CardList, name="Listagem dos Cards"),
    path("postCard/", views.CardPost, name="Cadastro de Card"),
    path("putCard/<str:pk>/", views.CardPut, name="Atualizar um Card"),
    path("deleteCard/<str:pk>/", views.CardDelete, name="Deletar um único Card"),
    path("deleteCardsAll/", views.CardDeleteAll, name="deletar todos Cards"),
]
