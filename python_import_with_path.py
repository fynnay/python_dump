# python relative import test

# Import the shotgun module from the pipeline folder
import imp
import sys
import inspect

# Add shotgun_api_dir to sys.path
shotgun_api_dir = "/Volumes/Verbinski/02_SCRIPTING/postyr/pipeline/active/10_OTHER/shotgun_api"
if shotgun_api_dir not in sys.path:
    sys.path.insert(0, shotgun_api_dir)
from shotgun import Shotgun
print Shotgun