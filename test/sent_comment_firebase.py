import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Inisialisasi aplikasi Firebase dengan menggunakan kredensial yang sesuai
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://carcinamon-comunity-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Mendapatkan referensi ke Firebase Realtime Database
ref = db.reference('post')

# ID kunci entri yang ingin diubah
entry_id = "-NY2aVlPBt1I1704EoLa"

# Membuat data JSON untuk komentar
komentar_data = {
    "text": "kontol"
}

# Menambahkan komentar dengan ID yang dihasilkan secara otomatis
new_comment_ref = ref.child(entry_id).child("coment").push(komentar_data)

# Mendapatkan ID yang dihasilkan secara otomatis
new_comment_id = new_comment_ref.key

print("Komentar baru ditambahkan dengan ID:", new_comment_id)