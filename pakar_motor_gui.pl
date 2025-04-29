:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.

% Jenis-jenis kerusakan motor
kerusakan("Busi Rusak").
kerusakan("Aki Soak").
kerusakan("Karburator Kotor").
kerusakan("Klep Bocor").

% Gejala untuk tiap kerusakan
gejala(susah_dihidupkan, "Busi Rusak").
gejala(mesin_mati_mendadak, "Busi Rusak").
gejala(tidak_ada_pengapian, "Busi Rusak").

gejala(motor_sulit_dinyalakan, "Aki Soak").
gejala(lampu_redup, "Aki Soak").
gejala(klakson_lemah, "Aki Soak").

gejala(mesin_brebet, "Karburator Kotor").
gejala(boros_bbm, "Karburator Kotor").
gejala(susah_starter, "Karburator Kotor").

gejala(tenaga_berkurang, "Klep Bocor").
gejala(asap_putih, "Klep Bocor").
gejala(suara_mesin_kasar, "Klep Bocor").

% Pertanyaan untuk masing-masing gejala
pertanyaan(susah_dihidupkan, Y) :- Y = "Apakah motor susah dihidupkan?".
pertanyaan(mesin_mati_mendadak, Y) :- Y = "Apakah mesin mati mendadak saat digunakan?".
pertanyaan(tidak_ada_pengapian, Y) :- Y = "Apakah tidak ada percikan api dari busi?".

pertanyaan(motor_sulit_dinyalakan, Y) :- Y = "Apakah motor sulit dinyalakan terutama saat pagi?".
pertanyaan(lampu_redup, Y) :- Y = "Apakah lampu terlihat redup saat dinyalakan?".
pertanyaan(klakson_lemah, Y) :- Y = "Apakah suara klakson menjadi lemah?".

pertanyaan(mesin_brebet, Y) :- Y = "Apakah mesin brebet saat digas?".
pertanyaan(boros_bbm, Y) :- Y = "Apakah konsumsi bahan bakar meningkat drastis?".
pertanyaan(susah_starter, Y) :- Y = "Apakah motor sulit distarter?".

pertanyaan(tenaga_berkurang, Y) :- Y = "Apakah tenaga motor berkurang saat digunakan?".
pertanyaan(asap_putih, Y) :- Y = "Apakah keluar asap putih dari knalpot?".
pertanyaan(suara_mesin_kasar, Y) :- Y = "Apakah terdengar suara kasar dari mesin?".
