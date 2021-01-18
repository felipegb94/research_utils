#### Standard Library Imports
import os
import json

#### Library imports
from IPython.core import debugger
breakpoint = debugger.set_trace

#### Local imports


def load_json( json_filepath ):
	assert( os.path.exists( json_filepath )), "{} does not exist".format( json_filepath )
	with open( json_filepath, "r" ) as json_file: 
		return json.load( json_file )