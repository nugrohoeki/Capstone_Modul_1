# Capstone Project Modul 1: Penjualan Barang Toko (Penjualan Barang Kaset/CD/Vinyl Pada Toko Musik)




## Overview
Capstone Project module 1 ini merupakan implementasi program penjualan format hasil rekaman musik fisik seperti Kaset, CD, Vinyl. Aplikasi ini dibuat untuk menampilkan list stock barang, menambahkan stock barang, melakukan sunting data yang tersimpan memudahkan pengelolaan atau pendataan stock.

### Batasan
Untuk Item Code hanya terbatas 4 karakter string

### Data Description
| No | Nama Kolom | Type | Range | Deskripsi |
| ------ | ------ | ---- | ----- | --------- |
| 1 | Item Code | ⁠ str ⁠ | 4 | Kode Unik |
| 2 | Jenis | ⁠ str ⁠ | - | Jenis rekaman musik (Kaset/CD/Vinyl) |
| 3 | Artist| ⁠ str ⁠  | - |Nama Artist|
| 4 | Album | ⁠ str ⁠ | - | Judul Album |
| 5 | Genre | ⁠ str ⁠ | - | Genre/Jenis Musik |
| 6 | Tahun Rilis | ⁠ int  | 1950 - 2024 | Tahun rilis Album |
| 7 | Jumlah | ⁠ int  | >0 | Stock Item |
| 8 | Harga | ⁠ float  | - | Harga item  dalam (Rp) |


### Read
Fungsi read pada aplikasi ini memungkinkan untuk menampilkan data penjualan barang toko musik, terdapat pilihan mencari barang berdasarkan item code dan nama

### Create
Fungsi create untuk menambahkan data berdasarkan item code yang unik dan belum ada sebelumnya.

### Update
Fungsi ini untuk merubah/mesunting data yang sudah disimpan pada list, berdasarkan id code kemudian baru memilih data mana yang akan diupdate, dan khusus untuk item code jika akan di edit ke id code yang sudah tersimpan, maka akan ditolak dan akan memintakan id code baru.

### Delete
Fungsi ini berfungsi untuk menghapus data per item code, jika item code yang dimasukan untuk dihapus tidak terdapat dalam data maka akan diberi tahu bahwa masukan kembali item code yang akan dihapus.




