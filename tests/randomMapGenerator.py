import matplotlib.pyplot as plt

from mars_explorer.envs.settings import DEFAULT_CONFIG as conf
from mars_explorer.utils.randomMapGenerator import Generator

g = Generator(conf)
plt.imshow(g.get_map())
plt.show()
