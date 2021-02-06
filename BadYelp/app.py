from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)#data base being initialize with app

# api_key='cEMSO47nzMpYTbNYQEplGnu9bbUvUl21WyG1YtxrsYMlXThj5nJxPE-eMA_V7FxWvPk1a8eVeDmsfBoMOZ29CILphvSnpk39Ix09YQovNHbcS8ypptHV471J7ywdYHYx'

# url = 'https://api.yelp.com/v3/businesses/search'
# params = {'term':'bookstore','location':'New York City'}

# headers = {'Authorization': 'Bearer %s' % api_key}
# req = requests.get(url, params=params, headers=headers)
 
# parsed = json.loads(req.text)
 
# businesses = parsed["businesses"]

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True) #takes in integer that will be the key
    content = db.Column(db.String(200), nullable=False)#nullable false means user cant leave content empty
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):#returns obkject in string format, invoked 
        return '<Task %r>' % self.id #everytime task is created will return id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']#gets content input from the form
        new_task = Todo(content=task_content)

        # for business in businesses:
        #     print("Name:", business["name"])

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()#query database by date created
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Error in deleting task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'ERROR in update'
    else:
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)