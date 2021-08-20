#================================================
#   IMPORTS
#================================================

from time import sleep
from picamera import PiCamera


#================================================
#   METHODS
#================================================


def preview(camera : object, t : int ):     # to start a preview
    '''
        input:
            t:  amount of time for preview;
    '''

    camera.start_preview()
    sleep( t )

    camera.stop_preview()

    return




def capture_and_save( camera : object, s_image_name : str, s_path : str ):
    '''
        input:
            s_image_name:   name of the image we want to save,
            s_path:         path where we want the image to be saved;
    '''

    camera.start_preview()
    sleep(3)

    camera.capture( s_path + '/' + s_image_name )

    camera.stop_preview()

    return



#================================================
#   MAIN
#================================================

if (__name__ == '__main__'):
    camera = PiCamera()

    preview( camera, 4 )     # preview testing

    capture_and_save( camera, 'my_pi_image.jpg', 'my_folder' )      # capturing an image



#================================================
#   END OF FILE
#================================================