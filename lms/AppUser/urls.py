from django.urls import URLPattern, path
from . import views
from AppUser.views import UploadUsersFromFileView

urlpatterns = [
    path('Student/', views.StudentList),
    path('Student/<int:pk>',views.StudentDetail),
    path('StudentCreate/', views.UserCreate),
    path('StudentUpdate/<int:pk>', views.StudentUpdate),
    path('StudentDelete/<int:pk>', views.StudentDelete),
    path('Teacher/', views.TeacherList.as_view()),
    path('Teacher/<int:pk>',views.TeacherDetail.as_view()),
    path('Parent/', views.ParentList.as_view()),
    path('Parent/<int:pk>',views.ParentDetail.as_view()),
    path('Annotation/', views.AnnotationList.as_view()),
    path('Annotation/<int:pk>',views.AnnotationDetail.as_view()),
    path('EnrollmentSubject/', views.EnrollmentSubjectList.as_view()),
    path('EnrollmentSubject/<int:pk>',views.EnrollmentSubjectDetail.as_view()),
    path('EnrollmentCourse/', views.EnrollmentCourseList.as_view()),
    path('EnrollmentCourse/<int:pk>', views.EnrollmentCourseDetail.as_view()),
    path('upload/', UploadUsersFromFileView.as_view())
]