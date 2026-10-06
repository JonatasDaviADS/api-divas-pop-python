from flask import Flask
from controllers.diva_controller import listar_divas, buscar_diva, criar_diva, atualizar_diva, deletar_diva
from flask_swagger_ui import get_swaggerui_blueprint
from flask import redirect

app = Flask(__name__)

SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'


swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': 'API Divas pop'}
)
app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)


@app.route('/')
def home():
    return redirect('/docs')


app.route('/divas', methods=['GET'])(listar_divas)
app.route('/divas/<int:id>', methods=['GET'])(buscar_diva)
app.route('/divas', methods=['POST'])(criar_diva)
app.route('/divas/<int:id>', methods=['PUT'])(atualizar_diva)
app.route('/divas/<int:id>', methods=['DELETE'])(deletar_diva)

if __name__ == '__main__':
    app.run(debug=True)
