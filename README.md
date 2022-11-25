## Table of Contents
* [General Info](#general-information)
* [Tech Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Creator](#creator)

## General Information
<p> Tugas besar ini mengimplementasikan parser untuk JavaScript (Node.js) untuk beberapa statement dan sintaks bawaan JavaScript dengan merancang parser dengan Python. Kami menggunakanlah konsep CFG untuk pengerjaan parser yang mengevaluasi syntax program. Untuk nama variabel dan operasi (+, -, >, dll) dalam program, kami menggunakanlah FA.

Grammar CFG yang kami deklarasikan akan diubah menjadi bentuk CNF. Setelah itu, kami akan memprosesnyaengan algoritma CYK dan menunjukan apakah sintaks JavaScript tersebut diterima oleh CFG atau tidak</p>


## Technologies Used
- Kami menggunakan Python sebagai bahasa pemrograman untuk memproses sintaks kami


## Features
<p> Program menerima inputan file Javascript yang berisikan kode program, kemudian program dapat melakukan evaluase sintaks dengan memanfaatkan konsep CFG, CNF,FA, dan Algoritma CYK. Program ini akan menampilkan pesan ke layar, apabila sintaks JavaScript tidak diterima, maka akan menampilkan "Syntax Error". Namun apabila diterima, program akan menampilkan "Accepted".</p>


## Setup
- Clone repository ini dan jalankan file main.py di folder src melalui command line dengan menambahkan nama file javascript yang ingin dievaluasi sintaksisnya


## Usage
Berikut merupakan tampilan penggunaan program 
```
 C:\Users\src> py main.py testcase1.js

Result: Accepted
Execution time :  28.22 s
Variable + terminal count : 285
```

## Creator
Tugas besar ini dibuat oleh:
- Febryan Arota H (13521120)
- Jeremya Dharmawan R (13521131)
- Michael Utama (13521137)
