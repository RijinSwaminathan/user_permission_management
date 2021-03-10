from rest_framework import status
from rest_framework.response import Response


def exception_response(error):
    """
    :param error: error message
    :return: exception occurred
    """
    return Response(
        {
            'status': 403,
            'error': error.__str__()
        },
        status=status.HTTP_403_FORBIDDEN
    )


def login_successfully(serializer):
    """
    :param serializer:
    :return: Login Successfully
    """
    return Response(
        {
            'success': 'True',
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
        },
        status=status.HTTP_200_OK,

    )


def register_successfully():
    """
    :return: User registration successful and new user created
    """
    return Response(
        {
            'success': 'True',
            'message': 'User registered  successfully',
        },
        status=status.HTTP_201_CREATED,

    )


def get_student_by_id(student_ser):
    """
    :param student_ser:
    :return: pass the id of the student get the information according to id
    """
    return Response(
        {
            'success': 'True',
            'data': student_ser.data,
            'message': 'student data get successfully',
        },
        status=status.HTTP_200_OK,

    )


def user_not_found():
    """
    :return: return the response if the user with the id does not exist
    """
    return Response(
        {
            'message': 'User does not exist'
        },
        status=status.HTTP_404_NOT_FOUND
    )


def get_student_list(student_list_ser):
    """
    :param student_list_ser:
    :return: get the list of the students as response
    """
    return Response(
        {
            'Success': 'True',
            'data': student_list_ser.data,
            'message': 'Student list fetched successfully'
        },
        status=status.HTTP_200_OK,
    )


def get_teachers_list(teachers_list_ser):
    """
    :param teachers_list_ser:
    :return: get the list of teachers as response
    """
    return Response(
        {
            'Success': 'True',
            'data': teachers_list_ser.data,
            'message': 'Teachers list fetched successfully'
        },
        status=status.HTTP_200_OK)


def change_password():
    """
    :return: if the password changed successfully this response will returned.
    """
    return Response(
        {
            'Success': 'True',
            'message': 'password set successfully'
        },
        status=status.HTTP_200_OK
    )


def not_registered():
    """
    :return: if the email id not registered then this response will returned.
    """
    return Response(
        {
            'message': 'user not registered'
        },
        status=status.HTTP_406_NOT_ACCEPTABLE,

    )


def unauthorized():
    """
    :return: if the user token is not authorized with user roles this response will return
    """
    return Response(
        {
            'Success': 'True',
            'message': 'Unauthorized user'
        },
        status=status.HTTP_401_UNAUTHORIZED,

    )
