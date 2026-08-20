from django.shortcuts import render, redirect, get_object_or_404
from . models import Student
from . forms import StudentForm


# Create your views here.

#READ
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

#CREATE
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_create.html', {'form': form})


#UPDATE
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method =='POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_create.html', {'form': form })

#DELETE
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method=='POST':
        student.delete()
    return redirect('student_list')
