from xNerodia import *

def browse_extractData( xNerodia_session ):
    bow = xNerodia_session

    x = bow.iframe(id="mainweb").inner_html
    print( x )

    y = bow.div(class_name="cont").inner_html
    print( y )

    #xx = bow.div(class_name="container-right.fr")
    #print( xx )

    bow.scroll.to( [0,500] )


    # //*[@id="ifrm_02"]
    

    


#########

brwFireFox = launch_Simple()
outPrintTable = browse_extractData(brwFireFox)
