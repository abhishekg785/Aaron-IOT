"""
    author : abhishek goswami
    abhishekg785@gmail.com

    processText.py : This module will take care of processing the text obtained
    from sources such as audio, app, web app etc and will take the desired actions
"""

"""
    We will be having modules for out queries eg :  whether module, greeting module, etc.
    steps to process the text :
        - get the text obtained from the source
        - find the suitable module for the text
        - validate the text for that module
        - and finally handle the operation for that module

    steps for modules:
        - Dynamically load all the modules and set them according to the priorities
        - Search the query against the list of the fetched modules
"""


class ProcessText:

    def __init__(self, audio):
        """
        Initializes a new ProcessText object , which check the user input against
        the list of the query modules.
        Note : The order of the query modules matters as the module which occurs on
        the top will be executed on validation.
        :param audio: audio module used to handle user input as well as output
        """
        pass
