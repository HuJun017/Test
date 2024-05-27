from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('/workspace/Test/data/data.csv')

@app.route('/')
def homepage():
    nazioni = sorted(list(set(df['country'])))
    return render_template('homepage.html', elenco = nazioni)

@app.route('/elencoCItta/<nazione>', methods=['GET'])
def elencoCitta(nazione):
    nazioneSelezionata = df[df['country'] == nazione]
    citta = nazioneSelezionata['city'].value_counts().sort_values(ascending = False)
    return render_template('elencoCitta.html', elenco = citta)

@app.route('/elencoClienti', methods=['POST'])
def elencoClienti():
    cittaSelezionata = request.form.get('citta')
    print(cittaSelezionata)
    elenco = df[df['city'] == cittaSelezionata]
    elenco = elenco.to_html()
    return render_template('elencoClienti.html', elenco = elenco)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 3245, debug = True)