from flask import Flask, render_template, request, redirect, url_for
from joblib import load
from get_news import get_news 
import dotenv

dotenv.load_dotenv()
pipeline = load('negative_content_classifier.joblib')

def classification(name, debug=False):
    news_df = get_news(name)
    news_df['prediction'] = pipeline.predict(news_df['content'])
    predict_counts = str(news_df['prediction'].value_counts()) + '\n\n'

    if debug == True:
        print(f'Query text = "{name}"')
        print(predict_counts + str(news_df))

    return f'Query text is "{name}" \n\n' + predict_counts + str(news_df)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST', 'GET'])
def get_textQuery():
    if request.method == 'POST':
        user = request.form['search']

        return redirect(url_for('success', name=user))
    
@app.route('/success/<name>')
def success(name):
    return '<xmp>' + classification(name) + '</xmp>'

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', debug=True, port=5000)