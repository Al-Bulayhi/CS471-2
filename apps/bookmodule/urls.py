from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('search/', views.search, name="books.search"),
    path('simple/query/', views.simple_query, name='simple_query'),
    path('complex/query/', views.complex_query, name='complex_query'),

    path('html5/links', views.links_page, name='links_page'),
    path('html5/text/formatting', views.text_formatting, name='text_formatting'),
    path('html5/listing', views.nested_listing, name='nested_listing'),
    path('html5/tables/', views.tables_view, name='tables'),

    path('lab8/task1', views.task1_view, name='lab8_task1'),
    path('lab8/task2', views.task2_view, name='lab8_task2'),
    path('lab8/task3', views.task3_view, name='lab8_task3'),
    path('lab8/task4', views.task4_view, name='lab8_task4'),
    path('lab8/task5', views.task5_view, name='lab8_task5'),
    path('lab8/task6', views.task6_view, name='lab8_task6'),
    path('lab8/task7', views.task6_view, name='lab8_task7'),

    path('lab9_part1/list_books/', views.list_books, name='list_books'),
    path('lab9_part1/addbook/', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<int:id>/', views.edit_book, name='edit_book'),
    path('lab9_part1/deletebook/<int:id>/', views.delete_book, name='delete_book'),

    path('lab9_part2/list_books/', views.list_books2, name='list_books2'),
    path('lab9_part2/addbook/', views.add_book2, name='add_book2'),
    path('lab9_part2/editbook/<int:id>/', views.edit_book2, name='edit_book2'),
    path('lab9_part2/deletebook/<int:id>/', views.delete_book2, name='delete_book2'),

    path('lab10/liststudents/', views.liststudents, name="books.list_students"),
    path('lab10/addstudent/', views.addstudent, name="books.addstudent"),
    path('lab10/editstudent/<int:id>', views.editstudent, name="books.editstudent"),
    path('lab10/deletestudent/<int:id>', views.deletestudent, name="books.deletestudent"),

    path('lab10/task2/liststudents/', views.liststudents2, name="books.liststudents2"),
    path('lab10/task2/addstudent/', views.addstudent2, name="books.addstudent2"),
    path('lab10/task2/editstudent/<int:id>', views.editstudent2, name="books.editstudent2"),
    path('lab10/task2/deletestudent/<int:id>', views.deletestudent2, name="books.deletestudent2"),

    path('lab10/task3/listimages/', views.listimages, name="books.listimages"),
    path('lab10/task3/addimage/', views.addimage, name="books.addimage"),
    path('lab10/task3/deleteimage/<int:id>', views.deleteimage, name="books.deleteimage"),
]
