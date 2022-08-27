from rest_framework import routers
from .views import QuestionViewSet

router = routers.DefaultRouter()

router.register('questions', QuestionViewSet)

urlpatterns = router.urls
