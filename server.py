from flask import Flask, request, Response, send_file
# import jsonpickle
import numpy as np
import cv2
import numpy as np
from flask import jsonify
import argparse
import time
from flask_cors import CORS
import json
import imutils
from werkzeug.utils import secure_filename
import pickle
import os
import face_recognition
import os
import cv2
import pickle




# Returns (R, G, B) from name
def name_to_color(name):
    # Take 3 first letters, tolower()
    # lowercased character ord() value rage is 97 to 122, substract 97, multiply by 8
    color = [(ord(c.lower())-97)*8 for c in name[:3]]
    return color

def rec(tempjson):
    KNOWN_FACES_DIR = 'dataset'
    UNKNOWN_FACES_DIR = 'unknown_faces'
    TOLERANCE = 0.47
    FRAME_THICKNESS = 2
    FONT_THICKNESS = 2
    MODEL = 'hog'  # default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model



    embedding = pickle.loads(open("embeddings.pickel", "rb").read())



    print('Loading known faces...')
    known_faces = []
    known_names = []

    known_faces = embedding["embeddings"]
    known_names = embedding["names"]



    print('Processing unknown faces...')
    # Now let's loop over a folder of faces we want to label
    for filename in os.listdir(UNKNOWN_FACES_DIR):

        # Load image
        print(f'Filename {filename}', end='')
        image = face_recognition.load_image_file(f'{UNKNOWN_FACES_DIR}/{filename}')

        # This time we first grab face locations - we'll need them to draw boxes
        locations = face_recognition.face_locations(image, model=MODEL)

        # Now since we know loctions, we can pass them to face_encodings as second argument
        # Without that it will search for faces once again slowing down whole process
        encodings = face_recognition.face_encodings(image, locations)

        # We passed our image through face_locations and face_encodings, so we can modify it
        # First we need to convert it from RGB to BGR as we are going to work with cv2
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # But this time we assume that there might be more faces in an image - we can find faces of dirrerent people
        print(f', found {len(encodings)} face(s)')
        for face_encoding, face_location in zip(encodings, locations):

            # We use compare_faces (but might use face_distance as well)
            # Returns array of True/False values in order of passed known_faces
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)

            # Since order is being preserved, we check if any face was found then grab index
            # then label (name) of first matching known face withing a tolerance
            match = None
            if True in results:  # If at least one is true, get a name of first of found labels
                match = known_names[results.index(True)]
                print(f' - {match}')

                # Each location contains positions in order: top, right, bottom, left
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])

                # Get color by name using our fancy function
                color = name_to_color(match)

                # Paint frame
                cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                # Now we need smaller, filled grame below for a name
                # This time we use bottom in both corners - to start from bottom and move 50 pixels down
                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2] + 22)

                # Paint frame
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                y = {"name": str(f'{match}')}
                tempjson.append(y)

                # Wite a name
                cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)

        # Show image
        # cv2.imshow(filename, image)
        cv2.imwrite("0-processed.png", image)
        # cv2.waitKey(0)
        # cv2.destroyWindow(filename)


# Initialize the Flask application
app = Flask(__name__)
CORS(app=app)


# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    # cv2.imshow("Image", img)
    # cv2.waitKey(0)
    cv2.imwrite("unknown_faces/0.png", img)
    time.sleep(0.2)

    data = """{
    "classCode" : "IT201",
    "day" : "1" ,
    "week" : "1",
    "branch" : "IT",
    "students" :[

        
        ]
        }"""
    # build a response dict to send back to client

    j = json.loads(data)
    temp = j["students"]
    # res = recog("0.png", temp)
    res = rec(temp)
    # temp.append(res)
    # response = {res: 'image received'}
    print(json.dumps(j))
    # encode response using jsonpickle
    # response_pickled = jsonpickle.encode(response)

    return Response(response=json.dumps(j), status=200, mimetype="application/json",)


@app.route('/api/video', methods=['POST'])
def test2():
    if request.method == 'POST':
        # fname="ss"
        fname=request.headers['Name']
        # print(fname)
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file')
            return Response(response="no file")
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('no filename')
            return Response(response="no file")
        else:
            fname=request.headers['Name']
            filename = secure_filename(file.filename)
            # path = os.path.join(path, "/")
            file.save(fname+".mp4")
            print("saved file successfully")
            # consent = input("Do you want to train")
      #send file name as parameter to downlad
            
            os.system('python -u "e:\Github\opencv-face-recognition\opencv-face-recognition2\dlibb\captureface_video.py" -f '+fname)
            # consent = input("Do you want to train")
            # if(consent == "y"):
            #     os.system('python -u "e:\Github\opencv-face-recognition\opencv-face-recognition2\dlibb\extract_embeddings.py"')
            return Response(response="Success")

@app.route('/api/image.png', methods=['GET'])
def processedImage():
    path = "0-processed.png"
    return send_file(path, as_attachment=False)
# start flask app
app.run(port=5000,host="0.0.0.0")

