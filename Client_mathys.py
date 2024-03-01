import socket

prenom = "Mathys"

# Création du socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Adresse et port du serveur
server_address = ('localhost', 50020)

# Établir la connexion avec le serveur
client_socket.connect(server_address)

# Ecris et envoie le message au serveur
requete = f"Serveur es-tu là, tu vas bien, je m’appelle {prenom} ?"
client_socket.sendall(requete.encode())

# Recevoir la réponse du serveur
reponse = client_socket.recv(1024).decode()
print(f"Réponse du serveur : {reponse}")

# Mathys (Aka Grimkujow)
# https://pbs.twimg.com/media/F2YTCXSXAAAqlNv.jpg:large

while True:
    # Lire l'entrée utilisateur
    message = input("Entrez votre message (ou 'exit' pour quitter) : ")

    # Vérifier si l'utilisateur veut quitter
    if message.lower() == "je sui a laeropor bisouuuu je manvol" or message.lower() == "exit":
        print("Déconnexion...")
        break

    # Transmettre la requête au serveur
    requete = f"{message} {prenom}"
    client_socket.sendall(requete.encode())

    # Recevoir la réponse du serveur (la valeur 1024 spécifie la taille maximale des données à recevoir en octets )
    reponse = client_socket.recv(1024).decode()
    print(f"Réponse du serveur : {reponse}")

# Interrompre la connexion
client_socket.close()
