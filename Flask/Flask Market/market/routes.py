
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables within the application context
    app.run(debug=True)
