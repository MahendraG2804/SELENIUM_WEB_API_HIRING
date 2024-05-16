import pyautogui
import cv2
import numpy as np

def recording():
    
    # Specify resolution
    resolution =(1920, 1080)
    pass

    # Specify video codec
    codec = cv2.VideoWriter_fourcc(*"XVID")
    
    # Filename
    filename = "Recording.avi"
    
    # Specify Frames per second
    fps = 60.0
    
    # Create a VideoWritter object
    out = cv2.VideoWriter(filename, codec, fps, resolution)
    
    # Create a empty window
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL )
    
    # Resize the window
    cv2.resizeWindow("Live", 480, 270)
    
    while True:
        # Taking Screenshot using pyautogui
        img = pyautogui.screenshot()
        
        # Convert screenshot to a numpy array
        frame = np.array(img)
        
        # Convert from BGR Tto RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Write into output file
        out.write(frame)
        
        # Display recording screen
        cv2.imshow('Live', frame)
        
        # Stop recording when "q" is pressed
        if cv2.waitKey(1) == ord('q'):
            break
        
    # Release the vedio writer
    out.release()
    
    # Quit all windows
    cv2.destroyAllWindows()
    