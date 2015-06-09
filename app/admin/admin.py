from flask import Blueprint, request, g, redirect, url_for, abort, \
                  render_template

admin = Blueprint('admin', __name__, template_folder='templates')
