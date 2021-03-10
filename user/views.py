# Create your views here.
from django.db import transaction
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from response import response as response
from user import serializers as ser
from user.models import Profile, User

"""
created_on: 09 - Mar - 2021
@author: Rijin NP
"""


class AdminRegistrationView(APIView):
    """Api to register the super-admin user."""
    serializer_class = ser.AdminRegistrationSerializer
    permission_classes = (AllowAny,)

    @transaction.atomic()
    def post(self, request):
        """
        :param request:
        {
            "email":"super_admin@gmail.com",
            "password":"123456",
            "profile":{
                "first_name": "Rahul",
                "last_name":"P",
                "phone_number":"+919068876645"
            }
        }
        :return:
        """
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.register_successfully()
        except Exception as error:
            return response.exception_response(error)


class TeacherRegisterView(APIView):
    """
    API to register Teacher this can be performed by the super-admin user
    """
    serializer_class = ser.TeacherRegistrationSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    @transaction.atomic()
    def post(self, request):
        """
        :param request:
        {
             "email":"teacher41@gmail.com",
             "password":"123456",
             "profile":{
                 "first_name": "Rahul",
                 "last_name":"PR",
                 "phone_number":"+919168876455",
                 "subject":"Science"
             }
        }
        pass the auth token to register the teacher if the users token match
        the role of super-admin then the operation will authenticate.
        :return:
        """
        try:
            if request.user.profile.role == 1:
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return response.register_successfully()
            return response.unauthorized()
        except Exception as error:
            return response.exception_response(error)


class StudentRegisterView(APIView):
    """
    API to register the student this can be performed only by super-admin or teacher
    """
    serializer_class = ser.StudentRegistrationSerializer
    permission_classes = (AllowAny,)

    @transaction.atomic()
    def post(self, request):
        """
        :param request:
        {
             "email":"student123@gmail.com",
             "password":"123456",
             "profile":{
                 "first_name": "Anais",
                 "last_name":"PR",
                 "phone_number":"+919064876455",
                 "standard": "plus two"
             }
        }
        pass the auth token to register the student if the users token match the role of super-admin
            or teacher then the operation will authenticate.
        :return:
        """
        try:
            if request.user.profile.role <= 2:
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return response.register_successfully()
            return response.unauthorized()
        except Exception as error:
            return response.exception_response(error)


class UserLoginView(APIView):
    """
    API for user login.
    """
    permission_classes = (AllowAny,)
    serializer_class = ser.UserLoginSerializer

    @transaction.atomic()
    def post(self, request):
        """
        :param request: pass the login credentials
        input:
        {
            "email":"example@gmail.com",
            "password":"123456"
        }
        :return:
        """
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            return response.login_successfully(serializer)
        except Exception as error:
            return response.exception_response(error)


class ViewStudent(APIView):
    """
    API to get the student his/her details
    """
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = ser.StudentProfileSerializer

    def get(self, request):
        """
        :param request: pass the user_id of the user and get the information's accordingly.
        :return:
        """
        try:
            user_id = request.GET.get('user_id')
            student = Profile.objects.get(user_id=user_id, role=3)
            if student:
                student_ser = ser.StudentProfileSerializer(student, many=False)
                return response.get_student_by_id(student_ser)
            return response.user_not_found()
        except Exception as error:
            return response.exception_response(error)


class GetStudentList(APIView):
    """
    API to get the student list this can be accessed by a teacher or super-admin
    """
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = ser.StudentProfileSerializer

    def get(self, request):
        """
        :param request: pass the auth token to fetch the student list.if the users token match the
            role of super-admin or teacher then the operation will authenticate.
        :return:
        """
        try:
            if request.user.profile.role <= 2:
                student_list = Profile.objects.filter(role=3)
                student_list_ser = ser.StudentProfileSerializer(student_list, many=True)
                return response.get_student_list(student_list_ser)
            return response.unauthorized()
        except Exception as error:
            return response.exception_response(error)


class GetTeacherList(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = ser.TeacherProfileSerializer

    def get(self, request):
        """
        :param request: pass the auth token to fetch the teachers list. if the auth token
            match the role of super-admin then the operation will authenticate.
        :return:
        """
        try:
            if request.user.profile.role == 1:
                teachers_list = Profile.objects.filter(role=2)
                teachers_list_ser = ser.TeacherProfileSerializer(teachers_list, many=True)
                return response.get_teachers_list(teachers_list_ser)
            return response.unauthorized()
        except Exception as error:
            return response.exception_response(error)


class ForgotPassword(APIView):
    """
    API to set a new password when the registered user need to
    """
    permission_classes = (AllowAny,)

    @transaction.atomic()
    def post(self, request):
        """
        :param request: get the email and password as input.
        {
            "email":"student123@gmail.com",
            "password":"123456"
        }
        :return: It will check the email is registered or not.
            if it registered then go for the execution.
        """
        try:
            mail_id = request.data.get('email')
            password = request.data.get('password')
            user = User.objects.get(email=mail_id[0])
            if user:
                user.set_password(password)
                user.save()
                return response.change_password()
            return response.not_registered()
        except Exception as error:
            return response.exception_response(error)
