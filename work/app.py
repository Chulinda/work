from flask import Flask, render_template, request
from work_data import get_data, get_pagination_number


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form.get('location')
        job = request.form.get('title')

        x,y,z,a = get_pagination_number(location,job)
        data = zip(x,y,z,a)
        

        
        # context = {'data':data}



        return render_template('index.html', data = data)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run()