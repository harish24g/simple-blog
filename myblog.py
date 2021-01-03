from flask import Flask,render_template,url_for
app = Flask(__name__)

posts = [
    {
        'author' : 'harish',
         'title' : 'post 1',
         'content': 'created my post!!!',
         'date_posted' : 'jan 3, 2021'
    },
    {
        'author' : 'roheth',
         'title' : 'post 2',
         'content': 'created my other post!!!',
         'date_posted' : 'jan 3, 2021'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')


if __name__  =='__main__' :
     app.run(debug=True)