# import required modules
from glob import glob
import shutil

# check whether or not there are any file of required types
source_path = '../Server/*'
intermediate_path = '../Intermediate'

source_object = glob(source_path)

if len(source_object) > 1:
    for i in range(1, len(source_object)):
        object_path = source_object[i]
        object_name = object_path.split('\\')[-1].split('.')
        prefix = object_name[0]
        postfix2 = object_name[1]


    # if the files are not in the intermideate folder, save them to the intermdeiate folder
    # if the file is .py run it

    # if the files are in the intermediate folder, check if any changes is made

        # if no changes are made, ignor

        # if changes are made, notify the user

            # if user wants to save the changes, save the file to intermediate folder

            # if he does not want to change it, replace the file from the intermediate folder

