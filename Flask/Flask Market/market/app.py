############################################################# sqlite ########################

# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class Item(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False, unique=True)
#     price = db.Column(db.Integer, nullable=False)
#     barcode = db.Column(db.String(12), nullable=False, unique=True)
#     description = db.Column(db.String(1024), nullable=False, unique=True)

# @app.route('/')
# @app.route('/home')
# def home_page():
#     return render_template('home.html')

# @app.route('/market')
# def market_page():
#     items = Item.query.all()
#     return render_template('market.html', items=items)

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()  # Create database tables within the application context
#     app.run(debug=True)


######################################################## mysql #############################

from flask import Flask, render_template


app = Flask(__name__)
# Update the URI to use MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/market_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


