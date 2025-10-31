from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Club, Group
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required



def h(request):
    return HttpResponse("hello world!")


@login_required
def main(request):
    students = Student.objects.all()
    return render(request, './students.html', {'students': students})


from .forms import StudentForm


# def create_club(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         curator = request.POST.get("curator")

#         Club.objects.create(
#             name=name,
#             curator=curator
#         )
#         return redirect("main")
#     return render(request, './create.html')




def create_student(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        group = request.POST.get("group")
        photo = request.FILES.get("photo")

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            group=group,
            photo=photo
        )
        return redirect("main")
    return render(request, './create.html')

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "./detail.html", {"student": student})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    groups = Group.objects.all()
    clubs = Club.objects.all()

    if request.method == "POST":
        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.age = request.POST.get("age")

        # Обновление группы
        group_id = request.POST.get("group")
        if group_id:
            student.group = Group.objects.get(id=group_id)

        student.save()

        # Обновление клубов
        selected_clubs = request.POST.getlist("clubs")  # список id выбранных клубов
        student.clubs.set(selected_clubs)

        return redirect("main")

    return render(
        request,
        "edit.html",
        {"student": student, "groups": groups, "clubs": clubs}
    )
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect("main")



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )
            return redirect("main")
    else:
        form = RegisterForm()
    return render(request, "./register.html", {"form": form})


def login_view(request):
    return render(request, "./login.html")