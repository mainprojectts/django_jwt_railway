from django.urls import path
from . import views

urlpatterns = [
    path("notes/",views.NoteListCreate.as_view(),name="note-list"),
    path("notesarray/",views.NoteListarrayCreate.as_view(),name="note-listarray"),
    path("notes/delete/<int:pk>/",views.NoteDelete.as_view(),name="delete-note"),
    path("category/",views.Createcategory.as_view(),name="category"),
    path("brand/",views.CreateBrand.as_view(),name="brand"),
    path("product/",views.CreateProduct.as_view(),name="product"),
    path("cart/",views.Addtocart.as_view(),name="cart"),
]
