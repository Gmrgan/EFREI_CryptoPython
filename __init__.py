from cryptography.fernet import Fernet
from flask import Flask, jsonify, render_template

app = Flask(__name__) #comm6

@app.route('/')
def hello_world():
    return "Bienvenue sur votre API de cryptographie ! Utilisez les routes /encrypt/<valeur>/<key> et /decrypt/<token>/<key>."

@app.route('/encrypt/<valeur>/<key>')
def encryptage(valeur, key):
    try:
        # Création de l'instance Fernet avec la clé fournie
        try:
            f = Fernet(key.encode())
        except Exception:
            return jsonify({"error": "Clé fournie invalide. Assurez-vous qu'elle est au format base64."}), 400

        # Chiffrement de la valeur
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return jsonify({"encrypted_value": token.decode()})
    except Exception as e:
        return jsonify({"error": f"Erreur lors du chiffrement : {str(e)}"}), 500

@app.route('/decrypt/<token>/<key>')
def decryptage(token, key):
    try:
        # Création de l'instance Fernet avec la clé fournie
        try:
            f = Fernet(key.encode())
        except Exception:
            return jsonify({"error": "Clé fournie invalide. Assurez-vous qu'elle est au format base64."}), 400

        # Déchiffrement du token
        token_bytes = token.encode()
        valeur = f.decrypt(token_bytes)
        return jsonify({"decrypted_value": valeur.decode()})
    except Exception as e:
        return jsonify({"error": f"Erreur lors du déchiffrement : {str(e)}"}), 500

# Routes pour les fichiers HTML
@app.route('/exo_1')
def exo_1():
    return render_template('exo_1.html')

@app.route('/exo_2')
def exo_2():
    return render_template('exo_2.html')

@app.route('/exo_3')
def exo_3():
    return render_template('exo_3.html')

if __name__ == "__main__":
    app.run(debug=True)
