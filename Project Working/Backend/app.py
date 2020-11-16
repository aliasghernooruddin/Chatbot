import pdb
from flask import Flask, jsonify, Response, request
import os
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
from flask_cors import CORS
import json
import pandas as pd

cred = credentials.Certificate("./firebase-credentials.json")

FIRESTORE = firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)

CORS(app)


@app.route('/reply', methods=['POST'])
def predictQuery():
    try:
        data = request.json

        files = os.listdir('./keywords')

        columns = ['Query']
        for name in files:
            columns.append(name.split('.')[0])

        df = pd.DataFrame(columns=columns)
        df['Query'] = [data['query']]

        dictionary = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        for index, file in enumerate(files):
            dictionary[index] = pd.read_json(
                './keywords/' + file, typ='series')

        for value, file in enumerate(dictionary):
            for files in zip(file.keys(), file.values):
                for index, query in enumerate(df.Query):
                    if files[0].lower() in query.lower():
                        if df.iloc[index, [value+1]].isnull().values.any():
                            df.iloc[index, [value+1]] = files[1]
                        else:
                            df.iloc[index, [value+1]] = df.iloc[index,
                                                                [value+1]].values[0] + files[1]

        labels = df.iloc[:, 1:17].sum()
        total = labels.sum()

        final_value = {}
        for value in zip(labels.keys(), labels.values):
            final_value[value[0]] = (value[1]/total) * 100

        highest = max(final_value, key=lambda k: final_value[k])

        doc_ref = db.collection(u'userDetails').document('6aPCZWJhQGtrw33B3DUh')

        doc_ref.update({
            "attendance": [
                "Applied Physics - 34%", "Communication Skills - 64%", "Software Eng-2 - 23%", "Final Project 80%", "Internet Security 96%"
            ],
            "info": {
                "name": "Balakj Yosuf",
                "Father": "Yousuf",
                "dob": "12-12-1995",
                "contact": "043240434343",
                "email": "balaj@gmail.com"
            },
            "class": {
                "monday": [
                    {
                        "class": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "class": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "tuesday": [
                    {
                        "class": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "class": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "wednesday": [
                    {
                        "class": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "class": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "thursday": [
                    {
                        "class": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "class": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "friday": [
                    {
                        "class": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "class": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ]
            },
            "mid": {
                "monday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "tuesday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "wednesday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "thursday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "friday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ]
            },
            "final": {
                "monday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "tuesday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "wednesday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "thursday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "friday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ]
            },
            "transport": {
                "totalPaid": 450000,
                "remaining": 16000
            },
            "tuition": {
                "totalPaid": 45000,
                "remainging": 44000
            },
            "hostel": {
                "totalPaid": 75000,
                "remainging": 0
            },
            "max_gpa": 3.8,
            "min_gpa": 1.6,
            "gpa": 3.5,
            "credit_hours": {
                "required": 124,
                "passed": 100
            },
            "registered_courses": ["Applied Physics", "Communication Skills", "Software Eng-2", "Final Project", "Internet Security"],
            "final_admit_card": "https://www.hamdard.edu.pk/wp-content/uploads/2018/09/1.png",
            "mid_admit_card": "https://www.hamdard.edu.pk/wp-content/uploads/2018/09/1.png",
            "report": "https://www.hamdard.edu.pk/wp-content/uploads/2018/09/1.png"
        }
        )

        doc_ref = db.collection(u'userDetails').document('4lZ2opCNWKuZidJcWDPE')

        doc_ref.update({
            "attendance": [
                "Applied Physics - 34%", "Communication Skills - 64%", "Software Eng-2 - 23%", "Final Project 80%", "Internet Security 96%"
            ],
            "info": {
                "name": "Arman",
                "Father": "Saad Nasir",
                "dob": "12-12-1994",
                "contact": "03423421",
                "email": "saad@gmail.com"
            },
            "class": {
                "monday": [
                    {
                        "class": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "class": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "tuesday": [
                    {
                        "class": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "class": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "wednesday": [
                    {
                        "class": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "class": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "thursday": [
                    {
                        "class": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "class": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "friday": [
                    {
                        "class": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "class": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ]
            },
            "mid": {
                "monday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "tuesday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "wednesday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "thursday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "friday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ]
            },
            "final": {
                "monday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "tuesday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "wednesday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "thursday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ],
                "friday": [
                    {
                        "exam": "Algebra",
                        "time": "0900 - 0945"
                    },
                    {
                        "exam": "Communication Skills",
                        "time": "1000 - 1130"
                    }
                ]
            },
            "transport": {
                "totalPaid": 450000,
                "remaining": 16000
            },
            "tuition": {
                "totalPaid": 45000,
                "remainging": 44000
            },
            "hostel": {
                "totalPaid": 75000,
                "remainging": 0
            },
            "max_gpa": 3.8,
            "min_gpa": 1.6,
            "gpa": 1.8,
            "credit_hours": {
                "required": 124,
                "passed": 96
            },
            "registered_courses": ["Applied Physics", "Communication Skills", "Software Eng-2", "Final Project", "Internet Security"],
            "final_admit_card": "https://www.hamdard.edu.pk/wp-content/uploads/2018/09/1.png",
            "mid_admit_card": "https://www.hamdard.edu.pk/wp-content/uploads/2018/09/1.png",
            "report": "https://www.hamdard.edu.pk/wp-content/uploads/2018/09/1.png"
        }
        )

        doc_ref = db.collection(u'userDetails').document(
            data['username']).get()

        doc = doc_ref.to_dict()

        mapping = {
            "ATTENDANCE": "attendance",
            "CGPA": "gpa",
            "CLASS_TIMINGS": "class",
            "CREDIT_HOURS": "credit_hours",
            "FINAL_SCHEDULE": "final",
            "HOSTEL_FEE": "hostel",
            "INFO": "info",
            "MAX_CGPA": "max_gpa",
            "MID_SCHEDULE": "mid",
            "MIN_CGPA": "min_gpa",
            "PRINT_FINAL_ADMIT_CARD": "final_admit_card",
            "PRINT_MID_ADMIT_CARD": "mid_admit_card",
            "REGISTERED_COURSES": "registered_courses",
            "RESULT": "report",
            "TRANSPORT_FEE": "transport",
            "TUITION_FEE": "tuition"
        }
        print(highest)
        return jsonify(doc[mapping[highest]])

    except Exception as e:
        print(str(e))
        return Response("No Internet Connection or server down")


if __name__ == "__main__":
    app.run(debug=True)
