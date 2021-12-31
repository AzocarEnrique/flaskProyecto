from flask import Blueprint
from controllers.UserController import index, store, store2, update, delete, store3, login, gestion, salas, mostrar, horario, mostrarhorario, autorizo

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)
user_bp.route('/ingresar', methods=['GET','POST'])(store)
user_bp.route('/opcion', methods=['GET','POST'])(store2)
user_bp.route('/ingresar2', methods=['GET','POST'])(store3)
user_bp.route('/login', methods=['GET','POST'])(login)
user_bp.route('/actualizar', methods=['GET','POST'])(update)
user_bp.route('/gestion', methods=['GET','POST'])(gestion)
user_bp.route('/salas', methods=['GET','POST'])(salas)
user_bp.route('/mostrarsalas', methods=['GET','POST'])(mostrar)
user_bp.route('/subirhorario', methods=['GET','POST'])(horario)
user_bp.route('/horario', methods=['GET','POST'])(mostrarhorario)
user_bp.route('/autorizo', methods=['GET','POST','DELETE'])(autorizo)
user_bp.route('/eliminar/<int:user_id>', methods=['DELETE'])(delete)
