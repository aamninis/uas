from rest_framework import viewsets
from .models import Mahasiswa, Dosen, MataKuliah, Presensi
from .serializers import MahasiswaSerializer, DosenSerializer, MataKuliahSerializer, PresensiSerializer

# Mahasiswa ViewSet
class MahasiswaViewSet(viewsets.ModelViewSet):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer

# Dosen ViewSet
class DosenViewSet(viewsets.ModelViewSet):
    queryset = Dosen.objects.all()
    serializer_class = DosenSerializer

# MataKuliah ViewSet
class MataKuliahViewSet(viewsets.ModelViewSet):
    queryset = MataKuliah.objects.all()
    serializer_class = MataKuliahSerializer

# Presensi ViewSet
class PresensiViewSet(viewsets.ModelViewSet):
    queryset = Presensi.objects.all()
    serializer_class = PresensiSerializer
