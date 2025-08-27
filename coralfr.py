#!/usr/bin/env python3
# Compiler/Interperter for the .CORAL framework based on NEMOlang ment to upgrade NEMOlang and future .CORAL languages
# The .CORAL framework is not a seperate language on its own and is based on the stock NEMOlang/GNFR (Global Novaxis Framework and Runtime) and is made to replace the weaker and floppy established stock framework built from Novaxis (GNFR) that was improperly ported.
# The .CORAL framework improves documentation, format, modular-ability, abstract-ability and replacing an outdated interperter (GNFR) to a Serialized IR Compiler (SIC)
# .CORAL doesnt compile into a runnable bytecode. Instead it compiles into serialized intermediate repersentation (IR) expressed in JSON. This JSON or more properly named JsnButler is used by the runtime to carry
# Values, Program structure and such over to the main runtime/language (for interop communication) but execution is handled by this so called "interperter" itself, not the JSON. In other words,
# .CORAL uses compilation into a serialized IR plus interperted execution.
# This version/file of .CORAL is the public share template for the .CORAL language framework (edit this with the name of your language)
# If your creating a language with the framework, edit everything at your will and follow the rules of the GPL 3.0 License in the LICENSE file.
# .CORAL Version 0.0.1



import json # to compile down to
import sys # to grab flags and file to be compiled

x_tape = [0] * 100 # define xtape
y_tape =[0] * 100 #  define ytape (delete if your not making a 2d tape)
tape = [x_tape, y_tape] # define general tape (also delete if your not making a 2d tape)
xptr = 0 # define x pointer
yptr = 0 # define y pointer (delete this too if your not making a 2d tape)
comment_mode = False # for comments
try: # prevent IndexError / Troubleshoot if doesnt work :(
    filenamer = sys.argv[1]
except IndexError:
    raise FileNotFoundError(f"The passed file argument does not exist or was not put in as an argument.")
rcode = "" # code to be compiled/interperted, passed through by sys.argv[1]
legalfes = ["", ""] # define the legal file extensions to be used, if file used with incorrect extension it wont run and will raise a FileNotFoundError
cjson = { # define basic json output skeletion, used to interop between languages and for IR
    "program_name": f'{filenamer}', # Name of the file
    "legal_file_extensions": legalfes, # Legal file extensions defined up ^^
    "tape": {
        "x_tape": x_tape, # x tape (currently 0, gets updated at end)
        "y_tape": y_tape # y tape (also currently 0 and gets updated at end (remove if not making 2d tape))
    },
    "pointers": {
        "x_pointer": xptr, # x pointer (currently 0, gets updated at end)
        "y_pointer": yptr  # y pointer (currently 0, also gets updated at end (remove if not making 2d tape))
    },
    "outputs": [
            # any outputs will be put here

    ],
    "debug": { # Debug options, add more here if wanted
        "steps_executed": 0, # how much commands ran
    }
} 

if legalfes[0] in filenamer: # if .nec is in the filename remove .nec to make a plain filename (edit the legalfes tape to add your file extensions)
    filenamew = filenamer.replace(legalfes[0], '')
elif legalfes[1] in filenamer: # if .nemoc is in the filename remove .nemoc to make a plain filename (edit the legalfes tape to add your file extensions)
    filenamew = filenamer.replace(legalfes[1], '')
else:
    raise FileNotFoundError(f"file '{filenamer}' does not have a valid file extension") # Raise FileNotFoundError if filename does not have a proper filename

file1 = open(filenamer, "r")
rcode = file1.read().strip() # open file, read code and store it in rcode/runtime code


if rcode.startswith("") != True: # check if rcode has the SoF marker/initiliser I, otherwise raise RuntimeError (edit to fit your custom SoF or delete)
    raise RuntimeError("Code not properly initilized with 'I' at SoF.")
elif rcode.endswith("") != True: # check if rcode has the EoF marker/ender $, otherwise raise RuntimeError (edit to fit your custom EoF or delete)
    raise RuntimeError("Code not properly closed with '$' at EoF.")
# Check if code contains SoF and EoF markers


for cmd in rcode.strip(): # for every char in code stripped (meaning the code doesnt have newlines or whitespaces) (if your reading by line make rcode.strip() to rcode.strip().splitlines())
    if cmd == "": # SoF already has a function so means we can just skip it
        continue
    elif cmd == "": # EoF already has a function so means we can just skip it
        continue
    elif cmd == "": # delete current cell command
        if comment_mode:
             continue
        else:
            tape.remove(tape[tape.index(cmd)])
            xptr -= 1
    elif cmd == "": # user input command
        if comment_mode:
            continue
        else:
            tape[0][xptr] = int(input(">> "))
    elif cmd == "": # y tape user input command
        if comment_mode:
            continue
        else:
            tape[1][yptr] = int(input(">> "))
    elif cmd == "": # place next int as value in current cell command
        if comment_mode:
            continue
        else:
            u = int(rcode[rcode.index(cmd) + 1])
            tape[0][xptr] = u
    elif cmd == "" : # y tape place next int as value in current cell command
        if comment_mode:
            continue
        else:
            c = rcode[rcode.index(cmd) + 1]
            tape[1][yptr] = c
    elif cmd == "": # if command is "" move x pointer by one/ to the right
        if comment_mode:
            continue
        else:
            xptr += 1
    elif cmd == "": # if command is "" move y pointer minus one / to the left
        if comment_mode:
            continue
        else:
            xptr -= 1
    elif cmd == "": # if command is "" move y pointer up / plus one
        if comment_mode:
            continue
        else:
            yptr += 1
    elif cmd == "": # if command is """ move y_pointer down / minus one
        if comment_mode:
            continue
        else:
            yptr -= 1
    elif cmd == "": # if command is "" square current cell in x tape
        if comment_mode:
            continue
        else:
            tape[0][xptr] = tape[0][xptr] * tape[0][xptr]
    elif cmd == "": # if command is "" square current cell in y tape
        if comment_mode:
            continue
        else:
            tape[1][yptr] = tape[1][yptr] * tape[1][yptr]
    elif cmd == "": # if command is "" start comments
        if comment_mode:
            continue
        else:
            comment_mode == True
    elif cmd == "": # if command is "" add the int from before and int infront together
        if comment_mode:
            continue
        else:
            a = int(rcode[rcode.index(cmd) -1])
            b = int(rcode[rcode.index(cmd) +1])
            tape[0][xptr] = a + b
    elif cmd == "": # if command is "" subtract the int from before and the int infront together
        if comment_mode:
            continue
        else:
            a = int(rcode[rcode.index(cmd) -1])
            b = int(rcode[rcode.index(cmd) +1])
            tape[0][xptr] = a-b
    elif cmd == "": # if command is "" end comment
        comment_mode = False

    elif cmd == cmd.lower(): # check if the command is lower case (means it manipulates the y_tape) (delete if your not using case-sensitivity or a 2d tape)
        if cmd == "": # if command is lower "" add one to current cell in y_Tape and append one cell into the y_tape to prevent underflow
            if comment_mode: # this checks if comments are open, if yes dont run this, else run
                continue
            else:
                tape[1][yptr] += 1
                tape[1].append(0)
        elif cmd == "": # if command is lower "" subtract one from current cell in Y_tape 
            if comment_mode:
                continue
            else:
                tape[1][yptr] -= 1
        elif cmd == "": # if command is lower "" remove current cell from Y_tape and move pointer back one
            if comment_mode:
                continue
            else:
                tape[1].remove(tape[1][yptr])
                yptr -= 1
        elif cmd == "": # if command is lower "" save current cell value as ysave
            if comment_mode:
                continue
            else:
                ysave = tape[1][yptr]
        elif cmd == "": # if command is lower "" load ysave into current cell
            if comment_mode:
                continue
            else:
                tape[1][yptr] = ysave
        elif cmd == "": # if command is lower "" print ascii of current value in current cell and store output in cjson
            if comment_mode:
                continue
            else:
                print(chr(tape[1][yptr]), end='')
                cjson["outputs"] += f"{chr(tape[1][yptr])}"
        elif cmd == "": # if command is lower "" print raw cell value and store output in cjson
            if comment_mode:
                continue
            else:
                print(tape[1][yptr])
                cjson["outputs"] += {tape[1][yptr]}
        elif cmd == "": # if command is lower "" if current cell == 0 go to n cell
            if comment_mode:
                continue
            else:
                i = rcode[rcode.index(cmd) + 1]
                if tape[1][yptr] == 0:
                    if i.isdigit():
                        yptr = int(i)
                    else:
                        raise SyntaxError(f"cannot go to ycell {i} as it is not a valid inttype")
        elif cmd == "": # if command is lower "" in json log current cell val
            if comment_mode:
                continue
            else:
                cjson["outputs"] += {tape[1][yptr]}
    elif cmd == cmd.capitalize(): # check if the command is capital case (means it manipulates the x_tape (delete if not using 2d tape or not using case sensitivity))
        if cmd == "": # if command is capital "" add one to current cell in x_Tape and append one cell into the x_tape to prevent underflow
            if comment_mode:
                continue
            else:
                tape[0][xptr] += 1
                tape[0].append(0)
        elif cmd == "": # if command is capital "" subtract one from current cell in Y_tape 
            if comment_mode:
                continue
            else:
                tape[0][xptr] -= 1
        if cmd == "": # if command is capital "" remove current cell from X_tape and move pointer back one
            if comment_mode:
                continue
            else:
                tape[0].remove(tape[0][xptr])
                xptr -= 1
        elif cmd == "": # if command is capital "" save current cell value as xsave
            if comment_mode:
                continue
            else:
                xsave = tape[0][xptr]
        elif cmd == "": # if command is capital "" load xsave into current cell
            if comment_mode:
                continue
            else:
                tape[0][xptr] = xsave
        elif cmd == "": # if command is capital "" print ascii of current value in current cell and store output in cjson
            if comment_mode:
                continue
            else:
                print(chr(tape[0][xptr]), end='')
                cjson["outputs"] += f"{chr(tape[0][xptr])}"
        elif cmd == "": # if command is capital "" print raw cell value and store output in cjson
            if comment_mode:
                continue
            else:
                print(tape[0][xptr])
                cjson["outputs"] += {tape[0][xptr]}
        elif cmd == "": # if command is capital "" if current cell == 0 go to n cell
            if comment_mode:
                continue
            else:
                i = rcode[rcode.index(cmd) + 1]
                if tape[0][xptr] == 0:
                    if i.isdigit():
                        xptr = int(i)
                    else:
                        raise SyntaxError(f"cannot go to xcell {i} as it is not a valid inttype")
        elif cmd == "": # if command is capital "" in json log current cell val
            if comment_mode:
                continue
            else:
                cjson["outputs"] += tape[0][xptr]
        # Add whatever else you would like here following a similar structure

    cjson["debug"]["steps_executed"] += 1




        
            
with open(f"{filenamew}.json", "w") as f: # open json file if doesnt exist it will make a new one with the same filename as your main code
    cjson["tape"] = { # add updated tapes

    "x_tape": x_tape,
    "y_tape": y_tape # delete if your not using 2d tapes

},
    cjson["pointers"] = { # add updated pointers

        "x_pointer": xptr,
        "y_pointer": yptr # delete if your not using 2d tapes
},
    
    f.write(json.dumps(cjson)) # insert json values into json file
    file1.close() # properly close first file
    f.close() # properly close json filemoha@momo:~/Desktop/Coding/Nemo/.CORAL$ 
