# Data judul buku
judul_buku = [ #digunakan untuk menyimpan judul buku
    "Pemrograman Python",
    "Algoritma dan Struktur Data",
    "Basis Data",
    "Jaringan Komputer",
    "Sistem Operasi"
]

# Menampilkan data awal
print("Judul buku sebelum diurutkan:")
print(judul_buku)

# Proses Insertion Sort
for i in range(1, len(judul_buku)):#Pengurutan dimulai dari indeks ke-1 karena elemen pertama dianggap sudah terurut

    key = judul_buku[i]#Key adalah data yang akan dicari posisi yang tepat
    j = i - 1

    print("\n=== Tahap", i, "===")
    print("Key =", key)

    # Membandingkan key dengan data sebelumnya
    while j >= 0 and judul_buku[j] > key:#Jika data sebelumnya lebih besar secara alfabet, maka data tersebut digeser ke kanan

        print(judul_buku[j],
              "lebih besar dari",
              key)

        print("Geser",
              judul_buku[j],
              "ke kanan")

        judul_buku[j + 1] = judul_buku[j]#Digunakan untuk memberi ruang bagi key agar dapat ditempatkan pada posisi yang benar

        j -= 1

        print("Hasil sementara:",
              judul_buku)

    # Menyisipkan key
    judul_buku[j + 1] = key#Key dimasukkan ke posisi yang sesuai sehingga bagian kiri tetap terurut


    print("Sisipkan",
          key,
          "ke posisi",
          j + 1)

    # Eliminasi
    print("Eliminasi:")
    print(judul_buku[:i + 1],
          "sudah terurut")#Menunjukkan bahwa sebagian data di sebelah kiri sudah selesai diurutkan dan tidak perlu diurutkan ulang

# Menampilkan hasil akhir
print("\nJudul buku setelah diurutkan:")
print(judul_buku)
