import face_recognition
import os
import pickle
import cv2
import argparse
import imutils

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", type=str, required=True,
                help="Folder to save images")
args = vars(ap.parse_args())

folder = args["folder"]


path = os.getcwd()
path = os.path.join(path, "dataset")
os.chdir(path)
print(os.listdir())

print(path)
if folder not in os.listdir():
    os.mkdir(folder)

os.chdir(folder)

print(os.getcwd())
# load our serialized face embedding model from disk
# print("[INFO] loading face recognizer...")
# embedder = cv2.dnn.readNetFromTorch(args["embedding_model"])

# load the actual face recognition model along with the label encoder
# recognizer = pickle.loads(open(args["recognizer"], "rb").read())
# le = pickle.loads(open(args["le"], "rb").read())

# initialize the video stream, then allow the camera sensor to warm up
print("[INFO] Reading Video...")
cap = cv2.VideoCapture("../../"+folder+".mp4")

k = 0
# loop over frames from the video file stream
while True:
    # grab the frame from the threaded video stream
    # frame = vs.read()
    ret, frame = cap.read()
    frame = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
    frame = imutils.resize(frame, width=400)
    frame2 = frame


    if k % 5 == 0:
        cv2.imwrite("0000"+str(k)+".png", frame2)
    k += 1

                # cv2.putText(frame, text, (startX, y),
                # 	cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

        # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
    if k >= 251:
        break
            
    if key == ord("q"):
        break


# do a bit of cleanup
cv2.destroyAllWindows()
# vs.stop()
cap.release()
