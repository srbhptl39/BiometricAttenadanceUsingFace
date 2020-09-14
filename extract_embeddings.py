import face_recognition
import os
import pickle
import cv2


KNOWN_FACES_DIR = 'dataset'
UNKNOWN_FACES_DIR = 'unknown_faces'
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
# default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model
MODEL = 'hog'


# Returns (R, G, B) from name
def name_to_color(name):
    # Take 3 first letters, tolower()
    # lowercased character ord() value rage is 97 to 122, substract 97, multiply by 8
    color = [(ord(c.lower())-97)*8 for c in name[:3]]
    return color


# embedding = pickle.loads(open("embeddings.pickel", "rb").read())
print('Loading known faces...')
known_faces = []
known_names = []
# known_faces = embedding["embeddings"]
# known_names = embedding["names"]

fol = 0
# We oranize known faces as subfolders of KNOWN_FACES_DIR
# Each subfolder's name becomes our label (name)
for name in os.listdir(KNOWN_FACES_DIR):
    countt = 0
    print("fol - "+ str(fol))
    fol+=1

    # Next we load every file of faces of known person
    for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
        

        # Load an image
        try:
            image = face_recognition.load_image_file(
                f'{KNOWN_FACES_DIR}/{name}/{filename}')
            print(str(f'{KNOWN_FACES_DIR}/{name}/{filename}'))
        except:
            print("")
            continue

        # Get 128-dimension face encoding
        # Always returns a list of found faces, for this purpose we take first face only (assuming one face per image as you can't be twice on one image)

        try:

            encoding = face_recognition.face_encodings(image)
            # encoding = encoding[0]
            print(str(len(encoding)))
            num = len(encoding)
            
            for i in range(num):
                known_faces.append(encoding[i])
                known_names.append(name)
                
                # print(encoding)
            print(" "+str(countt))

            # Append encodings and name
            # known_faces.append(encoding)
            # known_names.append(name)
        except:
            print("Failed")

        countt += 1
        if countt>21:
            break

        # Append encodings and name
        # known_faces.append(encoding)
        # known_names.append(name)


data = {"embeddings": known_faces, "names": known_names}

f = open("embeddings.pickel", "wb")
f.write(pickle.dumps(data))
f.close()
