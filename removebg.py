def run():
    print("\nRemoving background from letters...")
    import cv2
    import numpy as np
    import os

    directory='newfont'
    # #load image
    for filename in os.listdir(directory):
        if os.path.isdir("newfont"):
            os.chdir("newfont")
        if os.path.isdir("newfont"):
            os.chdir("newfont")
        if os.path.isfile(filename):
            img = cv2.imread(filename)

    # if True:
    #     filename='CamScanner 04-02-2022 16.19'
    #     img=cv2.imread('{}.jpg'.format(filename))

    # convert to graky
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # threshold input image as mask
            mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]

            # negate mask
            mask = 255 - mask

            # apply morphology to remove isolated extraneous noise
            # use borderconstant of black since foreground touches the edges
            kernel = np.ones((3,3), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

            # anti-alias the mask -- blur then stretch
            # blur alpha channel
            mask = cv2.GaussianBlur(mask, (0,0), sigmaX=2, sigmaY=2, borderType = cv2.BORDER_DEFAULT)

            # linear stretch so that 127.5 goes to 0, but 255 stays 255
            mask = (2*(mask.astype(np.float32))-255.0).clip(0,255).astype(np.uint8)

            # put mask into alpha channel
            result = img.copy()
            result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
            result[:, :, 3] = mask

            #save resulting masked image
            os.chdir("..")
            if not os.path.isdir("sem fundo"):
              os.mkdir("sem fundo")
            os.chdir("sem fundo")
            cv2.imwrite(filename.replace('jpg','png'), result)
            #cv2.imwrite('{}.png'.format(filename), result)
            os.chdir("..")

            # display result, though it won't show transparency
            #cv2.imshow("INPUT", img)
            #cv2.imshow("GRAY", gray)
            #cv2.imshow("MASK", mask)
            #cv2.imshow("RESULT", result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
run()