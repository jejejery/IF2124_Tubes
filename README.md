# IF2124_Tubes_Puyeng
Tubes TBFO
Dalam proses pembuatan program dari sebuah bahasa menjadi instruksi yang dapat dieksekusi oleh mesin, terdapat pemeriksaan sintaks bahasa atau parsing yang dibuat oleh programmer untuk memastikan program dapat dieksekusi tanpa menghasilkan error. Parsing ini bertujuan untuk memastikan instruksi yang dibuat oleh programmer mengikuti aturan yang sudah ditentukan oleh bahasa tersebut. Baik bahasa berjenis interpreter maupun compiler, keduanya pasti melakukan pemeriksaan sintaks. Perbedaannya terletak pada apa yang dilakukan setelah proses pemeriksaan (kompilasi/compile) tersebut selesai dilakukan.

Dibutuhkan grammar bahasa dan algoritma parser untuk melakukan parsing. Sudah sangat banyak grammar dan algoritma yang dikembangkan untuk menghasilkan compiler dengan performa yang tinggi. Terdapat CFG, CNF-e, CNF+e, 2NF, 2LF, dll untuk grammar yang dapat digunakan, dan terdapat LL(0), LL(1), CYK, Earley’s Algorithm, LALR, GLR, Shift-reduce, SLR, LR(1), dll untuk algoritma yang dapat digunakan untuk melakukan parsing.

Pada tugas besar ini, implementasikan parser untuk JavaScript (Node.js) untuk beberapa statement dan sintaks bawaan JavaScript. Gunakanlah konsep CFG untuk pengerjaan parser yang mengevaluasi syntax program. Untuk nama variabel dan operasi (+, -, >, dll) dalam program, gunakanlah FA.

Algoritma yang dipakai dibebaskan, namun tim asisten menyarankan menggunakan algoritma CYK (Cocke-Younger-Kasami). Algoritma CYK harus menggunakan grammar CNF (Chomsky Normal Form) sebagai grammar masukannya. Oleh karena itu, jika ingin menggunakan CYK buatlah terlebih dahulu grammar dalam CFG (Context Free Grammar), kemudian konversikan grammar CFG tersebut ke grammar CNF
