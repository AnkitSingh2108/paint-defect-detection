from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Homepage():
    return render_template('index.html')

@app.route('/base')
def About():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)