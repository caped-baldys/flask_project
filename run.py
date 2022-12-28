from flask import Flask , render_template,request

app = Flask(__name__)


posts = [
    {   
        'author': 'Admin',
        'title': 'Dr.D Y Patil School of Science and Technology',
        'rating':'5',
        'content': 'Courses available: \n CS , AI&DS \n Contact:XXXX',
        'date_posted': 'JAN 20, 2022',
        'link':'https://www.dypsst.dpu.edu.in/',
        'image':'DYPSST'
    },
    {
        'author': 'Admin',
        'title': 'Dr.D Y Patil School',
        'rating':'5',
        'content': 'Courses available: \n CS , AI&DS \n Contact: XXXX',
        'date_posted': 'JAN 20, 2022',
        'image':'default'
    }
]

@app.route('/'or '/home')
def home():

    return render_template('home.html',posts = posts)
        



@app.route("/search", methods=['GET', 'POST'])
def search():
    title = request.args.get('title')
    return render_template('search.html',title = title,posts = posts)



app.run(debug = True)