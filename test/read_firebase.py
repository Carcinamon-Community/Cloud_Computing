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

# Membaca data terbaru di bawah "post"
latest_post = ref.order_by_key().limit_to_last(1).get()

# Mengekstrak nilai entri terbaru
for key, value in latest_post.items():
    print("ID: ", key)
    print("Header: ", value['header'])
    print("Text: ", value['text'])
    print("Img: ", value['img'])