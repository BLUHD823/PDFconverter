from PIL import Image
image1 = Image.open("01877fce193bf92ae262a9d0c99c7fa8.jpg")
img1 = image1.convert('RGB')
img1.save("output.pdf")