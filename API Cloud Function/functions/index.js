const functions = require("firebase-functions");
const admin = require("firebase-admin");
admin.initializeApp();

exports.listenToPostChanges = functions.database.ref("/post/{postId}").onUpdate((change, context) => {
    const postId = context.params.postId;
    const updatedPostData = change.after.val();

    // Memeriksa apakah ada perubahan pada komentar
    if (updatedPostData.coment) {
        const comments = updatedPostData.coment;
        const commentIds = Object.keys(comments);
        const latestCommentId = commentIds[commentIds.length - 1];
        const latestComment = comments[latestCommentId];

        const latestCommentText = latestComment.text;
        console.log(`Komentar terbaru di entri ${postId}: ${latestCommentText}`);

        const text = `${latestCommentText}`;
        const url = "https://model-ml-7vvpza7dfa-et.a.run.app"; // Ganti URL dengan URL API ML Model yang sesuai

        fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `sentence=${encodeURIComponent(text)}`
        })
            .then(response => response.json())
            .then(jsonResponse => {
                const prediction = jsonResponse.prediction;
                console.log(jsonResponse);

                if (prediction > 0.5) {
                    console.log(`Hasil prediksi (${prediction}) lebih dari 0.5. Menghapus komentar dengan latestCommentId: ${latestCommentId}`);
                    const commentsRef = admin.database().ref(`/post/${postId}/comment`);
                    commentsRef.child($({latestCommentId})).remove()
                        .then(() => {
                            console.log(`Komentar dengan latestCommentId: ${latestCommentId} berhasil dihapus dari database.`);
                        })
                        .catch(error => {
                            console.error(`Gagal menghapus komentar dengan latestCommentId: ${latestCommentId} dari database:`, error);
                        });
                } else {
                    console.log(`Hasil prediksi (${prediction}) kurang dari atau sama dengan 0.5. Tidak menghapus komentar dengan latestCommentId: ${latestCommentId}`);
                }

            })
            .catch(error => {
                console.error("Error dalam mengirimkan permintaan ke model machine learning:", error);
            });
    } else {
        console.log(`Tidak ada komentar baru di entri ${postId}`);
    }

    return null; // Mengembalikan null agar fungsi selesai
});