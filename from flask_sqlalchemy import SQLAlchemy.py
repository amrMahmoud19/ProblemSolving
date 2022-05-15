from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#to start creating the database

app = Flask(__name__)
app.config['SECRET_KEY'] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
app.config['SQLALCHEMY'] = 'sqlite:///trial.db'

db = SQLAlchemy(app)

class AccountHolder(db.Model):

    id = db.Column(db.Integer, Primary_key = True) #Primarky_key = True making id as primary key
    UserName = db.Column(db.String(10), unique = True ) #passs unique = True to make it unique, to make datatype as string pass db.String
    Password = db.Column(db.String(60) ,  nullable=False )#, default= card number) #to not allow nulls , nullable = Flase

    #3shan a3ml relationship m3 table/relation tanya 
    Card = db.relationship('Card', backref='CardOwner',lazy = True) #backref deh htb2a el foreign key fe class el Card ely byreference ll class bta3 Account Holder


    def __repr__(self):
        return r"User: '{self.UserName}'"

class Card(db.Model):

    ccv = db.Column(db.String(3), nullable = False, unique = True)
    CardNo = db.Column(db.String(10), nullable = False, unique = True, Primary_key = True)
    Owner_id = db.Column(db.Integer, db.ForeignKey(accountHolder.id) , nullable = False) #account holder hkhaleha low case msh upper 3shan el default bta3 el table names byb2a lower case


    #ExpirationDate
