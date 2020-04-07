from django.forms import ModelForm
from .models import Student,Teacher,Division,Subject


class studentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class teacherform(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class divisionform(ModelForm):
    class Meta:
        model = Division
        fields = '__all__'

class subjectform(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'