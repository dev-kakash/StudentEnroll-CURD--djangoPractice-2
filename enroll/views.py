from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student


# Create your views here.
def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            student_id = form.cleaned_data['student_id']
            save = Student(name=name, email=email, student_id=student_id)
            save.save()
            return HttpResponseRedirect('/')

    else:
        form = StudentRegistration()
    student_data = Student.objects.all()
    return render(request, 'enroll/addshow.html', {'form': form, 'student_data': student_data})


def delete_data(request, id):
    if request.method == 'POST':
        deleteStudent = Student.objects.get(pk=id)
        deleteStudent.delete()
        return HttpResponseRedirect('/')


def update_data(request, id):
    if request.method == 'POST':
        updateStudent = Student.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=updateStudent)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        updateStudent = Student.objects.get(pk=id)
        form = StudentRegistration(instance=updateStudent)

    return render(request, 'enroll/update.html', {'form': form})
