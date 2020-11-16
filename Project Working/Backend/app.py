import pandas as pd
from flask import jsonify,Response,Flask
import os 
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app)

@app.route('/reply')
def predictQuery():
    try:
        query = 'hostel fees'
        files = os.listdir('./keywords')
        
        columns = ['Query']
        for name in files:
            columns.append(name.split('.')[0])
        
        df = pd.DataFrame(columns=columns)
        df['Query'] = [query]
        
        json = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

        for index,file in enumerate(files):
            json[index] = pd.read_json('./keywords/' + file, typ='series')
            
        for value,file in enumerate(json):
            for files in zip(file.keys(),file.values):
                for index,query in enumerate(df.Query):
                    if files[0].lower() in query.lower(): 
                        if df.iloc[index, [value+1]].isnull().values.any():
                            df.iloc[index, [value+1]] = files[1]
                        else:
                            df.iloc[index, [value+1]] = df.iloc[index, [value+1]].values[0] + files[1]

        labels = df.iloc[:,1:16].sum()
        total = labels.sum()

        final_value = {}
        for value in zip(labels.keys(),labels.values):
            final_value[value[0]] = (value[1]/total) * 100   
        
        highest = max(final_value, key=lambda k: final_value[k])
        return jsonify(final_value, highest)

    except Exception as e:
        print(str(e))
        return Response("No Internet Connection or server down")
