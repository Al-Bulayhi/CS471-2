from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count, Sum, Avg, Max, Min, Q
from .models import Book,Address,Student, Student2, Images
from .forms import BookForm,StudentForm, StudentForm2, ImageForm
from django.contrib.auth.decorators import login_required




def index(request):
    name = request.GET.get('name') or 'world!'
    return render(request, "template/bookmodule/index.html", {'name': name})

def index2(request, val1 = 0):
    return render('value1 = , ' + str(val1))

def viewbook(request, bookId):
# assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: 
        targetBook = book1
    elif book2['id'] == bookId: 
        targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context) 

def index(request):
    return render(request, "bookmodule/index.html")
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    else:
        return render(request, 'bookmodule/search.html')

mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition= 1)
mybook = Book.objects.create(title = 'Continuous Delivery', author = 'J.Humble and D.Farley', edition = 1)
mybook.save()

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def task1_view(request):
    # Get books with price <= 50
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2_view(request):
    # Filter books with the required conditions:
    # 1. Editions higher than 2
    # 2. Either the title or author contains 'qu'
    books = books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3_view(request):
    # Filter books that:
    # 1. Have no editions higher than 2 (edition <= 2)
    # 2. Neither the title nor author contains "qu"
    book = Book.objects.filter(
        Q(edition__lte=2) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task3.html', {'books': book})

def task4_view(request):
    # Get all books ordered by title
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})

def task5_view(request):
    # Perform aggregation on Book model
    book_stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'book_stats': book_stats})

def task6_view(request):

    ad = Address.objects.annotate(n = Count('student'))

    return render(request, 'bookmodule/task6.html', {'arr': ad})




def task7_view(request):
    cities = Address.objects.annotate(student_count=Count('students'))
    return render(request, 'bookmodule/task7.html', {'cities': cities})


def list_books(request):
    q = Book.objects.all()
    return render(request, 'bookmodule/booklist.html', {'books': q})

def edit_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        p = render(request, 'edit_book.html', {'message': 'Something went wrong'})
        p['Refresh'] = '3; url=/books/lab9_part1/listbooks/'
        return p

    if request.POST.get('edit') == 'edit':
        title = request.POST.get('title')
        author = request.POST.get('author')
        edition = request.POST.get('edition')
        price = request.POST.get('price')

        book.title = title
        book.author = author
        book.edition = edition
        book.price = price

        book.save()
        p = render(request, 'bookmodule/edit_book.html', {'message': f'The book {book.title} is edited successfully'})
        p['Refresh'] = '3; url=/books/lab9_part1/booklist/'
        return p
    else:
        return render(request, 'bookmodule/edit_book.html',{'book':book})

def delete_book(request, id):
    try:
        book = Book.objects.get(id = id)
        m = f'The book {book.title} is deleted successfully!'
        book.delete()
        p = render(request, 'bookmodule/delete_book.html', {'message': m})
        p['Refresh'] = '3; url=/books/lab9_part1/booklist/'
    except Book.DoesNotExist:
        m = 'Something went wrong!'
        p = render(request, 'bookmodule/delete_book.html', {'message': m})
        p['Refresh'] = '3; url=/books/lab9_part1/booklist/'

    return p

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        edition = request.POST.get('edition')
        price = request.POST.get('price')

        Book.objects.create(title=title, author=author, edition=edition, price=price)

        m = 'User added successfully!'
        p = render(request, 'bookmodule/add_book.html', {'message': m})
        p['Refresh'] = '3; url=/books/lab9_part1/list_books/'
        return p
    else:
        return render(request,'bookmodule/add_book.html')

def list_books2(request):
    q = Book.objects.all()
    return render(request, 'bookmodule/list_books2.html', {'books': q})

def delete_book2(request, id):
    try:
        book = Book.objects.get(id = id)
        m = f'The book {book.title} is deleted successfully!'
        book.delete()
        p = render(request, 'bookmodule/delete_book.html', {'message': m})
        p['Refresh'] = '3; url=/books/lab9_part2/list_books/'
    except Book.DoesNotExist:
        m = 'Something went wrong!'
        p = render(request, 'bookmodule/delete_book.html', {'message': m})
        p['Refresh'] = '3; url=/books/lab9_part2/list_books/'

    return p

def add_book2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            edition = form.cleaned_data['edition']
            price = form.cleaned_data['price']
            Book.objects.create(title=title, author=author, edition=edition, price=price)

            m = 'Book added successfully!'
            p = render(request, 'bookmodule/add_book.html', {'message': m})
            p['Refresh'] = '3; url=/books/lab9_part2/booklist/'
            return p
    else:
        form = BookForm()
        return render(request,'bookmodule/add_book2.html',{'form': form})

def edit_book2(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        p = render(request, 'bookmodule/edit_book.html', {'message': 'Something went wrong'})
        p['Refresh'] = '3; url=/books/lab9_part2/liststudents/'
        return p

    if 'title' in request.POST:
        form = BookForm(request.POST, instance=book)  # Bind data to the form
        if form.is_valid():
            form.save()  # Save the changes to the database
            p = render(request, 'bookmodule/edit_book2.html', {'message': 'Book edited successfully'})
            p['Refresh'] = '3; url=/books/lab9_part2/liststudents/'
            return p
    else:
        form = BookForm(instance=book)
        return render(request, 'bookmodule/edit_book2.html', {'form': form})
    


def liststudents(request):
    q = Student.objects.filter().all
    return render(request, 'bookmodule/list_students.html', {'students': q})

def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            p = render(request, 'bookmodule/addm.html', {'message': 'Student added successfully'})
            p['Refresh'] = '3; url=/books/lab10/liststudents/'
            return p

    form = StudentForm(None)
    return render(request, 'bookmodule/add_student.html', {'form': form})

def editstudent(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        p = render(request, 'bookmodule/editm.html', {'message': 'Something went wrong'})
        p['Refresh'] = '3; url=/books/lab10/liststudents/'
        return p

    if 'name' in request.POST:
        form = StudentForm(request.POST, instance=student)  # Bind data to the form
        if form.is_valid():
            form.save()  # Save the changes to the database
            p = render(request, 'bookmodule/editm.html', {'message': 'Student edited successfully'})
            p['Refresh'] = '3; url=/books/lab10/liststudents/'
            return p
    else:
        form = StudentForm(instance=student)
        return render(request, 'bookmodule/edit_student.html', {'form': form})

def deletestudent(request, id):
    try:
        student = Student.objects.get(id = id)
        m = f'The Student {student.name} is deleted successfully!'
        student.delete()
        p = render(request, 'bookmodule/delete.html', {'message': m})
        p['Refresh'] = '3; url=/books/lab10/liststudents/'
    except Student.DoesNotExist:
        m = 'Something went wrong!'
        p = render(request, 'bookmodule/delete.html', {'message': m})
        p['Refresh'] = '3; url=/books/lab10/liststudents/'

    return p

def liststudents2(request):
    q = Student2.objects.filter().all
    return render(request, 'bookmodule/list_students2.html', {'students': q})

def addstudent2(request):
    if request.method == 'POST':
        form = StudentForm2(request.POST)
        if form.is_valid():
            form.save()
            p = render(request, 'bookmodule/addm.html', {'message': 'Student added successfully'})
            p['Refresh'] = '3; url=/books/lab10/task2/liststudents/'
            return p

    form = StudentForm2(None)
    return render(request, 'bookmodule/add_student.html', {'form': form})

def editstudent2(request, id):
    try:
        student = Student2.objects.get(id=id)
    except Student2.DoesNotExist:
        p = render(request, 'bookmodule/editm.html', {'message': 'Something went wrong'})
        p['Refresh'] = '3; url=/books/lab10/task2/liststudents/'
        return p

    if 'name' in request.POST:
        form = StudentForm2(request.POST, instance=student)  # Bind data to the form
        if form.is_valid():
            form.save()  # Save the changes to the database
            p = render(request, 'bookmodule/editm.html', {'message': 'Student edited successfully'})
            p['Refresh'] = '3; url=/books/lab10/task2/liststudents/'
            return p
    else:
        print(student.addresses.all())
        form = StudentForm2(instance=student)
        return render(request, 'bookmodule/edit_student.html', {'form': form})

def deletestudent2(request, id):
    try:
        student = Student2.objects.get(id = id)
        m = f'The Student {student.name} is deleted successfully!'
        student.delete()
        p = render(request, 'bookmodule/delete_student.html', {'message': m})
        p['Refresh'] = '3; url=/books/lab10/task2/liststudents/'
    except Student.DoesNotExist:
        m = 'Something went wrong!'
        p = render(request, 'bookmodule/delete_student.html', {'message': m})
        p['Refresh'] = '3; url=/books/lab10/task2/liststudents/'

    return p

#@login_required(login_url='/users/login/')

def listimages(request):
    q = Images.objects.filter().all
    return render(request, 'bookmodule/imageslist.html', {'images': q})

def deleteimage(request, id):
    try:
        image = Images.objects.get(id = id)
        m = f'The Image deleted successfully!'
        image.delete()
        p = render(request, 'bookmodule/delete.html', {'message': m})
        p['Refresh'] = '3; url=/books/lab10/task3/listimages/'
    except Images.DoesNotExist:
        m = 'Something went wrong!'
        p = render(request, 'bookmodule/delete.html', {'message': m})
        p['Refresh'] = '3; url=/books/lab10/task3/listimages/'

    return p

def addimage(request):
    if request.method == 'POST':
        print("FILES:", request.FILES)  # Debug uploaded files
        print("CoverPage:", request.FILES.get('coverPage'))  # Check for specific file
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print('here')
            form.save()
            p = render(request, 'bookmodule/addm.html', {'message': 'Image added successfully'})
            p['Refresh'] = '3; url=/books/lab10/task3/listimages/'
            return p
        print(form.errors)

    form = ImageForm(None)
    return render(request, 'bookmodule/addimage.html', {'form': form})


