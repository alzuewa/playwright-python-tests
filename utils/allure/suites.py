from enum import StrEnum


class AllureParentSuite(StrEnum):
    LMS = 'LMS system'
    STUDENT = 'Student system'
    ADMINISTRATION = 'Administration system'


class AllureSuite(StrEnum):
    COURSES = 'Courses'
    DASHBOARD = 'Dashboard'
    AUTHENTICATION = 'Authentication'


class AllureSbuSuite(StrEnum):
    COURSES = 'Courses'
    DASHBOARD = 'Dashboard'
    REGISTRATION = 'Registration'
    AUTHORIZATION = 'Authorization'
