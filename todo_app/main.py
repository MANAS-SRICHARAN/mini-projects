from flask import Flask,request,url_for,redirect,render_template
import datetime 
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
"""
database configuration
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	task = db.Column(db.String(300),nullable=False)
	date= db.Column(db.DateTime,nullable=False)
	completion = db.Column(db.Boolean,nullable=False)

	def __init__(self,task_name,time_stamp,completion):
		self.task = task_name
		self.date = time_stamp
		self.completion= completion
		



@app.route('/')
def index():
	return(render_template('index.html'))

@app.route('/submit',methods=['POST','GET'])
def root():
	
	if request.method =='POST':
		task_name = request.form['task']
		time_stamp = datetime.datetime.now()#strftime('%Y-%m-%d:%H-%M-%s')
		completion = 0 #false, as sqlite3 doest understand boolean
		#let the database create the primary auto increament id 
		new_task = Todo(task_name,time_stamp,completion)
		
		db.session.add(new_task)
		db.session.commit()
		return redirect(url_for('index'))
		#except:
		#	return 'there is an issue'
	else:
		pass


@app.route('/update',methods=['POST','GET'])
def update():
	if request.method=='POST':
		if len(list(request.form.keys())) == 1:
			tasks=Todo.query.order_by(Todo.date).all()
			return render_template('index.html',tasks=tasks)
		else:
			update_ids = request.form
			update_ids=[int(val) for val in update_ids.values() if val !="refresh"]
			
			db.session.execute(db.update(Todo).where(Todo.id.in_(update_ids)).values(completion=1))
			db.session.commit()
			tasks=Todo.query.order_by(Todo.date).all()
			return render_template('index.html',tasks=tasks)


	
if __name__=="__main__":
	with app.app_context():	
		db.create_all()
	app.run(debug=True)

