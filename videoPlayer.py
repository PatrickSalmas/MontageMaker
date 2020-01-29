import cv2

video = cv2.VideoCapture("montageShotty1.4_Test.mp4")

while True:
    ret, frame = video.read()
    if not ret: break
    #print video.get(1)

    cv2.imshow('frame',frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
