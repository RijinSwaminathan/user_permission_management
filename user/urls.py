from django.conf.urls import url

from user import views as view

"""
Url for use api
"""
urlpatterns = [

    url(r'^register-admin/', view.AdminRegistrationView.as_view(), name='admin-register'),
    url(r'^register-teacher/', view.TeacherRegisterView.as_view(), name='register-teacher'),
    url(r'^register-student/', view.StudentRegisterView.as_view(), name='register-student'),
    url(r'^login/', view.UserLoginView.as_view(), name='login'),
    url(r'^get_student_by_id/', view.ViewStudent.as_view(), name='student_by_id'),
    url(r'^get_students_list/', view.GetStudentList.as_view()),
    url(r'^get_teacher_list/', view.GetTeacherList.as_view()),
    url(r'^forgot_password/', view.ForgotPassword.as_view(), name='forgot-password'),
]
