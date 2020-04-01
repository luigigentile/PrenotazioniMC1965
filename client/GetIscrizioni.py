import requests

def client():

    """    PERMETTE DI EFFETTUARE OPERAZIONI CRUD SUL    Database

            credentials Sono le credenziali di autenticazione

    """
    credentials = {"username": "luigi", "password": "filippo92"}
#    METODO GET
    response = requests.get("http://127.0.0.1:8000/api/iscrizioni/",
                          data=credentials)
    print("Response Status Code FOR GET METHOD", response.status_code)
    response.data = response.json()
    print(response.data)

#    METODO POST
# URLS    eventi1 = si tratta dell'evento partita n.ro 1 iscrizione = si tratta di una nuova iscrizione
    nuova_iscrizione = {
    "nome": "Elena",
    "cognome": "Dal Corso",
    "telefono": "0347006237",
    "id_fermata": 5
    }
    response = requests.post("http://127.0.0.1:8000/api/eventi/1/iscrizione",
                          auth=('luigi', 'filippo92'),data=nuova_iscrizione)
    print("Response Status Code FOR POST  METHOD", response.status_code)
#    response.data = response.json()
#    print(response.data)

#    METODO DELETE
# URLS    eventi1 = si tratta dell'evento partita n.ro 1 iscrizione = si tratta di una nuova iscrizione
#    response = requests.delete("http://127.0.0.1:8000/api/iscrizioni/15/delete",
#                      auth=('luigi', 'filippo92'))
#    print("Response Status Code FOR DELETE   METHOD ", response.status_code)

#    METODO UPDATE
# URLS    eventi1 = si tratta dell'evento partita n.ro 1 iscrizione = si tratta di una nuova iscrizione
    iscrizione_to_update = {
    "id": 7,
    "nome": "Felice",
    "cognome": "Gentile",
    "id_fermata": 5
    }

    response = requests.put("http://127.0.0.1:8000/api/iscrizioni/7",
                        auth=('luigi', 'filippo92'),data=iscrizione_to_update)
    print("Response Status Code FOR UPDATE   METHOD ", response.status_code)






if __name__ == '__main__':
    client()
