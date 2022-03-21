from flask import Flask, render_template, redirect

from controllers.member_controller import members_blueprint
from controllers.activity_controller import activities_blueprint
from controllers.booking_controller import bookings_blueprint

import repositories.activity_repository as activity_repository
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(activities_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title='Home Page')

@app.route('/site-map')
def site_map():
    return render_template('site_map.html', title='Sitemap')

# Function to delete absolutely everything
@app.route("/delete" , methods = ['POST'])
def delete_everything(id):
    booking_repository.delete_all()
    activity_repository.delete_all()
    member_repository.delete_all()
    return redirect ('/') # Redirect user back to the home page

if __name__ == '__main__':
    app.run(debug=True)