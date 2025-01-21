from django.db import models

class Mahasiswa(models.Model):
    id_mahasiswa = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nama} ({self.nim})"

class Dosen(models.Model):
    id_dosen = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    nip = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nama} ({self.nip})"

class MataKuliah(models.Model):
    id_matakuliah = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    kode = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nama} ({self.kode})"

class Presensi(models.Model):
    STATUS_CHOICES = [
        ('Hadir', 'Hadir'),
        ('Tidak Hadir', 'Tidak Hadir'),
        ('Izin', 'Izin'),
    ]

    id_presensi = models.AutoField(primary_key=True)
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, related_name='presensi')
    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE, related_name='presensi')
    matakuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE, related_name='presensi')
    tanggal = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Presensi: {self.mahasiswa.nama} - {self.matakuliah.nama} ({self.tanggal})"
