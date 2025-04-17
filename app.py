from flask import Flask, request, jsonify
import youtube_dl
import base64
import os

app = Flask(__name__)

@app.route("/api/ytdl", methods=["POST"])
def download_video():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "Missing YouTube URL"}), 400

    output_path = "downloaded_video.mp4"
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_path,
        'merge_output_format': 'mp4',
        'quiet': True,
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        with open(output_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")

        os.remove(output_path)

        return jsonify({
            "base64": encoded
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
