from django.conf.urls import url
from django.urls import path

from user import views as view

urlpatterns = [
    url(r'^signup/', view.UserRegistrationView.as_view(), name='signup'),
    url(r'^login/', view.UserLoginView.as_view(), name='login'),
    url(r'^get_student_by_id/', view.ViewStudent.as_view(), name='student_by_id'),
    url(r'^get_students_list/', view.GetStudentList.as_view()),
    url(r'^get_teacher_list/', view.GetTeacherList.as_view()),
    url(r'^forgot_password/', view.ForgotPassword.as_view()),
]
