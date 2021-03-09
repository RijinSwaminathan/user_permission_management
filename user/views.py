# Create your views here.
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


class UserRegistrationView(APIView):
    serializer_class = ser.UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        :param request:
        :return:
        """
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.register_successfully()
        except Exception as e:
            return response.exception_response(e)


class UserLoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ser.UserLoginSerializer

    def post(self, request):
        """
        :param request:
        :return:
        """
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            return response.login_successfully(serializer)
        except Exception as e:
            return response.exception_response(e)


class ViewStudent(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = ser.StudentProfileSerializer

    def get(self, request):
        try:
            user_id = request.GET.get('user_id')
            student = Profile.objects.get(user_id=user_id, role=3)
            if student:
                student_ser = ser.StudentProfileSerializer(student, many=False)
                return response.get_student_by_id(student_ser)
            return response.user_not_found()
        except Exception as e:
            return response.exception_response(e)


class GetStudentList(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = ser.StudentProfileSerializer

    def get(self, request):
        try:
            if Profile.objects.filter(role__lte=2):
                student_list = Profile.objects.filter(role=3)
                student_list_ser = ser.StudentProfileSerializer(student_list, many=True)
                return response.get_student_list(student_list_ser)
            return response.unauthorized()
        except Exception as e:
            return response.exception_response(e)


class GetTeacherList(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = ser.TeacherProfileSerializer

    def get(self, request):
        try:
            if Profile.objects.filter(role=1):
                teachers_list = Profile.objects.filter(role=2)
                teachers_list_ser = ser.TeacherProfileSerializer(teachers_list, many=True)
                return response.get_teachers_list(teachers_list_ser)
            return response.unauthorized()
        except Exception as e:
            return response.exception_response(e)


class ForgotPassword(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            mail_id = request.data.get('email'),
            password = request.data.get('password')
            user = User.objects.get(email=mail_id[0])
            if user:
                user.set_password(password)
                user.save()
                return response.change_password()
            return response.not_registered()
        except Exception as e:
            return response.exception_response(e)
