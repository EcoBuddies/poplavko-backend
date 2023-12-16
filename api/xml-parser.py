import requests
from supabase import Client, create_client
from utils import parseXML


def fetch_and_insert_data():
    # Replace with the URL of your XML file
    response = requests.get('https://www.arso.gov.si/xml/vode/hidro_podatki_zadnji.xml')
    data = response.content

    # Replace with your Supabase URL and key
    url = "https://hqzppnbdbfpalptrrzas.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhxenBwbmJkYmZwYWxwdHJyemFzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDI2NzI4NTcsImV4cCI6MjAxODI0ODg1N30.mx5rnff6qF9P6qMF7CejkL4IxijBH3dJfojrZYi2S7w"
    client: Client = create_client(url, key) 
    table_meritve = client.table('meritev')
    table_postaja = client.table('postaja')

    unparsed_xml_data = response.content 
    
    # Extract json data from XML elements
    parsed_data = parseXML(unparsed_xml_data)

    # Insert data into Supabase table and where there is a string type of column "test" insert as varchar
    
    table_postaja.delete().neq('sifra', 0).execute()
    table_postaja.insert(parsed_data[0]).execute()
    table_meritve.insert(parsed_data[1]).execute()

if __name__ == '__main__':
    fetch_and_insert_data()