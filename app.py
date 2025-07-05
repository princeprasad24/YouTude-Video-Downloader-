from flask import Flask , request , render_template , send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/' , methods=['GET', 'POST'])

def index():
    message = ""
    if request.method == "POST":
        link = request.form['link']
        fileName = "download.mp4"
        message = "Downloading..."

        ydl_opts = {
            'format' : "best",
            'outtmpl' : fileName,
            'quiet': True
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            message = "Downloaded!"
            return send_file(fileName , as_attachment=True)
        except:
            message = "Download failed. Please try again. "
    
    return render_template('index.html' , message = message)
        
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False  , port=port , host="0.0.0.0")