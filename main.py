from dados.banco import Banco

from modelos.documento_identidade import DocumentoIdentidade

from servicos.cadastro import Cadastro
from servicos.relatorios import Relatorios


banco = Banco()


pessoa = DocumentoIdentidade(
    "João Silva",
    "123456789",
    "foto.jpg",
    "digital.png",
    "16/06/2026"
)


Cadastro.cadastrar(banco, pessoa)

Relatorios.listar(banco)

Relatorios.quantidade_tramites(banco)

