from django.shortcuts import render
from student.models import Student, Subjects, Marks

def home(request):
    semesters = Subjects.objects.all()
    return render(request, 'home.html', {'semesters': semesters})



def enterMarks(request):

    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    branch = request.POST.get('branch')
    semester = Subjects.objects.get(semester = request.POST.get('semester'))

    student = Student()
    student.name = name
    student.phone = phone
    student.email =  email
    student.branch = branch
    student.semester = semester
    student.save()

    context = {
        'semester': semester,
        'student': student
    }

    return render(request, 'entermarks.html', context)


def submitMarks(request, id):
    
    marks = Marks()

    subject1 = request.POST.get('subject1')
    subject2 = request.POST.get('subject2')
    subject3 = request.POST.get('subject3')

    marks.student = Student.objects.get(pk=id)
    marks.subject1 = subject1
    marks.subject2 = subject2
    marks.subject3 = subject3

    marks.save()

    context = {
        'marks': marks
    }

    return render(request, 'submitted.html', context)