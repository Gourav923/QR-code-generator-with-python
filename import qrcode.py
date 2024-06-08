import qrcode

play= qrcode.make("https://game.chaotix.app/adda347/")

play.save("adda347.jpg")
play.show()