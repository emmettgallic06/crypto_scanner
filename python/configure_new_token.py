
import requests
def get_access_token():
    url ='https://api.polygonscan.com/api'
    client_id = "mealpricer-940ddd5f344ad0a2bde8913ee5b51b9d3823471200546567028"
    client_secret = "pqGNCYnGQ8lIrfAA69KJSTE9FhGhsNjFzzFFQuoG"
    response = requests.post(
        url,
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
    )
    return response.json()["access_token"]
