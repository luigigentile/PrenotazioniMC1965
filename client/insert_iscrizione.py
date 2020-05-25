import requests

def client():

    """    INSERISCE UN NUOVO RECORD NEL DATA BASE ISCRIZIONI
            credentials =  credenziali di autenticazione
            server      =  il server su cui gira l'applicazione
            endpoint    = l'endpoint che effettua l'operazione
            nuova_iscrizione = record da inserire  in formato json
            id_evento = l'id dell'evento in cui verrà inserito il nuovo record
    """
    credentials = ('luigi','filippo92')
    server = 'https://iscrizioneeventomc1965.herokuapp.com/'
    id_evento = 1
    endpoint = server + 'api/eventi/'+str(id_evento)+'/iscrizione'

#    METODO POST
# URLS    eventi1 = si tratta dell'evento partita n.ro 1 iscrizione = si tratta di una nuova iscrizione
    nuova_iscrizione = {
    "nome": "Elena",
    "cognome": "Dal Corso",
    "telefono": "0347006237",
    "id_fermata": 4
    }

    response = requests.post(endpoint,auth=credentials,data=nuova_iscrizione)

    print("Response Status Code FOR POST  METHOD", response.status_code)
    response.data = response.json()
    print(response.data)

if __name__ == '__main__':
    client()
