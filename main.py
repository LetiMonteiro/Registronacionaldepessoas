from dados.banco import Banco

from modelos.documento_identidade import DocumentoIdentidade

from servicos.cadastro import Cadastro
from servicos.consulta import Consulta
from servicos.revogacao import Revogacao
from servicos.relatorios import Relatorios


banco = Banco()


while True:

    print("\n======================================")
    print(" SISTEMA DE REGISTRO NACIONAL")
    print("======================================")
    print("1 - Cadastrar Documento")
    print("2 - Buscar por Documento")
    print("3 - Buscar por Nome")
    print("4 - Listar Registros")
    print("5 - Revogar Documento")
    print("0 - Sair")
    print("======================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Nome: ")
        documento = input("Número do documento: ")
        foto = input("Foto: ")
        digital = input("Impressão digital: ")
        data = input("Data de emissão: ")

        pessoa = DocumentoIdentidade(
            nome,
            documento,
            foto,
            digital,
            data
        )

        Cadastro.cadastrar(banco, pessoa)

    elif opcao == "2":

        documento = input("Digite o documento: ")

        resultado = Consulta.buscar_por_documento(
            banco,
            documento
        )

        if resultado:
            print(resultado)
        else:
            print("Documento não encontrado.")

    elif opcao == "3":

        nome = input("Digite o nome: ")

        resultados = Consulta.buscar_por_nome(
            banco,
            nome
        )

        if len(resultados) > 0:

            for pessoa in resultados:
                print(pessoa)

        else:
            print("Nenhum registro encontrado.")

    elif opcao == "4":

        Relatorios.listar(banco)

        Relatorios.quantidade_tramites(banco)

    elif opcao == "5":

        documento = input("Digite o documento para revogar: ")

        Revogacao.revogar(
            banco,
            documento
        )

    elif opcao == "0":

        print("Sistema encerrado.")

        break

    else:

        print("Opção inválida.")

