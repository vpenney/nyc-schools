from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
app = Flask(__name__)

# this says: there is a sqlite database called schools.db in the directory
# if you have your db in the same directory, you need to use three forward slashes
# hook this into the app and use a variable called 'db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.db'
db = SQLAlchemy(app)

# this code, that Soma stole from the internet, tells sqlalchemy to 
# pull out the column titles (autodetect)


class School(db.Model):
  __tablename__ = 'schools'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  dbn = db.Column(db.String, primary_key=True)

@app.route("/")
def hello():
  schools = Schools.query.all()
  return render_template("list.html", schools=schools)

@app.route("/schools/")
def schools():
  schools = School.query.all()
  return render_template("list.html", schools=schools)


# our variable, dbn, is whatever is in the URL
@app.route("/schools/<dbn>/")
def school(dbn):
  school = School.query.filter_by(dbn=dbn).first()
  return render_template("show.html", school=school)

# @app.route("/search")
# def search():
#   # if you need a parameter from a form submission:
#   name = requests.args.get('query')
#   schools = School.query.filter(School.school_name.contains("henry")).all()
#   return render_template("list.html", schools=schools)

# @app.route("/school/01M539")
# def school():
#   # this is like SELECT * FROM schools, LIMIT 1
#   #school = School.query.first()
#   school = School.query.filter_by(dbn='01M539').first()
#   return render_template("show.html", school=school)




# If this is running from the command line
# do something
if __name__ == '__main__':
  app.run(debug=True)