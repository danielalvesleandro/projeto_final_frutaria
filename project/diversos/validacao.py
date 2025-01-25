import re

# Função para validar id
def validar_id(id):
    if id.isdigit() and int(id) >= 0:
        return True, ""
    else:
        return False, "ID inválido. O ID deve ser um número inteiro não negativo."

# Função para validar nome
def validar_nome(nome):
    padrao_nome = r"^[A-ZÀ-ÿ][a-zà-ÿ'-]*(?: [A-ZÀ-ÿ][a-zà-ÿ'-]*)*$"
    if re.match(padrao_nome, nome):
        return True, ""
    else:
        return False, "Nome inválido. O nome deve começar com uma letra maiúscula e conter apenas letras, espaços, ou apóstrofos e hífens."

# Função para validar e-mail
def validar_email(email):
    padrao_email = r"^[a-z0-9]+([.-_][a-z0-9]+)*@[a-z0-9]+([.-][a-z0-9]+)*\.[a-z]{2,}$"
    if re.match(padrao_email, email):
        return True, ""
    else:
        return False, "E-mail inválido. O e-mail deve estar no formato: exemplo@dominio.com."

# Função para validar telefone
def validar_telefone(telefone):
    padrao_telefone = r"^[9][0-9]{8}$"
    if re.match(padrao_telefone, telefone):
        return True, ""
    else:
        return False, "Telefone inválido. O número deve começar com 9 e ter 9 dígitos."

# Função para validar NIF
def validar_nif(nif):
    padrao_nif = r"^[1-9][0-9]{8}$"
    if re.match(padrao_nif, nif):
        return True, ""
    else:
        return False, "NIF inválido. O NIF deve ter 9 dígitos e começar com um número de 1 a 9."

# Função para validar categoria
def validar_categoria(categoria):
    padrao_categoria = r"^[A-ZÀ-ÿ][a-zà-ÿ'-]*(?: [A-ZÀ-ÿ][a-zà-ÿ'-]*)*$"
    if re.match(padrao_categoria, categoria):
        return True, ""
    else:
        return False, "Categoria inválida. A categoria deve começar com uma letra maiúscula e conter apenas letras e espaços."

# Função para validar preço
def validar_preco(preco):
    padrao_preco = r"^\d+(\.\d{1,2})?$"
    if re.match(padrao_preco, preco):
        return True, ""
    else:
        return False, "Preço inválido. O preço deve ser um número com até duas casas decimais."

# Função para validar quantidade
def validar_quantidade(quantidade):
    padrao_quantidade = r"^\d+$"
    if re.match(padrao_quantidade, quantidade):
        return True, ""
    else:
        return False, "Quantidade inválida. A quantidade deve ser um número inteiro."
    
# Função para validar quantidade
def validar_endereco(endereco):
    padrao_endereco = r"^[A-Za-zÀ-ÿ0-9\s'-]*$"
    if re.match(padrao_endereco, endereco):
        return True, ""
    else:
        return False, "Endereço inválido. O endereço deve conter letras e números e iniciar com letra maiúscula."

