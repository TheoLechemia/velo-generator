from flask import Blueprint, render_template
blueprint = Blueprint('socket', import_name="socket")

@blueprint.route('/', methods=['GET'])
def home():
    return render_template('home.html', name="Jack")
    
