
import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def propiedades():
    url = f'https://witei.com/api/v1/houses/'
    headers = {'Authorization': 'Bearer 7a54f9633cf443d988c0c49e2b77989b'}
    response = requests.get(url, headers=headers)
    data = response.json()
    propiedades_disponibles = [prop for prop in data['results'] if prop['status'] == 'disponible']
    return render_template('propiedades.html', propiedades=propiedades_disponibles)

@app.route('/propiedad/<prop_id>')
def propiedad_detalle(prop_id):
    url = f'https://witei.com/api/v1/houses/?identifier={prop_id}'
    headers = {'Authorization': 'Bearer 7a54f9633cf443d988c0c49e2b77989b'}
    response = requests.get(url, headers=headers)
    data = response.json()
    if data['count'] > 0:
        propiedad = data['results'][0]
        return render_template('propiedad_detalle.html', detalle=[propiedad])
    else:
        return 'Propiedad no encontrada'



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
