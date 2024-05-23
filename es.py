from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('/workspace/Test/data/data.csv')

@app.route('/')
def homepage():
    nazioni = df['country'].drop_duplicates()
    return render_template('homepage.html', elenco=nazioni)

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('/workspace/Test/data/data.csv')

@app.route('/')
def homepage():
    nazioni = df['country'].unique()
    return render_template('homepage.html', elenco=nazioni)

@app.route('/elencoCitta', methods=['POST'])
def elencoCitta():
    nazioneSelezionata = request.form.get('nazione')
    citta = df[df['country'] == nazioneSelezionata].groupby('city').size().sort_values(ascending=False)
    elenco = pd.DataFrame({'city': citta.index, 'num_clients': citta.values})
    print(elenco)
    return render_template('elencoCitta.html', elenco=elenco)

@app.route('/elencoClienti', methods=['POST'])
def elencoClienti():
    cittaSelezionata = request.form.get('citta')
    print(cittaSelezionata)
    elenco = df[df['city'] == cittaSelezionata]
    elenco = elenco.to_html()
    return render_template('elencoClienti.html', elenco = elenco)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 3245, debug = True)