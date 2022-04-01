from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Joaquim', idade=40)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Mateus').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Mateus').first()
    pessoa.idade = 30
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Mateus').first()



if __name__ == '__main__':
    # insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()

