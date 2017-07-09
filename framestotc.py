def framesToTC(framecount,framerate):
    # Convert everything to float to get accurate decimals
    frms = float(framecount)
    fps  = float(framerate)
    cnt  = float(60)
    
    # Hours
    hours   = frms/(cnt*cnt*fps)
    remain  = hours-int(hours)
    
    # Minutes
    minutes = remain*cnt
    remain  = minutes-int(minutes)
    
    # Seconds
    seconds = remain*cnt
    remain  = seconds-int(seconds)
    
    # Frames
    frames  = float(round(remain*fps))
    # Round up to next second if framecount == fps
    if frames == fps:
        frames = float(0)
        seconds += float(1)

    # Pad zeroes
    hours   = str(int(hours)).zfill(2)
    minutes = str(int(minutes)).zfill(2)
    seconds = str(int(seconds)).zfill(2)
    frames  = str(int(frames)).zfill(2)

    # Create timecode format
    TC = "%s:%s:%s:%s"%(hours,minutes,seconds,frames)

    return TC

print framesToTC(257,30)