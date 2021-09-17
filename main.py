from watermark import WaterMark

una_imagen=WaterMark()
una_imagen.read_file("C:/Users/omejia/Downloads/resume-4.png")
una_imagen.add_watermark("que tranza")
una_imagen.show_watermark()
una_imagen.save_watermark()


