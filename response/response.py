from rest_framework import status
from rest_framework.response import Response


def exception_response(e):
    return Response(
        {
            'status': 403,
            'error': e.__str__()
        },
        status=status.HTTP_403_FORBIDDEN
    )


def login_successfully(serializer):
    return Response(
        {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
        }
    )


def register_successfully():
    return Response(
        {
            'success': 'True',
            'status code': status.HTTP_201_CREATED,
            'message': 'User registered  successfully',
        }
    )


def get_student_by_id(student_ser):
    return Response(
        {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'data': student_ser.data,
            'message': 'student data get successfully',
        }
    )


def user_not_found():
    return Response(
        {
            'status code': status.HTTP_404_NOT_FOUND,
            'message': 'User does not exist'
        }
    )


def get_student_list(student_list_ser):
    return Response(
        {
            'Success': 'True',
            'status': status.HTTP_200_OK,
            'data': student_list_ser.data,
            'message': 'Student list fetched successfully'
        }
    )


def get_teachers_list(teachers_list_ser):
    return Response(
        {
            'Success': 'True',
            'status': status.HTTP_200_OK,
            'data': teachers_list_ser.data,
            'message': 'Teachers list fetched successfully'
        }
    )


def change_password():
    return Response(
        {
            'Success': 'True',
            'status': status.HTTP_200_OK,
            'message': 'password set successfully'
        }
    )


def not_registered():
    return Response(
        {
            'Status': status.HTTP_406_NOT_ACCEPTABLE,
            'message': 'user not registered'
        }
    )


def unauthorized():
    return Response(
        {
            'Success': 'True',
            'status': status.HTTP_401_UNAUTHORIZED,
            'message': 'Unauthorized user'
        }
    )
