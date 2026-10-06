from config.db import get_db_connection


class Diva:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM divas")

        colunas = [coluna[0] for coluna in cursor.description]

        resultado = []
        for linha in cursor.fetchall():
            resultado.append(dict(zip(colunas, linha)))

        cursor.close()
        conn.close()
        return resultado

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM divas WHERE id = %s", (id,))
        linha = cursor.fetchone()

        resultado = None
        if linha:
            colunas = [coluna[0] for coluna in cursor.description]
            resultado = dict(zip(colunas, linha))

        cursor.close()
        conn.close()
        return resultado

    @staticmethod
    def create(nome, nacionalidade, ano_nascimento, maior_hit, premios_grammy, estilo):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO divas (nome, nacionalidade, ano_nascimento, maior_hit, premios_grammy, estilo) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nome, nacionalidade, ano_nascimento, maior_hit, premios_grammy, estilo)
        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def update(id, nome, nacionalidade, ano_nascimento, maior_hit, premios_grammy, estilo):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "UPDATE divas SET nome=%s, nacionalidade=%s, ano_nascimento=%s, maior_hit=%s, premios_grammy=%s, estilo=%s WHERE id=%s"
        valores = (nome, nacionalidade, ano_nascimento, maior_hit, premios_grammy, estilo, id)
        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM divas WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
