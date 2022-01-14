import pyqrcode
import png
from pyqrcode import QRCode


s = "https://www.youtube.com/watch?v=LK6DlZ2uPpo&list=RDLK6DlZ2uPpo&start_radio=1"
url = pyqrcode.create(s) 
url.svg("myqr.svg", scale = 8)
url.png('myqr.png', scale = 6)