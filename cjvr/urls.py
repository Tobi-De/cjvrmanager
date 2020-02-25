from django.urls import path

from .views import (home, TestimonyList, TestimonyDetail, VictimDetail, VictimsList, PlaintiffDetail, PlaintiffsList,
                    register_testimony, statistics_graph, graph)

urlpatterns = [
    path('', home, name="home"),
    path('testimonies/', TestimonyList.as_view(), name="testimonies"),
    path('testimonies/<int:pk>/', TestimonyDetail.as_view(), name="testimony-detail"),
    path('victims/', VictimsList.as_view(), name="victims"),
    path('victims/<int:pk>/', VictimDetail.as_view(), name="victim-detail"),
    path('plaintiffs/', PlaintiffsList.as_view(), name="plaintiffs"),
    path('plaintiffs/<int:pk>/', PlaintiffDetail.as_view(), name="plaintiff-detail"),
    path('register/testimony/', register_testimony, name="register-testimony"),
    path('statistics/', statistics_graph, name="statistics-graph"),
    path('/graph/', graph, name="graph"),

]
