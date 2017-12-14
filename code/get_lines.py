def get_lines(file_name):
    # open the config file object as a temporary variable
    temp = open('files/{}'.format(file_name), 'r')

    # Save the contents of the file into an other variable
    open_file = temp.readlines()

    # Close the file
    temp.close()

    # Remove all of the EOL Characters
    for item in range(len(open_file)):
        open_file[item] = open_file[item].rstrip('\n')

    return open_file
