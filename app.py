from flask import Flask
from views import main

app = Flask(__name__)

# Реєструємо Blueprint
app.register_blueprint(main)

@app.route('/')
def hello():
    return "Привіт, користувачу!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
