import pygame
from pygame.locals import *

import globalVariable
import config_reader
import get_lines
import text_format

pygame.init()


def run():

    # Set GlobalVariable Screen properties
    if config_reader.use_monitor() is True:
        info_object = pygame.display.Info()
        globalVariable.screen_w = info_object.current_w
        globalVariable.screen_h = info_object.current_h
    else:
        globalVariable.screen_w = config_reader.screen_width()
        globalVariable.screen_h = config_reader.screen_height()

    if config_reader.full_screen() is True:
        # If the mode is full screen, set the mode to pygame object FULLSCREEN
        globalVariable.screen_mode = FULLSCREEN
    else:
        # If the mode is not full screen, set the mode to pygame object 0 (windowed)
        globalVariable.screen_mode = 0

    # Set the list of files to use into global variable
    globalVariable.file_list = config_reader.file_order()

    # Generate the screen, and set it to a GlobalVariable value
    globalVariable.screen = pygame.display.set_mode((globalVariable.screen_w, globalVariable.screen_h),
                                                    globalVariable.screen_mode, 32)

    # Set the screen's caption to globalVaraible.NAME
    pygame.display.set_caption(globalVariable.NAME)

    # Get first file in memory
    data_set = generate_file()
    globalVariable.file_index = 0

    # Generate the font from settings
    main_font = pygame.font.SysFont(config_reader.font_name(), config_reader.font_size())

    # Get the first line, and set as text
    try:
        main_text = text_format.wrapline(data_set[globalVariable.file_index], main_font, globalVariable.screen_w)
    except IndexError:
        main_text = text_format.wrapline(config_reader.end_message(), main_font, globalVariable.screen_w)

    # get the alignment setting of the text
    align = config_reader.font_align()
    margin = config_reader.text_margin()

    # The main loop of the game!
    while True:
        for event in pygame.event.get():

            # Quit Event
            if event.type == QUIT:
                quit()

            if event.type == KEYDOWN:
                # If the 'quit' key is pressed(Default - 27 [Escape])
                if event.key == config_reader.key_close():
                    # Quit the program
                    quit()

                # If the 'go' key is pressed (Default - 32 [Space])
                if event.key == config_reader.key_go():
                    try:
                        globalVariable.file_index += 1
                        # Attempt to set the text to the next line
                        text = data_set[globalVariable.file_index]
                        # Increment the index for the next line

                    except IndexError:
                        # On failure due to running out of file
                        # Grab the next file into memory
                        data_set = generate_file()
                        if data_set is False:
                            # If this returns false, the show has ended
                            # The "End Show" message is shown
                            text = config_reader.end_message()
                        else:
                            # Set the index back to 0
                            globalVariable.file_index = 0
                            # Get the first item (index 0)
                            text = data_set[globalVariable.file_index]
                            # Increment the file index
                            # globalVariable.file_index += 1

                    except TypeError:
                        # If an unexpected data type is returned (A not list)...
                        text = ""
                        # Set text to nothing (to get rid of a PyCharm PEP Error)
                        if type(data_set) is bool:
                            # If the data set returns as a boolean (AKA False, from generate_file() function)
                            # Terminate the program
                            quit()

                    # Get the next line, and set as text
                    # This function returns the text all word wrapped, and pretty and stuff
                    main_text = text_format.wrapline(text, main_font, globalVariable.screen_w - 2 * margin)

        # Fill in the screen as the color in the config file
        globalVariable.screen.fill(config_reader.back_color())

        # Set the draw text y_position to 60
        y_pos = margin

        # For each word wrapped line in the file,
        for item in main_text:
            # Create a font object of the line with the color in the config file
            msg = main_font.render(item, 1, config_reader.front_color())
            # Draw the new text at appropriate spto based on alignment

            if align == 'right':
                # If right aligned, calculate right alignment position
                x_pos = globalVariable.screen_w - margin - msg.get_size()[0]
            elif align == 'center':
                # If center aligned, calculate center alignment position
                x_pos = (globalVariable.screen_w / 2) - (msg.get_size()[0] / 2)
            else:
                # If it is not either, assume left, and place at margin
                x_pos = margin

            globalVariable.screen.blit(msg, (x_pos, y_pos))
            # add the y-value by the text size just drawn
            y_pos += msg.get_size()[1]

        # Update the screen
        pygame.display.update()


def generate_file():
    try:
        # Attempt to grab the next file, and return it
        current_file = globalVariable.file_list[globalVariable.current_file]
        globalVariable.current_file += 1
        return get_lines.get_lines(current_file)

    except IndexError:
        # If it fails, return False
        return False

