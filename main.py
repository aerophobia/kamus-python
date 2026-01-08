meme_dict = {
            "CRINGE": "sesuatu yang sangat aneh atau memalukan",
            "LOL": "tanggapan umum terhadap sesuatu yang lucu",
            "ROFL" : "tanggapan terhadap lelucon",
            "SHEESH" : "sedikit ketidaksetujuan",
            "CREEPY" : "menakutkan, tidak menyenangkan",
            "AGGRO" : "untuk menjadi agresif/marah"
            }

word = input("ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("kata", word, "tidak ditemukan")
