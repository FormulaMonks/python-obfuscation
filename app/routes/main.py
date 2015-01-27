from numpy import matrix
from flask import Blueprint, jsonify, request

from utils import render_to


main = Blueprint('calc', __name__)


@main.route('/')
@render_to('main.html')
def calc_form():
    pass


@main.route('/calc')
def calc():
    matrix1 = matrix(request.args['m1'].encode('utf8'))
    matrix2 = matrix(request.args['m2'].encode('utf8'))
    out = {'result': str(matrix1 * matrix2)}
    return jsonify(out)
