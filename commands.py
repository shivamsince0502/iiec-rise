import os
while True:
    cmd = input("Give your command\n")
    if((("run" in cmd) or ("open" in cmd)or("looking" in cmd) or ("execute" in cmd) or("launch" in cmd) or ("start" in cmd)or
        ("enable" in cmd)or ("access" in cmd)or ("call" in cmd)) and(("chrome" in cmd) or ("google" in cmd) or ("use" in cmd))
            and (not(("don't" in cmd) or ("donot" in cmd)) or ("not" in cmd))):
        os.system("chrome")
    elif(cmd == "chrome"):
        os.system("chrome")
    elif((("run" in cmd) or ("open" in cmd) or ("execute" in cmd) or("launch" in cmd) or ("start" in cmd)or
        ("enable" in cmd)or ("access" in cmd)or ("call" in cmd) or ("use" in cmd) or
         or ("music" in cmd)  or ("video" in cmd)  ) and (("wmplayer" in cmd)
         or ("windows player" in cmd) or ("window player" in cmd) or ("default player" in cmd) or  ("video" in cmd))
         and (not(("don't" in cmd) or ("donot" in cmd) or ("not" in cmd) ))):
        os.system("wmplayer")
    elif(cmd == "wmplayer"):
        os.system("wmplayer")
    elif((("run" in cmd) or ("open" in cmd) or ("execute" in cmd) or("launch" in cmd) or ("start" in cmd)or ("use" in cmd) or
        ("enable" in cmd)or ("access" in cmd)or("looking for" in cmd) or ("call" in cmd)) and (("text" in cmd) or ("editor" in cmd) or ("notepad" in cmd)
        and (not(("don't" in cmd) or ("donot" in cmd) or ("not" in cmd) )))):
        os.system("notepad")
    elif(cmd == "notepad"):
        os.system("notepad")
    elif(("exit" in cmd) or ("quit" in cmd) or ("out of " in cmd) or ("close" in cmd)):
        break
    else:
        print("don't support\n")