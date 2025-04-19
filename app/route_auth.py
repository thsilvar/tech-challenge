from flask import request, session
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required
from app.model.User import User
from app import db

auth_api = Namespace("Autenticação", description="Rotas para autenticação")

# Modelos para documentação Swagger
user_model = auth_api.model('User', {
    'username': fields.String(required=True, description='Nome de usuário', example='admin'),
    'password': fields.String(required=True, description='Senha do usuário', example='senha123')
})

token_response = auth_api.model('TokenResponse', {
    'access_token': fields.String(description='JWT de acesso')
})

message_response = auth_api.model('MessageResponse', {
    'msg': fields.String(description='Mensagem de status'),
})

msg_response = auth_api.model('MessageResponse', {
    'msg': fields.String(description='Mensagem da ação realizada')
})

error_response = auth_api.model('ErrorResponse', {
    'error': fields.String(description='Mensagem de erro'),
})

perfil_response = auth_api.model('PerfilResponse', {
    'usuario': fields.String(description='Usuário logado na sessão')
})


@auth_api.route('/register')
class Register(Resource):
    @auth_api.expect(user_model, validate=True)
    @auth_api.response(201, 'Usuário criado com sucesso', model=message_response)
    @auth_api.response(400, 'Usuário já existe', model=error_response)
    def post(self):
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first():
            return {"error": "User already exists"}, 400

        user = User(username=data['username'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        return {"msg": "User created"}, 201

@auth_api.route('/login')
class Login(Resource):
    @auth_api.expect(user_model, validate=True)
    @auth_api.response(200, 'Login bem sucedido', model=token_response)
    @auth_api.response(401, 'Credenciais inválidas', model=error_response)
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()

        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=str(user.id))

            session.permanent = True
            session['usuario'] = user.username
            session['user_id'] = user.id
            
            return {"access_token": access_token}, 200

        return {"error": "Invalid credentials"}, 401