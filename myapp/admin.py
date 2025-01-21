from django.contrib import admin
from .models import Mahasiswa, Dosen, MataKuliah, Presensi

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('id_mahasiswa', 'nama', 'nim')
    search_fields = ('nama', 'nim')

@admin.register(Dosen)
class DosenAdmin(admin.ModelAdmin):
    list_display = ('id_dosen', 'nama', 'nip')
    search_fields = ('nama', 'nip')

@admin.register(MataKuliah)
class MataKuliahAdmin(admin.ModelAdmin):
    list_display = ('id_matakuliah', 'nama', 'kode')
    search_fields = ('nama', 'kode')

@admin.register(Presensi)
class PresensiAdmin(admin.ModelAdmin):
    list_display = ('id_presensi', 'mahasiswa', 'dosen', 'matakuliah', 'tanggal', 'status')
    list_filter = ('status', 'tanggal')
    search_fields = ('mahasiswa__nama', 'dosen__nama', 'matakuliah__nama')
