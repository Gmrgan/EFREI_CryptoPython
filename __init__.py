from cryptography.fernet import Fernet
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Bienvenue sur votre API de cryptographie ! Utilisez les routes /encrypt et /decrypt." #comm5

@app.route('/encrypt', methods=['POST'])
def encryptage():
    try:
        # Récupérer les données JSON
        data = request.json
        valeur = data.get('valeur')  # Valeur à chiffrer
        key = data.get('key')  # Clé personnelle

        # Validation des données
        if not valeur or not key:
            return jsonify({"error": "Les champs 'valeur' et 'key' sont obligatoires."}), 400

        # Création de l'instance Fernet avec la clé fournie
        try:
            f = Fernet(key.encode())
        except Exception as e:
            return jsonify({"error": "Clé fournie invalide."}), 400

        # Chiffrement
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return jsonify({"encrypted_value": token.decode()})
    except Exception as e:
        return jsonify({"error": f"Erreur lors du chiffrement : {str(e)}"}), 500

@app.route('/decrypt', methods=['POST'])
def decryptage():
    try:
        # Récupérer les données JSON
        data = request.json
        token = data.get('token')  # Valeur à déchiffrer
        key = data.get('key')  # Clé personnelle

        # Validation des données
        if not token or not key:
            return jsonify({"error": "Les champs 'token' et 'key' sont obligatoires."}), 400

        # Création de l'instance Fernet avec la clé fournie
        try:
            f = Fernet(key.encode())
        except Exception as e:
            return jsonify({"error": "Clé fournie invalide."}), 400

        # Déchiffrement
        token_bytes = token.encode()
        valeur = f.decrypt(token_bytes)
        return jsonify({"decrypted_value": valeur.decode()})
    except Exception as e:
        return jsonify({"error": f"Erreur lors du déchiffrement : {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
