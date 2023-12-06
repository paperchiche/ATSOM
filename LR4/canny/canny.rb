require 'vips'

input_image_path = 'C:/GitHub/ATSOM/LR4/curry.jpg'
image = Vips::Image.new_from_file(input_image_path)

canny_edges = image.canny

# Сохранение результата
canny_edges.write_to_file('canny_result.png')
