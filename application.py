'''
Resume app Uses Elastic Beanstalk, RDS and Flask

Author: Paul Godin godin.paul@gmail.com

'''

from flask import Flask, render_template, request
from application import db, models
from application.models import *
from application.forms import EnterDBInfo, RetrieveDBInfo

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'   

@application.route('/')
@application.route('/index')

def index():
  try:
    results = models.Summary.query.all()
    for u in results:
      print(u.details)
    db.session.close()
  except:
    db.session.rollback()
  return render_template('index.html', 
                            details=u.details,
                            title='Paul J Godin')

@application.route('/projects')

def projects():
  try:
    results = models.Projects.query.all()
    for u in results:
      print(u.details)
    db.session.close()
  except:
    db.session.rollback()
  return render_template('projects.html', 
                            details=u.details,
                            title='Paul J Godin - Projects')

@application.route('/whoami')

def whoami():   
  try:
    results = models.Whoami.query.all()
    for u in results:
      print(u.details)
    db.session.close()
  except:
    db.session.rollback()
  return render_template('whoami.html',
                            details=u.details,
                            title='Paul J Godin - Who Am I')

@application.route('/experience')

def experience():
  try:
    result = models.Experience.query.all()
    for u in result:
      jobid=u.id
      company=u.company
      jobtitle=u.jobtitle
      when=u.when
      details=u.details
    db.session.close()
  except:
    db.session.rollback()
  return render_template('experience.html',
                          results = result,
                          title='Paul J Godin - Experience')

@application.route('/education')

def education():
  try:
    results = models.Education.query.all()
    for u in results:
      print(u.details)
    db.session.close()
  except:
    db.session.rollback()
  return render_template('education.html',
                            details=u.details,
                            title='Paul J Godin - Education')

@application.route('/about')

def about():
  try:
    results = models.About.query.all()
    for u in results:
      print(u.details)
    db.session.close()
  except:
    db.session.rollback()
  return render_template('about.html', 
                            details=u.details,
                            title='Paul J Godin - About')

  
if __name__ == '__main__':
    application.run(host='0.0.0.0')
