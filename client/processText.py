"""
    author : abhishek goswami
    abhishekg785@gmail.com

    processText.py : This module will take care of processing the text obtained
    from sources such as audio, app, web app etc and will take the desired actions
"""

import pkgutil      # for loading and unloading the packages, query modules in our case
from config import path

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

    module will consist of :

        a handler function to handle the required operation
        priority for deciding b/w modules
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
        self.queryModules = self.loadQueryModules()
        self.audio = audio

    @classmethod
    def loadQueryModules(cls):
        """
        Dynamically loads all the query modules in the query module folder
        and sorts them according to their priority orders. If no priority is
        defined for a given module, a priority 0 is defined
        """
        queryModulesPath = path.QUERY_MODULES_PATH
        print "loading modules from the path %s", queryModulesPath
        locations = [queryModulesPath]
        sortedQueryModules = []     # array containing the fetched query modules
        for finder, name, ispkg in pkgutil.walk_packages(locations):
            try:
                loader = finder.find_module(name)
                mod = loader.load_module(name)
                sortedQueryModules.append(mod)
            except:
                print 'Error in loading the module ' + name
        sortedQueryModules.sort(key = lambda mod: mod.PRIORITY if hasattr(mod, 'PRIORITY') else 0, reverse = True)
        return sortedQueryModules

    def parseText(self, text):
        """Parses the user input to the appropriate query module,
        testing it against the each module isValid function

        :param text: The user input
        :return:
        """
        textArr = text.split(' ')
        print textArr
        for module in self.queryModules:
            if module.isValid(text):
                print "the matching module found! ", module
                try:
                    module.handle(text, self.audio)
                except Exception as err:
                    print err
                    self.audio.speak('I am sorry! I could not take the actions, Try again after some time!')
                else:
                    print 'handling of the query by the module %s done !', module
                finally:
                    return
        print 'No module could take the action !'
        self.audio.speak('I am still a child! I have to learn a lot of things. The next time i will surely have an answer')


