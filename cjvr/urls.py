from django.urls import path

from .views import (TestimonyList, TestimonyDetail, VictimDetail, VictimsList, PlaintiffDetail, PlaintiffsList,
                    register_testimony, statistics_graph, search_result, register_report, delete_plaintiff,
                    delete_testimony, delete_victim, TaskList, register_task, TaskDeleteView, add_testimony)

urlpatterns = [
    path('', TestimonyList.as_view(), name="testimonies"),
    path('testimonies/<int:pk>/', TestimonyDetail.as_view(), name="testimony-detail"),
    path('victims/', VictimsList.as_view(), name="victims"),
    path('victims/<int:pk>/', VictimDetail.as_view(), name="victim-detail"),
    path('plaintiffs/', PlaintiffsList.as_view(), name="plaintiffs"),
    path('plaintiffs/<int:pk>/', PlaintiffDetail.as_view(), name="plaintiff-detail"),
    path('register/testimony/', register_testimony, name="register-testimony"),
    path('register/report/<int:testimony_id>', register_report, name="register-report"),
    path('statistics/', statistics_graph, name="statistics-graph"),
    path('delete/plaintiff/<int:plaintiff_id>', delete_plaintiff, name="delete-plaintiff"),
    path('delete/victim/<int:victim_id>', delete_victim, name="delete-victim"),
    path('delete/testimony/<int:testimony_id>', delete_testimony, name="delete-testimony"),
    path('search/', search_result, name="search"),
    path('tasks/', TaskList.as_view(), name="task-list"),
    path('register/task/', register_task, name="register-task"),
    path('delete/task/<int:pk>', TaskDeleteView.as_view(), name="delete-task"),
    path('testimony/<str:type>/<int:pk>', add_testimony, name="add-testimony"),
]
