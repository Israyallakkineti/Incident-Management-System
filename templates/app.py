from flask_mail import Mail, Message

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']='awsisrayal@gmail.com'
app.config['MAIL_PASSWORD']='Israyal@3534'

mail = Mail(app)
