import pyrebase

# Konfigurasi Firebase
config = {
    "apiKey": "msnE8pdZStSCOtkENXEOkTiHZx5fim5cc5H3LXzQ",
    "authDomain": "918631797563-b1hoetsk03iipu9fcl01971nvfhqf7en.apps.googleusercontent.com",
    "databaseURL": "https://carcinamon-comunity-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "carcinamon-comunity",
    "storageBucket": "gs://carcinamon-comunity.appspot.com",
    "messagingSenderId": "918631797563",
    "appId": "1:918631797563:android:1eeb46d9c26597e1a11d1e",
}

# Inisialisasi aplikasi Firebase
firebase = pyrebase.initialize_app(config)

# Mendapatkan referensi ke Firebase Realtime Database
db = firebase.database()

# Mendaftar ke notifikasi perubahan di direktori "post"
def stream_handler(message):
    if message["event"] == "put":
        entry_id = message["path"].split("/")[-1]
        updated_value = message["data"]
        
        print("Entry ID:", entry_id)
        print("Nilai terbaru:", updated_value)

        # Lakukan apa pun yang diperlukan dengan entry ID dan nilai terbaru di sini
        # Misalnya, baca komentar terbaru atau lakukan operasi lainnya

# Mendengarkan perubahan pada direktori "post"
post_ref = db.child("post")
post_ref.stream(stream_handler)