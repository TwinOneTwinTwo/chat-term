# chatgpt-term
python script to run gpt inside bash/zsh terminal

#README -- To run this python program you need to have the following modules installed either by pipx or your linux package manager:
 1.  Python 3.6 or higher
 2.  openai    #a python library for interfacing with the OpenAI API
 3.  pyfzf     #a python library for fuzzy searching
 4.  rich      #a python library for rich text and beautiful formatting
 5.  pyperclip #a python library for copy and pasting to clipboard
 6.  dotenv    #a python library for loading environment variables from .env file
 7.  sys       #a python library for system-specific parameters and functions
 8.  os        #a python library for interacting with the operating system
 9.  threading #a python library for threading
 10. time      #a python library for time


You must have an OpenAI account for this program, and be sure that your OpenAIkey is export inside your .bashrc/.zshrc (or in your environment so that any shell you want could read it)

Then it's as easy as ```python chatgpt-term.py``` or rename it to "chatgpt" and place it inside your .local/bin folder, which should be in your $PATH -- if not ```export PATH=$PATH:/path/to/new/directory``` to add any directory ( in this case ~/.local/bin)

