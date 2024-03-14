#!/bin/sh

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
                # downloading and installing packages
                echo "Downloading and installing packages"
                source geminivenv/bin/activate
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