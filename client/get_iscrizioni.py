import requests

def client():

    """    LEGGE TUTTI I RECORDS DEL  DATA BASE ISCRIZIONI
            credentials =  credenziali di autenticazione
            server      =  il server su cui gira l'applicazione
            endpoint    = l'endpoint che effettua l'operazione
    """
#    credentials = {"username": "luigi", "password": "filippo92"}
    credentials = ('luigi','filippo92')
    server = 'https://iscrizioneeventomc1965.herokuapp.com/'
    endpoint = server + 'api/iscrizioni/'

#    METODO GET
#    response = requests.get("http://127.0.0.1:8000/api/iscrizioni/",
    response = requests.get(endpoint, auth=credentials)
    print("Response Status Code FOR GET METHOD", response.status_code)
    response.data = response.json()
    print(response.data)


if __name__ == '__main__':
    client()
