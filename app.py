from flask import Flask, render_template
from data import SourceData
from back import back_bp, start_threads
app = Flask(__name__)
app.register_blueprint(back_bp)

@app.route('/')
def index():
    data = SourceData()
    start_threads()
    return render_template('index.html', form=data, title='空间利用率情况展示')


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=False)
