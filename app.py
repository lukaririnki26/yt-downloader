from flask import Flask, request, jsonify
import yt_dlp
import base64
import os

app = Flask(__name__)


@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        output_file = 'downloaded_video.mp4'

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            'outtmpl': output_file,
            'merge_output_format': 'mp4',
            'noplaylist': True,
            'quiet': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        with open(output_file, 'rb') as f:
            encoded_string = base64.b64encode(f.read()).decode('utf-8')

        os.remove(output_file)

        return jsonify({
            'title': info.get('title'),
            'base64_video': encoded_string
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route("/")
def home():
    return "Hello from Flask on Replit!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
