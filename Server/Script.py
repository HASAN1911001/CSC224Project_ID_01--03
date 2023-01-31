# import required modules
from glob import glob
from subprocess import call

source_path = '../Server/*'
intermediate_path = '../Intermediate/*'

source_object = glob(source_path)
intermediate_object = glob(intermediate_path)
intermediate_files = []

for i in range(len(intermediate_object)):
    object_path = source_object[i]
    object_name = object_path.split('\\')[-1].split('.')
    prefix = object_name[0]
    postfix2 = object_name[1]

    intermediate_files.append(prefix)


# Check if there any file other then Script file
if len(source_object) > 1:
    # For every file
    for i in range(1, len(source_object)):
        object_path = source_object[i]
        object_name = object_path.split('\\')[-1].split('.')
        prefix = object_name[0]
        postfix2 = object_name[1]
        
        path = '.'.join(object_name)
        # if the file is .py run it
        if postfix2 == 'py' and prefix != 'Script':
            print()
            print("==================================================")
            print(f"{path} is running from Script.py")
            print("Output:")
            call(["python", "{}".format('.'.join(object_name))])
            print("==================================================")
            print()
        
        
        if postfix2 == 'py' or postfix2 == 'c' or postfix2 == 'txt':

            # if the files are in the intermediate folder, check if any changes is made
            if prefix in intermediate_files:
                with open(path, 'r') as f:
                    file = f.readlines()
                
                with open(f"../Intermediate/{path}", 'r') as f:
                    iFile = f.readlines()

                # if changes are made, notify the user
                if file != iFile:
                    print()
                    print("===============================================")
                    print("There are some changes in the file {path}!")
                    print("Do yo want to keep the changed file?")
                    opinion = input("Y or N: ")
                    print("===============================================")
                    print()
                    
                    # if user wants to save the changes, save the file to intermediate folder
                    if opinion == 'Y':
                        with open(f"../Intermediate/{path}", 'w') as f:
                            for i in range(len(file)):
                                f.write(''.join(file[i]))

                    # if he does not want to change it, replace the file from the intermediate folder
                    elif opinion == 'N':
                        with open(path, 'w') as f:
                            for i in range(len(iFile)):
                                f.write(''.join(iFile[i]))

            # if the file is not in the intermideate folder, save it to the intermdeiate folder
            else:
                with open(path, 'r') as f:
                    file = f.readlines()

                with open(f"../Intermediate/{path}", 'w') as f:
                    for i in range(len(file)):
                        f.write(''.join(file[i]))



#Algorithm:

# Check if there any file other then Script file
# For every file
# if the file is .py run it
# if the files are in the intermediate folder, check if any changes is made
# if changes are made, notify the user
# if user wants to save the changes, save the file to intermediate folder
# if he does not want to change it, replace the file from the intermediate folder
# if the file is not in the intermideate folder, save it to the intermdeiate folder