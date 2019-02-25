from picamera import PiCamera
picam = PiCamera()
picam.resolution(1920,1080)
picam.framerate = 30
picam.start_Preview(1000)
