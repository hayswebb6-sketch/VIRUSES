from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

password=os.environ.get('password')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_password = request.form.get('password')
        if user_password == password:
            return send_from_directory(
                "dist","NO_INPUT.exe", as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))