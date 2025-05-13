from enum import StrEnum


class AppRoute(StrEnum):
    COURSES = './#/courses'
    CREATE_COURSE = './#/courses/create'
    DASHBOARD = './#/dashboard'
    LOGIN = './#/auth/login'
    REGISTRATION = './#/auth/registration'
