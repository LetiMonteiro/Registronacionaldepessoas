class Relatorios:

    @staticmethod
    def quantidade_tramites(banco):

        print(f"Total de registros: {len(banco.registros)}")

    @staticmethod
    def listar(banco):

        for pessoa in banco.registros:

            print(pessoa)
