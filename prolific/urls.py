from django.conf.urls import url
from prolific import views

urlpatterns = [
    url(
        'studies/$',
        views.StudyView.as_view(),
        name="studies"
    ),
    url(
        'studies/(?P<study_id>[\d])/submissions/$',
        views.StudySubmissionsView.as_view(),
        name="study_submission_list"
    ),
    url(
        'submissions/$',
        views.SubmissionView.as_view(),
        name="submissions"
    ),
    url(
        'submissions/(?P<submission_id>[\d])/$',
        views.SubmissionUpdateView.as_view(),
        name="submission_update"
    ),
]