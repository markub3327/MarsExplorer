# MarsExplorer

<img src="img/GraphicalAbstract.png">

Mars Explorer is an openai-gym compatible environment designed and developed as an initial endeavor to bridge the gap between powerful Deep Reinforcement Learning methodologies and the problem of exploration/coverage of an unknown terrain. For full description and performance analysis, please check out our companion paper [MarsExplorer: Exploration of Unknown Terrains via Deep Reinforcement Learning and Procedurally Generated Environments](https://arxiv.org/abs/2107.09996)

## Achieved Results with PPO-based RL agent

<img src="img/intro.gif">

## Strong Generalization is the Key

Terrain diversification is one of the MarsExplorer kye attributes. For each episode, the general dynamics are determined by a specific automated process that has different levels of variation. These levels correspond to the randomness in the number, size, and positioning of obstacles, the terrain scalabality (size), the percentage of the terrain that the robot must explore to consider the problem solved and the bonus reward it will receive in that case. This procedural generation of terrains allows training in multiple/diverse layouts, forcing, ultimately, the RL algorithm to enable generalization capabilities, which are of paramount importance in real-life applicaiton where unforeseen cases may appear.

<img src="img/terrain.gif">

# Installation

## Quick Start

### Installation
You can install MarsExplorer environment by using the following command:

```shell
pip3 install git+https://github.com/markub3327/MarsExplorer@main
```

### Usage
```python
import gymnasium
import mars_explorer

env = gym.make('explorer-v1')

obs, info = env.reset()

done = False
while not done:
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated

env.close()
```

# Citation
If you find this useful for your research, please use the following:
```
@article{Koutras2021MarsExplorer,
  title={MarsExplorer: Exploration of Unknown Terrains via Deep Reinforcement Learning and Procedurally Generated Environments},
  author={Dimitrios I. Koutras and A. C. Kapoutsis and A. Amanatiadis and E. Kosmatopoulos},
  journal = {arXiv preprint arXiv:2107.09996},
  year={2021}
}
```
