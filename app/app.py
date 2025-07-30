from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>DevOps Project</title>
        <style>
            body {
                background-color: #282c34;
                color: white;
                text-align: center;
                font-family: Arial;
                margin-top: 100px;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Welcome to My Jenkins + Ansible + Docker Project!</h1>
        <p>Hi, I'm <strong>Anurag</strong> — an aspiring DevOps Engineer passionate about CI/CD, automation, and cloud-native tools.</p>
        <p>This is a Flask app deployed using a full CI/CD pipeline!</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)