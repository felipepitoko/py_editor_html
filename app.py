from flask import Flask
from flask import jsonify, request
from leitor import LeitorUrl

app = Flask(__name__)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=False) #<-- esta configuração deve ser feita, setar host='0.0.0.0'

@app.route("/")
def index():
    return "Hello World!"

# @app.route('/v1', methods=["GET"])
# def info_view():
#     """List of routes for this API."""
#     output = {
#         'info': 'GET /api/v1',
#         'register': 'POST /api/v1/accounts',
#         'single profile detail': 'GET /api/v1/accounts/<username>',
#         'edit profile': 'PUT /api/v1/accounts/<username>',
#         'delete profile': 'DELETE /api/v1/accounts/<username>',
#         'login': 'POST /api/v1/accounts/login',
#         'logout': 'GET /api/v1/accounts/logout',
#         "user's tasks": 'GET /api/v1/accounts/<username>/tasks',
#         "create task": 'POST /api/v1/accounts/<username>/tasks',
#         "task detail": 'GET /api/v1/accounts/<username>/tasks/<id>',
#         "task update": 'PUT /api/v1/accounts/<username>/tasks/<id>',
#         "delete task": 'DELETE /api/v1/accounts/<username>/tasks/<id>'
#     }
#     return jsonify(output)

@app.route('/scrap',methods=["GET"])
def gerarBoleto():
    tag_pesquisa = request.args.get('tag')
    url_pesquisa = request.args.get("url")

    print(tag_pesquisa,url_pesquisa)

    texto_tag = LeitorUrl.buscarTag(url_pesquisa,tag_pesquisa)

    return jsonify({
        "tag_pesquisa": tag_pesquisa,
        "url_pesquisa": url_pesquisa,
        "qtd_ocorrencias": len(texto_tag), 
        "primeiro_resultado": texto_tag[0],
        "segundo_resultado": texto_tag[1]})