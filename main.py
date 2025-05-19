import cv2

# Replace with your actual RTSP URL
rtsp_url = "rtsp://admin:123456Ai@192.168.1.73:554/snl/live/1/1"  # This path may vary
# rtsp_url = "rtsp://192.168.144.25:8554/main.264"
# Open the stream
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Cannot open RTSP stream")
    exit()

max_width = 1280
max_height = 720

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

     # Get original dimensions
    h, w = frame.shape[:2]

    # Calculate scale to maintain aspect ratio
    scale = min(max_width / w, max_height / h)
    new_w, new_h = int(w * scale), int(h * scale)

    resized_frame = cv2.resize(frame, (new_w, new_h))

    cv2.imshow("IP Camera Stream", resized_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
