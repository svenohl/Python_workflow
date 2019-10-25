# To do:
# set all variables to NULL at new trial
# Make sure all variables are correctly filled
# customize to go through all files
# move them to correct file
#
# should we use lists, or dicts??


# Start with a message
print("Start parsing ...")

#show content in working directory

# open a file
f_tmp = open("rIM1ap02.msg",'r')

# open file for output
fout = open("output.txt",'w')

cnt = 0
for line in f_tmp:
    cnt = cnt + 1
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
            #trialdata = words[3:22]
            trialdata = '\t'.join(words[3:22])   
            outline   = [trialdata, EVENT_FixationDot,EVENT_MemoryOn,EVENT_MemoryOff,EVENT_GoSignal,EVENT_ProbeOn,EVENT_ClearScreen,TRIAL_ENDE]   
            outline   = map(str,outline)
            outline   = '\t'.join(outline)
            outline  += "\n"
            fout.write(outline)

# close files
f_tmp.close()
fout.close()