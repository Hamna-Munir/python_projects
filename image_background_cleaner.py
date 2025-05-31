from rembg import remove
from PIL import Image

input_path = r'c:\Users\AAA\Desktop\butterfly.jpg'
output_path = r'c:\Users\AAA\Desktop\butterfly_output.png'

inp = Image.open(input_path)
output = remove(inp)

output.save(output_path)


output.show()
