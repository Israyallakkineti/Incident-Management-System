from flask import Flask, render_template, request, redirect
from models import db, Incident

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

@app.route('/')
def index():
    incidents = Incident.query.all()
    return render_template('index.html', incidents=incidents)

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['description']

        incident = Incident(title=title,
                            description=desc,
                            status="Open",
                            assigned_to="Unassigned")

        db.session.add(incident)
        db.session.commit()

        return redirect('/')

    return render_template('create_incident.html')

@app.route('/resolve/<int:id>')
def resolve(id):
    incident = Incident.query.get(id)
    incident.status = "Resolved"
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000)
