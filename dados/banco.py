```python
import sqlite3
import json


class Banco:
    def __init__(self, caminho_db="sistema_registro.db"):
        self.__caminho = caminho_db
        self.__criar_tabelas()

    def __conectar(self):
        """
        Cria e retorna uma conexão com o banco de dados SQLite.
        """
        conexao = sqlite3.connect(self.__caminho)
        conexao.row_factory = sqlite3.Row
        return conexao

    def __criar_tabelas(self):
        """
        Cria a tabela principal caso ela ainda não exista.
        """
        with self.__conectar() as con:
            cur = con.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS tramites (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT NOT NULL,
                    nome TEXT NOT NULL,
                    documento TEXT UNIQUE NOT NULL,
                    foto TEXT,
                    digital TEXT,
                    data_emissao TEXT,
                    extras TEXT
                )
            """)

            con.commit()

    # ==========================================================
    # MÉTODOS PÚBLICOS
    # ==========================================================

    def inserir(self, tramite):
        """
        Insere um novo trâmite no banco.
        """

        tipo = tramite.__class__.__name__
        extras = self.__extras_para_dict(tramite, tipo)

        try:
            with self.__conectar() as con:
                cur = con.cursor()

                cur.execute("""
                    INSERT INTO tramites (
                        tipo,
                        nome,
                        documento,
                        foto,
                        digital,
                        data_emissao,
                        extras
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    tipo,
                    tramite.nome,
                    tramite.documento,
                    tramite.foto,
                    tramite.digital,
                    tramite.data_emissao,
                    json.dumps(extras)
                ))

                con.commit()

                return True

        except sqlite3.IntegrityError:
            print("Erro: documento já cadastrado.")
            return False

    def buscar_por_documento(self, documento):
        """
        Busca um registro pelo documento.
        """

        with self.__conectar() as con:
            cur = con.cursor()

            cur.execute("""
                SELECT *
                FROM tramites
                WHERE documento = ?
            """, (documento,))

            resultado = cur.fetchone()

        if resultado:
            return self.__row_para_objeto(resultado)

        return None

    def buscar_por_nome(self, nome):
        """
        Busca registros contendo parte do nome.
        """

        with self.__conectar() as con:
            cur = con.cursor()

            cur.execute("""
                SELECT *
                FROM tramites
                WHERE nome LIKE ?
                ORDER BY nome
            """, (f"%{nome}%",))

            resultados = cur.fetchall()

        return [self.__row_para_objeto(r) for r in resultados]

    def buscar_por_tipo(self, tipo):
        """
        Busca todos os registros de um determinado tipo.
        """

        with self.__conectar() as con:
            cur = con.cursor()

            cur.execute("""
                SELECT *
                FROM tramites
                WHERE tipo = ?
                ORDER BY nome
            """, (tipo,))

            resultados = cur.fetchall()

        return [self.__row_para_objeto(r) for r in resultados]

    def listar_todos(self):
        """
        Lista todos os registros cadastrados.
        """

        with self.__conectar() as con:
            cur = con.cursor()

            cur.execute("""
                SELECT *
                FROM tramites
                ORDER BY id DESC
            """)

            resultados = cur.fetchall()

        return [self.__row_para_objeto(r) for r in resultados]

    def atualizar_data_emissao(self, documento, nova_data):
        """
        Atualiza a data de emissão de um documento.
        """

        with self.__conectar() as con:
            cur = con.cursor()

            cur.execute("""
                UPDATE tramites
                SET data_emissao = ?
                WHERE documento = ?
            """, (nova_data, documento))

            con.commit()

            return cur.rowcount > 0

    def remover(self, documento):
        """
        Remove um registro pelo documento.
        """

        with self.__conectar() as con:
            cur = con.cursor()

            cur.execute("""
                DELETE FROM tramites
                WHERE documento = ?
            """, (documento,))

            con.commit()

            return cur.rowcount > 0

    def contar_por_tipo(self):
        """
        Retorna a quantidade de registros por tipo.
        """

        with self.__conectar() as con:
            cur = con.cursor()

            cur.execute("""
                SELECT tipo, COUNT(*) AS quantidade
                FROM tramites
                GROUP BY tipo
            """)

            resultados = cur.fetchall()

        return {
            linha["tipo"]: linha["quantidade"]
            for linha in resultados
        }

    # ==========================================================
    # MÉTODOS AUXILIARES
    # ==========================================================

    @staticmethod
    def __extras_para_dict(tramite, tipo):
        """
        Converte os atributos específicos de cada classe
        para um dicionário.
        """

        extras = {}

        if tipo == "AutorizacaoResidencia":

            extras["pais_origem"] = tramite.pais_origem
            extras["data_vencimento"] = tramite.data_vencimento

        elif tipo == "AutorizacaoRefugio":

            extras["pais_origem"] = tramite.pais_origem
            extras["motivo_refugio"] = tramite.motivo_refugio

        return extras

    @staticmethod
    def __row_para_objeto(row):
        """
        Reconstrói um objeto a partir dos dados do banco.
        """

        from src.modelos.documento_id import DocumentoIdentidade
        from src.modelos.autorizacao_residencia import AutorizacaoResidencia
        from src.modelos.autorizacao_refugio import AutorizacaoRefugio

        tipo = row["tipo"]
        nome = row["nome"]
        documento = row["documento"]
        foto = row["foto"]
        digital = row["digital"]
        data_emissao = row["data_emissao"]

        extras = {}

        if row["extras"]:
            extras = json.loads(row["extras"])

        if tipo == "DocumentoIdentidade":

            return DocumentoIdentidade(
                nome,
                documento,
                foto,
                digital,
                data_emissao
            )

        elif tipo == "AutorizacaoResidencia":

            return AutorizacaoResidencia(
                nome,
                documento,
                foto,
                digital,
                data_emissao,
                extras.get("pais_origem", ""),
                extras.get("data_vencimento", "")
            )

        elif tipo == "AutorizacaoRefugio":

            return AutorizacaoRefugio(
                nome,
                documento,
                foto,
                digital,
                data_emissao,
                extras.get("pais_origem", ""),
                extras.get("motivo_refugio", "")
            )

        return None
```
