from .use_everywhere import *

UE_VERSION = "4.9"

NODE_CLASS_MAPPINGS = { 
    "Seed Everywhere": SeedEverywhere,
    "Anything Everywhere": AnythingEverywhere,
    "Anything Everywhere3": AnythingEverywhereTriplet,
    "Anything Everywhere?": AnythingSomewhere,
    "Prompts Everywhere": AnythingEverywherePrompts,
    "Simple String": SimpleString,
    "Combo to String": ComboToString,
    "String to Combo": StringToCombo,
}

# temporary code to remove old javascript installs
import os, shutil
import folder_paths
module_js_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "js")
application_root_directory = os.path.dirname(folder_paths.__file__)
old_code_location = os.path.join(application_root_directory, "web", "extensions", "use_everywhere")
if os.path.exists(old_code_location):
    shutil.rmtree(old_code_location)

old_code_location = os.path.join(application_root_directory, "web", "extensions", "cg-nodes", "use_everywhere.js")
if os.path.exists(old_code_location):
    os.remove(old_code_location)
# end of temporary code

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "WEB_DIRECTORY"]