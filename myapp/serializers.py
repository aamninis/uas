from rest_framework import serializers
from .models import Mahasiswa, Dosen, MataKuliah, Presensi

class MahasiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = ['id_mahasiswa', 'nama', 'nim']


class DosenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dosen
        fields = ['id_dosen', 'nama', 'nip']


class MataKuliahSerializer(serializers.ModelSerializer):
    class Meta:
        model = MataKuliah
        fields = ['id_matakuliah', 'nama', 'kode']


class PresensiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presensi
        fields = ['id_presensi', 'mahasiswa', 'dosen', 'matakuliah', 'tanggal', 'status']
