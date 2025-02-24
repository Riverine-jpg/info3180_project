"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for,flash,send_from_directory
from .forms import PropForm
from werkzeug.utils import secure_filename
from app.models import Properties
from . import db
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create',methods=['POST', 'GET'])
def create():
    form = PropForm()
    if request.method =='POST':
        print("ydadadsaes")
        print(form.validate_on_submit())
        if form.validate_on_submit():
            print("yes")
            filename = secure_filename(form.photo.data.filename)
            form.photo.data.save(app.config['UPLOAD_FOLDER'] + '/' + filename)
            property = Properties(form.ptitle.data,form.desc.data,form.rooms.data,form.brooms.data,form.price.data,form.ptype.data,form.locat.data,filename)
            db.session.add(property)
            db.session.commit()
            flash("works", "Success")
            
            return render_template('properties.html',get_image= get_image,prop = Properties.query.all())
    return render_template("create.html",form=form)

@app.route('/properties')
def properties():
    return render_template('properties.html',get_image= get_image,prop = Properties.query.all())

@app.route('/properties/<id>')
def oneprop(id):
    return render_template("pview.html", prop = Properties.query.filter_by(id=id).first())

@app.route('/pimages/<id>')
def get_image(id):
    prop = Properties.query.filter_by(id=id).first()
    print(prop)
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), path=prop.photo)
    

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
