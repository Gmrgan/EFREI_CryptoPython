from cryptography.fernet import Fernet
from flask import Flask, jsonify, render_template

app = Flask(__name__) #comm6

@app.route('/')
def hello_world():
    return render_template('index.html')

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

@app.route('/exo_4')
def exo_4():
    return render_template('exo_4.html')

@app.route('/exo_5')
def exo_5():
    return render_template('exo_5.html')

@app.route('/svg')
def svg():
    return render_template('svg.html')

@app.route('/maison')
def maison():
    return render_template('maison.html')

@app.route('/jack_club')
def jack_club():
    return render_template('jack_club.xml')

@app.route('/chenille')
def chenille():
    return render_template('chenille.html')

@app.route('/d6')
def d6():
    return render_template('Jeu_Des_Base.html')

@app.route('/outils_js')
def outils_js():
    return render_template('Outils_JS.html')

@app.route('/afficher_img')
def afficher_img():
    return render_template('afficher_img.html')

@app.route('/russian_roulette')
def russian_roulette():
    return render_template('russian_roulette.html')

if __name__ == "__main__":
    app.run(debug=True)
