import requests

def client():

    """    ELIMINA UN RECORD DAL DATA BASE ISCRIZIONI
            credentials =  credenziali di autenticazione
            server      =  il server su cui gira l'applicazione
            endpoint    = l'endpoint
            id_to_delete = id record da eliminare
    """
    #blueberry-surprise-37969
    server = 'https://iscrizioneeventomc1965.herokuapp.com/'
    #    server = 'http://127.0.0.1:8000/'
    credentials = ('luigi','filippo92')
    id_to_delete = 4
    endpoint = server + 'api/iscrizioni/'+ str(id_to_delete) + '/delete'

#    METODO DELETE
    response = requests.delete(endpoint,auth=credentials)
    print("Response Status Code FOR DELETE   METHOD ", response.status_code)

if __name__ == '__main__':
    client()
