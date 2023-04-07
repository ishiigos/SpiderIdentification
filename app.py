from flask import Flask, jsonify, request
import bayes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

allSpiders = bayes.get_all_spiders()

@app.route('/api/v1/calculate_posterior', methods=['POST'])
def calculate_posterior():
    global allSpiders
    key = request.args.get('key')
    value = request.args.get('value')
    print(key, value)
    print(request)
    priors = request.json
    if allSpiders == None:
        allSpiders = bayes.get_all_spiders()    
    response = bayes.calculate_posterior(allSpiders, key, value, priors)
    return jsonify(response)

if __name__ == '__main__':
    print('Flask is running')
    # allSpiders = bayes.get_all_spiders()
    # response = bayes.calculate_posterior(allSpiders, "Sex", "Male", 1/1531)
    # print(response)
    app.run(debug=True)
else:
    print("run as module api")