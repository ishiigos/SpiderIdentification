import copy
from flask import Flask, jsonify, request
import bayes
from flask_cors import CORS
import time 

app = Flask(__name__)
CORS(app)

start_api = time.perf_counter()
allSpiders = bayes.get_all_spiders()
completed_api = time.perf_counter() - start_api
print("Time to initialise = ", completed_api)

@app.route('/api/v1/calculate_posterior', methods=['POST'])
def calculate_posterior():
    global allSpiders
    calculation_start = time.perf_counter()
    key = request.args.get('key')
    value = request.args.get('value')
    print(key, value)
    print(request)
    priors = request.json
    if allSpiders == None:
        allSpiders = bayes.get_all_spiders() 
    allSpidersCopy = copy.deepcopy(allSpiders)
    response = bayes.calculate_posterior(allSpidersCopy.values(), key, value, priors)
    calculation_completed = time.perf_counter() - calculation_start
    print(f"The time to calculate for {key} and {value} is = ", calculation_completed)
    return jsonify(response)

@app.route('/api/v1/get_spider_details', methods=['GET'])
def get_spider_details():
    global allSpiders
    spiderSpeciesName = request.args.get('speciesName')
    spiderDetails = allSpiders[spiderSpeciesName]
    spiderProperties = spiderDetails.keys()
    selectedSpiderDetails = {}
    for property in spiderProperties:
        if(not (property.startswith('P(X |') or property.startswith('Sum P('))):
            selectedSpiderDetails[property] = spiderDetails[property]
    return jsonify(selectedSpiderDetails)

if __name__ == '__main__':
    print('Flask is running')
    # allSpiders = bayes.get_all_spiders()
    # response = bayes.calculate_posterior(allSpiders, "Sex", "Male", 1/1531)
    # print(response)
    app.run(debug=True)
else:
    print("run as module api")