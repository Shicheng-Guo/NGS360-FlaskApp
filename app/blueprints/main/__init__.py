'''
Main application endpoints
'''
from flask import Blueprint, render_template, request, session, jsonify, current_app
from flask_login import login_required
from app import project_registry

BP = Blueprint('main', __name__)

@BP.route('/')
@login_required
def index():
    '''
    Home Page URL: /
    '''
    return render_template('main/index.html')

@BP.route("/basespace")
@login_required
def show_basespace():
    ''' Show Basespace page '''
    return render_template('main/basespace.html')

@BP.route("/jobs")
@login_required
def show_batch_jobs():
    ''' Show user jobs '''
    if 'username' in request.args:
        username = request.args.get('username')
    elif 'username' in session:
        username = session['username']
    else:
        username = None
    return render_template('main/jobs.html', username=username)

@BP.route("/illumina_runs")
@login_required
def show_illumina_runs():
    ''' Show Illumina Runs page '''
    return render_template('main/illumina_runs.html')

@BP.route("/projects")
@login_required
def show_projects():
    ''' Show Projects page '''
    return render_template('main/projects.html')

# TODO: Move this to a REST Endpoint
@BP.route("/projectregistry_json")
def projectregistry_json():
    '''
    Returns a json list of all projects in ProjectRegistry, optionally
    limited to specific fields
    :param fields: comma-seperated list of fields to retrieve
    :return: JSON list of projects
    '''
    pr_url = current_app.config['PROJECTREGISTRY']
    if 'fields' in request.args:
        fields = request.args.get('fields').split(",")
        return jsonify(project_registry.get_projects(pr_url, fields))
    return jsonify(project_registry.get_projects(pr_url))