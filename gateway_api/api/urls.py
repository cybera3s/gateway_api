from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register("users", UserViewSet, basename='user')

urlpatterns = router.urls
