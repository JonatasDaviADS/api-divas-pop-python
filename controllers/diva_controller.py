from flask import jsonify, request
from models.diva import Diva


def listar_divas():
    try:
        dados = Diva.get_all()
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


def buscar_diva(id):
    try:
        dados = Diva.get_by_id(id)
        if dados:
            return jsonify(dados), 200
        return jsonify({"mensagem": "Diva não encontrada."}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


def criar_diva():
    try:
        dados = request.get_json()
        Diva.create(
            dados['nome'], dados['nacionalidade'], dados['ano_nascimento'],
            dados['maior_hit'], dados['premios_grammy'], dados['estilo']
        )
        return jsonify({"mensagem": "Diva cadastrada com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


def atualizar_diva(id):
    try:
        dados = request.get_json()
        Diva.update(
            id, dados['nome'], dados['nacionalidade'], dados['ano_nascimento'],
            dados['maior_hit'], dados['premios_grammy'], dados['estilo']
        )
        return jsonify({"mensagem": "Diva atualizada com sucesso!"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


def deletar_diva(id):
    try:
        Diva.delete(id)
        return jsonify({"mensagem": "Diva excluída com sucesso!"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
