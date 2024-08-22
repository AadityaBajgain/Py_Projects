import pyqrcode

user_input = input("give the url of which you want to make a qrcode: ")

url = pyqrcode.create(user_input)

url.png("user_input.png",scale=8)   #saves as png
