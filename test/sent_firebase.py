import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Inisialisasi aplikasi Firebase dengan menggunakan kredensial yang sesuai
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://carcinamon-comunity-default-rtdb.asia-southeast1.firebasedatabase.app/Users'
})

# Mendapatkan referensi ke Firebase Realtime Database
ref = db.reference('post')

# Membuat data JSON
data = {
    "header": "ini judul",
    "text": "4",
    "img": "kalau ada"
}

# Mengirim data JSON ke Firebase Realtime Database dengan membuat ID unik
new_post_ref = ref.push()
new_post_ref.set(data)

print("Data berhasil dikirim ke Firebase dengan ID unik:", new_post_ref.key)