# Dota 2 Rune Reminder
## Scope

The purpose of this program is rather simple, given the addition of many different runes with patch 7.33, it might be helpful to have a reminder of the different spawning times.

## How it works

The program uses the GSI (game state integration) capabilities provided by Valve to parse the state of the game and obtaing the game clock. Given the events specified in the config file, it informs the users about the events that are about to happen.


## How to use it

### From source

If you want to build it from this repo:
1. Clone the repo
2. Install the dependencies running 

        pip install -r requirements.txt
3. Modify the config,toml that resides under the resource folder. Specifically, set:
   
        dota2path = "your\\installatiom\\path"
    
    it is important to keep the double quotes and to double the slashes. The path should point to the "dota" folder which usually if found under 
        
        "...\steamapps\common\dota 2 beta\game\dota" 

    This is needed as the program need to create a configuration file that is parsed by the game client in order to send the game information. 
4. You're set. You can run the program:
        
        main.py

### As exec

In this case you do not need a python installation in your pc as it is bundled in the .zip file you download from here.

1. Download the .zip file
2. Extract the content in a folder
3. Open the extract folder and modify the config.toml that resides under the resource folder. Specifically, set:
   
        dota2path = "your\\installatiom\\path"
    
    it is important to keep the double quotes and to double the slashes. The path should point to the "dota" folder which usually if found under 
        
        "...\steamapps\common\dota 2 beta\game\dota" 

    This is needed as the program need to create a configuration file that is parsed by the game client in order to send the game information. 
4. Execute the main.exe file. 

### How to start it

Once you performed the above steps you should see a dota icon in the system tray. 
Right clicking on it gives you 3 options:
1. Start. The program starts to listen for information coming from the game client.
2. Stop. Pause the execution, the program stops listening and the alerts do not work anymore. You can re-start listening clicking on the start option.
3. Exit. Completely close the application. You will need to restart program (from your IDE or main.exe) to use it again.

## Permissions
It is likely that windows will complain about the exe not being signed. If you do not trust the source code, you can read it yourself and then decide if you want to execute it or not.
The program also need network access in order to listen for the requests coming from the game client

## Problems? 
If you are using the .zip file (and therefore the main.exe file) and the program does not seem to start, you can do the following:
1. Open a powershell window.
2. Copy the address of the folder in which you extracted the zip file.
3. Paste the address in the powershell window as follows:

        cd "<your copied path>"
    and press enter

4. Type:

        .\main.exe
    and press enter.  
Now the error message should appear on the screen.
If you do not know how to solve it, feel free to contact me or open a problem here on GitHub.

If you are building from the source code, I am confident you know where to look for the error message :D