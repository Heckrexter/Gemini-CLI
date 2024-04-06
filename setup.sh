#!/bin/sh

# creating final gemini file
echo "Creating final gemini file"
echo "#!/bin/sh\n\npath=$(pwd)\n$(cat geminiformat.sh)" > gemini.sh
chmod +x gemini.sh

# creating historydb file
echo "Creating historydb file"
echo "import sqlite3\n\npath=\"$(pwd)\"\n$(cat historydbformat.py)" > historydb.py


# check for python3
echo "Checking for python3"
which python3
if [ $? -eq 0 ] 
    then
        echo "Python3 found"
        # create virtual environment
        echo "Creating virtual environment"
        python3 -m venv "geminivenv"
        if [ $? -eq 0 ] 
            then
                echo "Virtual environment created"
                source geminivenv/bin/activate
                # downloading and installing packages
                echo "Downloading and installing packages"
                pip install -q -U google-generativeai
                if [ $? -eq 0 ] 
                    then
                        echo "Package installed"
                        echo "Installation successful"
                        exit 0
                    else 
                        echo "Package not installed due to error $?"
                    fi
            else 
                echo "Virtual environment not created due to error $?"
        fi
    else
        echo "Python3 is not installed, please install then return"
    fi