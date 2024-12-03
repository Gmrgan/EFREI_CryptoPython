from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')  # Comm4

@app.route('/encrypt', methods=['POST'])
def encryptage():
    try:
        # Récupération des données JSON
        data = request.json
        valeur = data.get('valeur')  # Valeur à chiffrer
        key = data.get('key')  # Clé personnelle

        # Validation des données
        if not valeur or not key:
            return "Erreur : 'valeur' et 'key' sont requis.", 400
        
        # Vérification de la validité de la clé
        try:
            f = Fernet(key.encode())
        except Exception:
            return "Erreur : clé invalide.", 400

        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        token = f.encrypt(valeur_bytes)  # Encrypt la valeur
        return jsonify({"encrypted_value": token.decode()})  # Retourne le token en JSON
    except Exception as e:
        return f"Erreur : {str(e)}", 500

@app.route('/decrypt', methods=['POST'])
def decryptage():
    try:
        # Récupération des données JSON
        data = request.json
        token = data.get('token')  # Valeur à déchiffrer
        key = data.get('key')  # Clé personnelle

        # Validation des données
        if not token or not key:
            return "Erreur : 'token' et 'key' sont requis.", 400
        
        # Vérification de la validité de la clé
        try:
            f = Fernet(key.encode())
        except Exception:
            return "Erreur : clé invalide.", 400

        token_bytes = token.encode()  # Conversion str -> bytes
        valeur = f.decrypt(token_bytes)  # Décryptage du token
        return jsonify({"decrypted_value": valeur.decode()})  # Retourne la valeur décryptée en JSON
    except Exception as e:
        return f"Erreur : {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
