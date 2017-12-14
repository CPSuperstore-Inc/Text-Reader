def __open_config():
    # open the config file object as a temporary variable
    temp = open('configurations/config.txt', 'r')

    # Save the contents of the file into an other variable
    open_file = temp.readlines()

    # Close the file
    temp.close()

    # Remove all of the EOL Characters
    for item in range(len(open_file)):
        # Check if a line contains "//"
        if '//' in open_file[item]:
            # if it does, clear it. it is a comment.
            open_file[item] = ""
        open_file[item] = open_file[item].rstrip('\n')

    # Convert this to a dictionary, and return it
    open_file = eval(''.join(open_file))
    return open_file


def __open_keys():
    # open the config file object as a temporary variable
    temp = open('configurations/key_bindings.txt', 'r')

    # Save the contents of the file into an other variable
    open_file = temp.readlines()

    # Close the file
    temp.close()

    # Remove all of the EOL Characters
    for item in range(len(open_file)):
        # Check if a line contains "//"
        if '//' in open_file[item]:
            # if it does, clear it. it is a comment.
            open_file[item] = ""
        open_file[item] = open_file[item].rstrip('\n')

    # Convert this to a dictionary, and return it
    open_file = eval(''.join(open_file))
    return open_file


def full_screen():
    # Return Full Screen Boolean
    return __open_config()['Full Screen']


def use_monitor():
    # Return Use Monitor Boolean
    return __open_config()['Use Monitor Size']


def screen_width():
    # Return Screen Width Integer
    return __open_config()['Screen Width']


def screen_height():
    # Return Screen Height Integer
    return __open_config()['Screen Height']


def file_order():
    # Return file order list
    return __open_config()['File Order']


def font_name():
    # Return font name
    return __open_config()['Font Name']


def font_size():
    # Return font size
    return __open_config()['Font Size']


def end_message():
    # Return message to display when everything is done
    return __open_config()['End Message']


def back_color():
    # Return background color
    return __open_config()['Background Color']


def front_color():
    # Return foreground color (text color)
    return __open_config()['Foreground Color']


def font_align():
    # Return text alignment (left, center, right)
    return __open_config()['Align Text'].lower()


def text_margin():
    # Return text margin
    return __open_config()['Margin']


def key_go():
    # Return the "GO" key ID
    return __open_keys()["Next"]


def key_close():
    # Return the "Quit" key ID
    return __open_keys()["Exit"]

