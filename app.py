from flask import Flask, render_template
from nba_api_routes import nba_api_bp

app = Flask(__name__)

app.register_blueprint(nba_api_bp, url_prefix='/nba')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/nba_page')
def nba_page():
    return render_template('nba_page.html')

if __name__ == '__main__':
    app.run(debug=True)