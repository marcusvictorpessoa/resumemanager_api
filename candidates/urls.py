
from rest_framework.routers import SimpleRouter

from .views import CandidatesController


router = SimpleRouter()
router.register('candidates', CandidatesController)