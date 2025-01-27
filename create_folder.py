import os

msg = []

def path_creation(subpath, project_name, release, radio_position, buyer):
    # SEARCHING RELEASE GROUP
    ap, cp, csc = release.split('_')
    group = csc[0:3]

    # TYPE A PICKED
    if radio_position == 1:
        for i in range(len(buyer)):
            path_type_A = r"{a}\{b}\{c}\{d}\Example\{e}\Example".format(a=subpath, b=project_name, c=group, d=release, e=buyer[i])
            creation_message(path_type_A)
        creation_message(path_type_A)  
    
    # TYPE B PICKED
    if radio_position == 2:
        for i in range(len(buyer)):
            path_type_A = r"{a}\{b}\{c}\{d}\Example\{e}\Example".format(a=subpath, b=project_name, c=group, d=release, e=buyer[i])
            creation_message(path_type_A)
        creation_message(path_type_A) 
        
    # TYPE C PICKED
    if radio_position == 3:
        for i in range(len(buyer)):
            path_type_A = r"{a}\{b}\{c}\{d}\Example\{e}\Example".format(a=subpath, b=project_name, c=group, d=release, e=buyer[i])
            creation_message(path_type_A)
        creation_message(path_type_A)

def creation_message(path):
    try:
        os.makedirs(path)
    except OSError:
        msg.append('Creation of the directory %s failed' % path)
    else:
        msg.append('Successfully created the directory %s ' % path)
