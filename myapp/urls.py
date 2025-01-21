from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MahasiswaViewSet, DosenViewSet, MataKuliahViewSet, PresensiViewSet

router = DefaultRouter()
router.register(r'mahasiswa', MahasiswaViewSet)
router.register(r'dosen', DosenViewSet)
router.register(r'matakuliah', MataKuliahViewSet)
router.register(r'presensi', PresensiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
