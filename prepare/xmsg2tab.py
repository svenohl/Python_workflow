# To do:
# open file with filenames
# while through filenames
# Start with a message
print("Start parsing ...")

# import
import os

# set path
path_wd = os.getcwd() #get working directory
path_parent = os.path.abspath('..')
path_msg = path_parent+"/msg/"
path_tab = path_parent+"/tab/"

# get filename
path_msg_files = os.listdir(path_msg)
for filename_in in path_msg_files:
    #filename_in  = "rIM1ap02.msg"
    filename_out = filename_in[0:8]
    filename_out +=  ".txt"
    filename_out = os.path.join(path_tab,filename_out)
    filename_in = os.path.join(path_msg,filename_in)

    # open a file
    f_tmp = open(filename_in,'r')

    # open file for output
    fout = open(filename_out,'w')

    # init variable
    newtrial = True

    for line in f_tmp:
        # if new trial then initialize all variables
        if newtrial == True:
            trial             = None
            EVENT_FixationDot = None
            EVENT_MemoryOn    = None
            EVENT_MemoryOff   = None
            EVENT_GoSignal    = None
            EVENT_ProbeOn     = None
            EVENT_ClearScreen = None
            TRIAL_ENDE        = None
            trialdata         = None
            newtrial          = False
        
        # split words in a line and parse information
        words = line.split()
        if len(words)>= 3:
            #print(words[2])
            if words[2] == "TRIALID":
                trial = words[3]
            elif words[2] == "EVENT_FixationDot":
                EVENT_FixationDot = words[1]
            elif words[2] == "EVENT_MemoryOn":
                EVENT_MemoryOn = words[1]
            elif words[2] == "EVENT_MemoryOff":
                EVENT_MemoryOff = words[1]
            elif words[2] == "EVENT_GoSignal":
                EVENT_GoSignal = words[1]
            elif words[2] == "EVENT_ProbeOn":
                EVENT_ProbeOn = words[1]  
            elif words[2] == "EVENT_ClearScreen":
                EVENT_ClearScreen = words[1]   
            elif words[2] == "TRIAL_ENDE":
                TRIAL_ENDE = words[1]               
            elif words[2] == "TrialData":
                trialdata = '\t'.join(words[3:22])   
                outline   = [trialdata, EVENT_FixationDot,EVENT_MemoryOn,
                         EVENT_MemoryOff,EVENT_GoSignal,EVENT_ProbeOn,
                         EVENT_ClearScreen,TRIAL_ENDE]   
                outline   = map(str,outline)
                outline   = '\t'.join(outline)
                outline  += "\n"
            
                # check if outline of a trial is complete and only then save
                if (bool(trial) == bool(EVENT_FixationDot) == bool(EVENT_MemoryOn)
                == bool(EVENT_MemoryOff) == bool(EVENT_GoSignal) 
                == bool(EVENT_ProbeOn)== bool(EVENT_ClearScreen) 
                == bool(TRIAL_ENDE)== bool(trialdata)==True):
                    fout.write(outline)
                    newtrial = True

# close files
f_tmp.close()
fout.close()