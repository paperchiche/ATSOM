require 'ruby-vips'

im = Vips::Image.new_from_file("C:/Users/20art/Desktop/01.jpg")

im = im.gaussblur(4.0)

im.write_to_file("C:/GitHub/ATSOM/LR3/rubyblur.jpg")
