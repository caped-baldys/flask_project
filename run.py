from flask import Flask , render_template,request
import pandas as pd

posts = pd.read_csv(r'flask_project\Book1.csv',low_memory=False,encoding='windows-1254')


app = Flask(__name__)

size = len(posts)


@app.route('/'or '/home')
def home():

    return render_template('home.html',posts = posts,size=size)
        



@app.route("/search", methods=['GET', 'POST'])
def search():
    title = int(request.args.get('title'))
    print(title)
    # db = int(posts[posts['Pincode']==title].index())
    i = next(iter(posts[posts['Pincode']==title].index), 'no match')
    return render_template('search.html',title = title,posts=posts,i=i)



app.run(debug = True)