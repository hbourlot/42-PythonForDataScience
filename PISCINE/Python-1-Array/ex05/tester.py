import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

array = ft_load("a.jpg")

# ft_red(array)
# ft_invert(array)
# ft_green(array)
# ft_blue(array)
plt.imshow(ft_grey(array))
plt.show()
# print(ft_invert.__doc__)
