import datetime
import socket

def find_port(age):
    """
    fonction permettant de trouver un port en fonction de mon age et de lier le socket au port
    """
    port = 50000 + age
    while True:
        try:
            # Essayez de lier le socket au port
            server_socket.bind(('localhost', port))
            break
        except OSError as e:
                # si l'erreur 
                port += 100

# J'instencie mes informations
prenom = "Mathys"
age = 20

# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#utilise la fonction pour trouver le port et lier le socket au port
find_port(age)

# Active le mode d'écoute du socket
server_socket.listen(5)


# Mathys (Aka Grimkujow)
# https://pbs.twimg.com/media/F2YTCXSXAAAqlNv.jpg:large

try:

    # Accepter les connexions entrantes
    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie avec {client_address}")

    while True:
        
        # Recevoir le message du client
        message = client_socket.recv(1024).decode()
        print(f"Message reçu du client : {message}")

        # On regarde si le message n'est pas égale a date
        if(message[0:4] == "date"):
            # On prend la date actuelle
            date_actuelle = datetime.datetime.now()
            # On ne prend que la date et les heures
            date_et_heure = date_actuelle.strftime("%Y-%m-%d %H:%M:%S")
            # On met la date et l'heure dans le message
            message = "Date actuelle : "+ str(date_et_heure)

        # Ajouter une réponse au message
        message += " \nJe suis là !"

        # Envoyer la réponse au client
        client_socket.send(message.encode())
except ConnectionAbortedError:
     print("connection interrompue par le client")
     client_socket.close()