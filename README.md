# MarsExplorer

<img src="utils/images_repo/GraphicalAbstract.png">

Mars Explorer is an openai-gym compatible environment designed and developed as an initial endeavor to bridge the gap between powerful Deep Reinforcement Learning methodologies and the problem of exploration/coverage of an unknown terrain. For full description and performance analysis, please check out our companion paper [MarsExplorer: Exploration of Unknown Terrains via Deep Reinforcement Learning and Procedurally Generated Environments](https://arxiv.org/abs/2107.09996)

## Achieved Results with PPO-based RL agent

<img src="utils/images_repo/intro.gif">

## Strong Generalization is the Key

Terrain diversification is one of the MarsExplorer kye attributes. For each episode, the general dynamics are determined by a specific automated process that has different levels of variation. These levels correspond to the randomness in the number, size, and positioning of obstacles, the terrain scalabality (size), the percentage of the terrain that the robot must explore to consider the problem solved and the bonus reward it will receive in that case. This procedural generation of terrains allows training in multiple/diverse layouts, forcing, ultimately, the RL algorithm to enable generalization capabilities, which are of paramount importance in real-life applicaiton where unforeseen cases may appear.

<img src="utils/images_repo/terrain.gif">

# Installation

## Quick Start

You can install MarsExplorer environment by using the following command:

```shell
pip3 install git+https://github.com/markub3327/MarsExplorer@main
```

# Testing

Please run the following command to make sure that everything works as expected:

```shell
python tests/test.py
```

## Manual Control

We have included a manual control of the agent, via the corresponding arrow keys. Run the manual control environment via:

```shell
python tests/manual.py
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
