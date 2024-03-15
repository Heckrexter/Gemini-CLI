# Gemini-CLI
This application serves to allow the user to access Google's [Gemini AI Chatbot](gemini.google.com) from the Mac's Commandline. It is made with Google's [Gemini API](https://ai.google.dev/docs/gemini_api_overview)

## Requirements:-
- Python 3.9+
- Pip

## Program Setup:-
1. Download the repository

2. Access into the repository from the terminal with the cd command
    ```shell
    cd path/to/gemini-api-repo
    ```

3. Execute the setup.sh file with the sh command to setup the project and install dependencies and wait for it to finish execution.
    ```shell
    sh setup.sh
    ```

4. To make the gemini command to trigger the CLI app add an alias to to .zshrc or .bash_profile depending on which shell you use. You can do with using nano or textedit.
    ```
    alias gemini='path/to/gemini.sh'
    ```

5. Obtain the Gemini API key [here](https://makersuite.google.com/app/apikey)

6. Create a file called key.py and paste the following line of code in it and replace the placeholder text with the Gemini API code.
    ```
    GOOGLE_API_KEY = "PlaceAPIKeyHere"
    ```

7. Once all the above steps have been completed run the Gemini-CLI program with the following command
    ```shell
    gemini
    ```