import requests

def client():

    """    AGGIORNA UN RECORD DEL  DATA BASE ISCRIZIONI
            credentials =  credenziali di autenticazione
            server      =  il server su cui gira l'applicazione
            endpoint    = l'endpoint
            iscrizione_to_update = record da aggiornare in formato json
            id_to_update = id del record da aggiornare
    """


    server = 'https://iscrizioneeventomc1965.herokuapp.com/'
#    server = 'http://127.0.0.1:8000/'
    credentials = ('luigi','filippo92')
    id_to_update = 4
    endpoint = server + 'api/iscrizioni/'+ str(id_to_update)
#    METODO PUT
    iscrizione_to_update = {
    "id": id_to_update,
    "nome": "Luigi",
    "cognome": "Gentile",
    "id_fermata": 1
    }

    response = requests.put(endpoint,auth=credentials,data=iscrizione_to_update)
    print("Response Status Code FOR UPDATE   METHOD ", response.status_code)

if __name__ == '__main__':
    client()
