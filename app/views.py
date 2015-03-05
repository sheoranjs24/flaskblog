from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Jyoti'}  # fake user
    posts = [ # fake array of posts
             {
                'author': {'nickname': 'John'},
                'body': 'Beautiful day in Victoria!'
              },
             {
                'author': {'nickname': 'Susan'},
                'body': 'The Avatar movie was so cool!'
              }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

