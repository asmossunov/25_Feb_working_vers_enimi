from django.urls import path

from cabinet_parents.views.base import ParentProfileView, ParentCreateChildrenView, \
    ParentCreateChildrenWithoutEmailView, ParentChildrenSurveysView, CreateParentChildrenSurveyView

urlpatterns = [
    path('<int:pk>/', ParentProfileView.as_view(), name='parents_cabinet_detail'),
    path('<int:pk>/create/children/', ParentCreateChildrenView.as_view(), name='parent_create_children'),
    path('<int:pk>/create/children_without_email/', ParentCreateChildrenWithoutEmailView.as_view(), name='parent_create_children_without_email'),
    path('<int:pk>/parent_children_surveys', ParentChildrenSurveysView.as_view(), name='parent_children_surveys'),
    path('<int:pk>/parent_children_surveys/create_survey', CreateParentChildrenSurveyView.as_view(), name='parent_children_create_surveys')
    # path('<int:pk>/get_children_surveys/', GetDataForSurveysView.as_view(), name='get_children_surveys'),
    # path('<int:pk>/change_avatar/', upload_file, name='change_avatar'),
]