try:
    # import the opencv library
    import cv2
    import mediapipe
    import traceback
    import math
    import time
    import pysinewave as ps
    
        #DEFINING VARIABLES
    
    #Initializing SineWave for Audio
    sto=ps.SineWave()
    
    #Setting up the Video Frames Variable
    vid = cv2.VideoCapture(0)
    fw=vid.get(cv2.CAP_PROP_FRAME_WIDTH)   #Later Used to mark points on frames
    fh=vid.get(cv2.CAP_PROP_FRAME_HEIGHT)   #Later Used to mark points on frames
    #Initializing Other Required Variable
    octave=math.pow(2,(3-1)-3)
    f=0
    pfreq=-1 #To check if same Audio is not already playing (Avoids overlapping)
    
        #DEFINING FUNCTIONS
    
    #To Play a Particular Note/Frequency
    def Play_Note(sto,freq,vol):
    
        print(pfreq,freq) #prints current and previous frequency(for debug purpose)
         
        if not freq==pfreq: #if current note/frequency is different
            ps.SineWave.stop(sto)
            ps.SineWave.set_frequency(sto,freq)
            ps.SineWave.set_volume(sto,vol)
            sto.play()
            # print("Hi") #For Debug Pupose
        return freq    
        
    #To Set the Octave of Notes like Sa of Middle or Higher Octave
    # (Not in Proper Use Right now but fuction is working)
    def Play_Note_Octave(st,f,vol,mul):
        return Play_Note(st,f*mul,vol)
    
    #Draws the Points on input coordinates    
    def draw(frame,i):
        if i is not None:
            
            #mediapipe normalize each point, so we need to convert it to pixel coordinate
            # so as to draw circle on the frame
            
            c=mediapipe.solutions.drawing_utils._normalized_to_pixel_coordinates(i.x,i.y,fw,fh)
            if c is not None:
                frame=cv2.circle(frame,(c[0],c[1]),5,(255,255,255),-5)
                cv2.putText(frame,str(c),(c[0]+10,c[1]+10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
        return frame,c
    
# define a video capture object

    with mediapipe.solutions.hands.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.8, max_num_hands=2) as hands:
            while vid.isOpened():
                
                # t=time.time()
                # t_current=t
                if(f==0):
                    while 1:
                        ret, frame = vid.read()
                        
                        # print(ret)
                        
                        
                        if ret == False:
                            continue
                        f=1
                        # t_current=time.time()
                        frame=cv2.flip(frame,1)
                        frame=cv2.resize(frame,(1080,720))
                        cv2.putText(frame,"WELCOME TO MUSICMENT",(300,360),cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0, 255), 5)
                        cv2.putText(frame,"Press 'Enter' To Continue",(370,390),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 2)
                        cv2.putText(frame,"INSTRUCTIONS",(450,500),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
                        cv2.putText(frame,"First, Show the Hand, you wanna use for Octaves ",(200,540),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
                        cv2.putText(frame,"Then, Show the Hand, you wanna use for Notes ",(220,570),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
                        cv2.putText(frame,"(NOTE: if You are using one hand, then, it will be used for Notes only)",(150,610),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)
                        # cv2.putText(frame,"First Show the Hand, you wanna use for Octaves Hand",(350,480),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
                        cv2.putText(frame,"Press q/Q To Exit",(10,50),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,0, 0), 2)
                        cv2.imshow('Musicment-Musical Instrument', frame)
                        cv2.resizeWindow('Musicment-Musical Instrument', 1080,720)
                        key1=cv2.waitKey(1)
                        if key1 & 0xFF == 13:
                            break
                        elif key1 & 0xFF== ord('q') or key1 & 0xFF==ord('Q'):
                            exit(0)
                        # time.sleep(1)
                        
                # time.sleep(1)        
                        
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
           
                ret, frame = vid.read()
                if ret == False:
                    continue
                key=cv2.waitKey(1)
                if (key & 0xFF == ord('Q') or key & 0xFF == ord('q') ) :
                    break 
                
                frame = cv2.flip(frame, 1)
                results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                if results.multi_hand_landmarks != None:
                    # print('Handedness:', results.multi_handedness)
                    thumb=results.multi_hand_landmarks[0].landmark[mediapipe.solutions.hands.HandLandmark.THUMB_TIP]
                    index = results.multi_hand_landmarks[0].landmark[mediapipe.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
                    middle = results.multi_hand_landmarks[0].landmark[mediapipe.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]
                    ring= results.multi_hand_landmarks[0].landmark[mediapipe.solutions.hands.HandLandmark.RING_FINGER_TIP]
                    little=results.multi_hand_landmarks[0].landmark[mediapipe.solutions.hands.HandLandmark.PINKY_TIP]
                    wri=results.multi_hand_landmarks[0].landmark[mediapipe.solutions.hands.HandLandmark.WRIST]
                
                    a=[thumb ,index,middle,ring,little]
                    x0=0
                    y0=0
                
                # Calculating the centroid of 6 points finger's tips and wrist point

                    for i in a:
                        x0+=i.x
                        y0+=i.y
                    x0+=wri.x
                    y0+=wri.y
                    c=(x0/6,y0/6)
                    centroid = mediapipe.solutions.drawing_utils._normalized_to_pixel_coordinates(c[0],c[1],fw,fh)
                    if centroid is not None:
                        frame=cv2.circle(frame, centroid, 5, (0, 0, 255), -1)
                        cv2.putText(frame,str(centroid),(centroid[0]+10,centroid[1]+10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                    wri = mediapipe.solutions.drawing_utils._normalized_to_pixel_coordinates(wri.x,wri.y,fw,fh)
                    if wri is not None and centroid is not None and all(a):
                        frame=cv2.circle(frame, wri, 5, (0, 255, 255), -1)
                        cv2.putText(frame,str(wri),(wri[0]+10,wri[1]+10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                        cv2.putText(frame,"Notes",(wri[0],wri[1]+50),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 255), 2)
                        
                    
                    if all(a) and centroid is not None and wri is not None:
                        
                        #draws points on each of 5 points in a
                        k=0
                        for i in a:
                            frame,a[k]=draw(frame,i)
                            k=k+1
                        #calculates the ratios required by using distances between points
                        ai=0
                        if all(a):
                            for ij in a:
                                ai+=(math.dist(centroid,ij))
                            # print(ai/5)
                            sat=[]
                            ai=[]
                            # print(len(ai))
                            ref=math.dist(centroid,wri)
                            for  j in range(5):
                                ai.append(math.dist(centroid,a[j]))
                            if ai is not None:
                                for  j in range(5):     
                                    sat.append(ai[j]/(ref+ai[j]))
                            
                            #prints distance ratio for finger tips(for debug purpose)
                            print("Notes"+str(sat)) 
                            
                        # hand 2 
                        # (Same Logic as hand 1,but other functionality)
                        # (octaves based on second hand)
                        if len(results.multi_hand_landmarks)==2:
                            thumb1=results.multi_hand_landmarks[1].landmark[mediapipe.solutions.hands.HandLandmark.THUMB_TIP]
                            index1 = results.multi_hand_landmarks[1].landmark[mediapipe.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
                            middle1 = results.multi_hand_landmarks[1].landmark[mediapipe.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]
                            ring1= results.multi_hand_landmarks[1].landmark[mediapipe.solutions.hands.HandLandmark.RING_FINGER_TIP]
                            little1=results.multi_hand_landmarks[1].landmark[mediapipe.solutions.hands.HandLandmark.PINKY_TIP]
                            wri1=results.multi_hand_landmarks[1].landmark[mediapipe.solutions.hands.HandLandmark.WRIST]
                
                            a1=[thumb1 ,index1,middle1,ring1,little1]
                            x01=0
                            y01=0
                
                        # Calculating the centroid of 5 finger's tips
                            for i in a1:
                                x01+=i.x
                                y01+=i.y
                            x01+=wri1.x
                            y01+=wri1.y
                            c1=(x01/6,y01/6)
                            centroid1 = mediapipe.solutions.drawing_utils._normalized_to_pixel_coordinates(c1[0],c1[1],fw,fh)
                            if centroid1 is not None:
                                frame=cv2.circle(frame, centroid1, 5, (0, 0, 255), -1)
                                cv2.putText(frame,str(centroid1),(centroid1[0]+10,centroid1[1]+10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                            wri1 = mediapipe.solutions.drawing_utils._normalized_to_pixel_coordinates(wri1.x,wri1.y,fw,fh)
                            if wri1 is not None and centroid1 is not None and all(a1):
                                frame=cv2.circle(frame, wri1, 5, (0, 255, 255), -1)
                                cv2.putText(frame,str(wri1),(wri1[0]+10,wri1[1]+10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                                cv2.putText(frame,"Octave",(wri1[0],wri1[1]+50),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 255), 2)
                        
                    
                            if all(a1) is not None and centroid1 is not None and wri1 is not None:
                                k=0
                                for i in a1:
                                    frame,a1[k]=draw(frame,i)
                                    k=k+1
                                ai1=0
                                if all(a1):
                                    for ij in a1:
                                        ai1+=(math.dist(centroid1,ij))
                                # print(ai/5)
                                sat1=[]
                                ai1=[]
                                # print(len(ai))
                                ref1=math.dist(centroid1,wri1)
                                for  j in range(5):
                                    ai1.append(math.dist(centroid1,a1[j]))
                                if ai1 is not None:
                                    for  j in range(5):     
                                        sat1.append(ai1[j]/(ref1+ai1[j]))

                                #prints distance ratio for finger tips(for debug purpose)
                                print("Octaves"+str(sat1))
                                if not(sat[1]<0.4 and sat[2]<0.4 and sat[0]<0.4 and sat[4]>0.45):
                                    if (sat1[0]>0.5 and not sat1[1]>0.45 and not sat1[2]>0.45):
                                        cv2.putText(frame,"Octave: 4",(40,170),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                                        octave=math.pow(2,(4-1)-3)
                                    elif(sat1[0]>0.4 and sat1[1]>0.45 and not sat1[2]>0.45):
                                        cv2.putText(frame,"Octave: 5",(40,170),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255, 0), 2)
                                        octave=math.pow(2,(5-1)-3)
                                    elif(sat1[1]>0.4 and sat1[2]>0.4 and sat1[0]>0.4):
                                        cv2.putText(frame,"Octave: 6",(40,170),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 255), 2)
                                        octave=math.pow(2,(6-1)-3)
                                    else:
                                        cv2.putText(frame,"Octave: 3",(40,170),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255, 255), 2)
                                        octave=math.pow(2,(3-1)-3)
                                else:
                                    if (sat1[0]>0.5 and not sat1[1]>0.45 and not sat1[2]>0.45):
                                        cv2.putText(frame,"Octave: 5",(40,170),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                                        octave=math.pow(2,(4)-3)
                                    elif(sat1[0]>0.4 and sat1[1]>0.45 and not sat1[2]>0.45):
                                        cv2.putText(frame,"Octave: 6",(40,170),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255, 0), 2)
                                        octave=math.pow(2,(5)-3)
                                    elif(sat1[1]>0.4 and sat1[2]>0.4 and sat1[0]>0.4):
                                        cv2.putText(frame,"Octave: 7",(40,170),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 255), 2)
                                        octave=math.pow(2,(6)-3)
                                    else:
                                        cv2.putText(frame,"Octave: 4",(40,170),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255, 255), 2)
                                        octave=math.pow(2,(3)-3)    
                
                    # hand 2 ----end
                    
                        #freq of notes 
                        sa=[261.63,293.66,329.63,369.99,392.00,440.00,493.88]
                        #based on pitch values(not in use)
                        pitch=[0,2,4,6,7,9,11,12]
                        
                        #if one hand detected then only plays
                        if len(results.multi_hand_landmarks)==1 or len(results.multi_hand_landmarks)==2:
                            if octave==1/2 :
                                if not(sat[1]<0.4 and sat[2]<0.4 and sat[0]<0.4 and sat[4]>0.45):
                                    cv2.putText(frame,"Octave: 3",(40,170),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255, 255), 2)
                            if (sat[0]>0.5 and not sat[1]>0.5 and not sat[2]>0.5):
                                cv2.putText(frame,"Note: Re/D",(40,130),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                                cv2.putText(frame,"Frequency: "+str(sa[1]*octave),(40,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0),2)
                                pfreq=Play_Note_Octave(sto,sa[1],1,octave)
                            elif(sat[1]>0.5 and not sat[0]>0.45 and not sat[2]>0.5):
                                cv2.putText(frame,"Note: Ga/E",(40,130),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                                cv2.putText(frame,"Frequency: "+str(sa[2]*octave),(40,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0),2)
                                pfreq=Play_Note_Octave(sto,sa[2],1,octave)
                            elif(sat[2]>0.45 and not sat[1]>0.45 and not sat[0]>0.4):
                                cv2.putText(frame,"Note: Ma'/F#",(40,130),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                                cv2.putText(frame,"Frequency: "+str(sa[3]*octave),(40,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0),2)
                                pfreq=Play_Note_Octave(sto,sa[3],1,octave)
                            elif(sat[0]>0.45 and sat[1]>0.5 and not sat[2]>0.5):
                                cv2.putText(frame,"Note: Pa/G",(40,130),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                                cv2.putText(frame,"Frequency: "+str(sa[4]*octave),(40,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0),2)
                                pfreq=Play_Note_Octave(sto,sa[4],1,octave)
                            elif(sat[1]>0.3 and sat[2]>0.4 and not sat[0]>0.4):
                                cv2.putText(frame,"Note: Dha/A",(40,130),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                                cv2.putText(frame,"Frequency: "+str(sa[5]*octave),(40,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0),2)
                                pfreq=Play_Note_Octave(sto,sa[5],1,octave)
                            elif(sat[1]>0.4 and sat[2]>0.4 and sat[0]>0.385):
                                cv2.putText(frame,"Note: Ni/B",(40,130),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                                cv2.putText(frame,"Frequency: "+str(sa[6]*octave),(40,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0),2)
                                pfreq=Play_Note_Octave(sto,sa[6],1,octave)
                            elif(sat[1]<0.4 and sat[2]<0.4 and sat[0]<0.4 and sat[4]>0.45):
                                if octave==1/2 :
                                    cv2.putText(frame,"Note: Sa'/C",(40,130),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                                    cv2.putText(frame,"Frequency: "+str(sa[0]*(octave*2)),(40,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0),2)
                                    cv2.putText(frame,"Octave: 4",(40,170),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
                                    pfreq=Play_Note_Octave(sto,sa[0],1,(octave*2))
                                else:
                                    cv2.putText(frame,"Note: Sa'/C",(40,130),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                                    cv2.putText(frame,"Frequency: "+str(sa[0]*(octave)),(40,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0),2)
                                    pfreq=Play_Note_Octave(sto,sa[0],1,octave)
                            elif(sat[1]<0.35 and sat[2]<0.2 and sat[0]<0.5 and sat[3]<0.25 and sat[4]<0.4):
                                cv2.putText(frame,"Note: Sa/C",(40,130),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
                                cv2.putText(frame,"Frequency: "+str(sa[0]*octave),(40,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0),2)
                                pfreq=Play_Note_Octave(sto,sa[0],1,octave)
                            else:
                                ps.SineWave.stop(sto) 
                                pfreq=-1
                        
                        #else if more than 2 then it will play breaked Notes
                        else:
                            
                            ps.SineWave.stop(sto)
                            time.sleep(0.3)
                            sto.play()
                            time.sleep(0.5)
                            # pfreq=-1
                            
                #if none hand is found then stops playing
                else:
                    ps.SineWave.stop(sto) 
                    pfreq=-1   
                    
                #frame resizing and naming and displaying               
                frame=cv2.resize(frame,(1080,720))
                cv2.putText(frame,"Press q/Q To Exit",(10,50),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,0, 0), 2)
                cv2.imshow('Musicment-Musical Instrument', frame)
                cv2.resizeWindow('Musicment-Musical Instrument', 1080,720)
                
# After the loop release the cap object
    vid.release()
# Destroy all the windows
    cv2.destroyAllWindows()

except:
    pass
    traceback.print_exc()