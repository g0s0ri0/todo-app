from flask import Blueprint, jsonify, request
from . import db
from .models import Task

main = Blueprint('main', __name__)

@main.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@main.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

# ... (endpoints para editar, borrar y marcar como completada)
