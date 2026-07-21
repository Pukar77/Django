
all() command -> Used to fetch all the data

>>> from blog.models import Student
>>> student = Student.objects.all()
>>> print(student)
<QuerySet [<Student: Pukar>, <Student: Rimal>]>
>>> for s in student:
...     print(s.name, s.age, s.email)
... 
Pukar 22 pukar@email.com
Rimal 23 rimal@gmail.com
>>> 

get() -> used to fetch only one item, it will throw error if there is no matching items or even if there are multiple items. It just writtens 1 single item

>>> stu = Student.objects.get(id=2)
>>> print(stu)
Rimal


>>> student = Student.objects.filter(age__gt=22)
>>> print(student)
<QuerySet [<Student: Rimal>]>


>>> student = Student.objects.filter(name__startswith="p")
>>> print(student)
<QuerySet [<Student: Pukar>]>

