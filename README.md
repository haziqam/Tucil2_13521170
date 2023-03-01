# Tugas Kecil II Strategi Algoritma

# Penyelesaian Permasalahan Closest Pair pada Ruang 3D Menggunakan Divide and Conquer

## Deskripsi singkat
Program ini akan menerima input pengguna berupa banyaknya titik (n) serta dimensi (m). Program akan membangkitkan n titik pada dimensi m secara acak. Kemudian, program akan mencari pasangan titik terdekat dari n titik tersebut. Output program berupa jarak terdekat, pasangan titik terdekat, waktu eksekusi, serta banyaknya operasi jarak Euclidean yang diperlukan pada pendekatan brute force dan divide and conquer. Program ini berbasis Command Line Interface (CLI) dan ditulis dalam bahasa Python.

## Requirements
1. Python 3

2. NumPy

3. Matplotlib

## Cara melakukan kompilasi
1. Lakukan clone pada repositori ini dengan cara memasukkan script berikut pada terminal
    ```
    git clone https://github.com/haziqam/Tucil2_13521170
    ```

2. Buka direktori doc, kemudian jalankan script berikut pada terminal
    ```
    python main.py
    ```

## Cara menggunakan program
1. Masukkan banyaknya titik dan dimensi yang diinginkan. Banyaknya titik berupa integer >=2 dan dimensi berupa integer >=1
    ```
    ====================== INPUTS =======================
    Number of points: 16
    Dimensions: 3
    =====================================================
    ```


2. Program akan menampilkan output seperti contoh berikut
    ```
    ==================== BRUTE FORCE ====================
    Min distance: 110.45693866842409
    Closest pair: ((-845.95, 150.21, 221.02), (-769.47, 106.56, 287.7))
    Execution time: 0.0
    Total operations: 120
    =====================================================


    ================ DIVIDE AND CONQUER =================
    Min distance: 110.45693866842409
    Closest pair:  ((-845.95, 150.21, 221.02), (-769.47, 106.56, 287.7))
    Execution time: 0.0009961128234863281
    Total operations: 15
    =====================================================
    ```


3. Jika dimensi = 3, maka program akan menyediakan pilihan untuk plotting hasil ke grafik
    ```
    Plot results? (y/n): y
    ```


4. Jika pengguna memilih y, maka program akan menampilkan hasil plotting menggunakan matplotlib. Setelah pengguna menekan close pada aplikasi matplotlib, maka program akan selesai

    
## Identitas author
Nama    : Haziq Abiyyu Mahdy

NIM     : 13521170

Kelas   : K2

Spesifikasi komputer yang digunakan author adalah sbb.

Processor       :	11th Gen Intel(R) Core(TM) i7-1195G7 @ 2.90GHz   2.92 GHz

Installed RAM   :	8,00 GB 

System type	    :   64-bit operating system, x64-based processor

Operating system:   Windows 11
