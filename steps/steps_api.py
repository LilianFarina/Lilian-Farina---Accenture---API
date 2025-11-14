import time
# resposta deve retornar um userId
context.created_user = resp
# o demoqa costuma retornar campo 'userID' ou 'userId' - normalizar
context.user_id = resp.get('userID') or resp.get('userId') or resp.get('userID')


@when('eu gero um token para o usuário')
def step_impl(context):
user = context.user
resp = context.service.generate_token(user['username'], user['password'])
context.token_response = resp
context.token = resp.get('token') or resp.get('Token') or resp.get('accessToken')


@then('o usuário deve estar autorizado')
def step_impl(context):
auth = context.service.is_authorized()
# demoqa /Authorized retorna booleano true/false
assert auth is True or auth.get('authorized') is True


@when('eu recupero a lista de livros disponíveis')
def step_impl(context):
books_resp = context.service.list_books()
# normalmente retorna { 'books': [ ... ] }
context.books = books_resp.get('books') or books_resp
assert len(context.books) > 0


@when('eu escolho 2 livros e os adiciono à conta do usuário')
def step_impl(context):
# escolhe os dois primeiros ISBNS válidos
chosen = []
for b in context.books:
# alguns registros podem não ter 'isbn' dependendo da fonte
isbn = b.get('isbn') or b.get('ISBN') or b.get('isbn13')
if isbn:
chosen.append(isbn)
if len(chosen) == 2:
break
assert len(chosen) == 2, 'Não foi possível encontrar 2 livros com ISBNs'
context.chosen_isbns = chosen
add_resp = context.service.add_books_to_user(context.user_id, chosen, token=context.token)
context.add_response = add_resp


@then('ao recuperar os detalhes do usuário, devo ver os 2 livros reservados')
def step_impl(context):
details = context.service.get_user(context.user_id)
context.user_details = details
# DemoQA devolve campo 'books' na resposta do user
user_books = details.get('books') or []
isbns_in_user = [b.get('isbn') for b in user_books]
for isbn in context.chosen_isbns:
assert isbn in isbns_in_user
