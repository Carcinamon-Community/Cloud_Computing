
import functions
import admin

admin.initializeApp()

def listenToPostChanges(change, context):
    postId = context.params['postId']
    updatedPostData = change.after.val()

    # Memeriksa apakah ada perubahan pada komentar
    if 'coment' in updatedPostData:
        comments = updatedPostData['coment']
        commentIds = list(comments.keys())
        latestCommentId = commentIds[-1]
        latestComment = comments[latestCommentId]

        latestCommentText = latestComment['text']
        print(f"Komentar terbaru di entri {postId}: {latestCommentText}")
    else:
        print(f"Tidak ada komentar baru di entri {postId}")

    return None # Mengembalikan None agar fungsi selesai

listenToPostChangesFunction = functions.database.ref('/post/{postId}').onUpdate(listenToPostChanges)