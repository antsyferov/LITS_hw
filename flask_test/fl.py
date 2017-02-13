from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    lst = ['john', 'jane', 'marry', '', None]
    return render_template('index.html', people=lst)

if __name__ == '__main__':
    app.run()