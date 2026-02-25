import argparse

import gymnasium
import matplotlib.pyplot as plt
import numpy as np
import pygame as pg

from mars_explorer.envs.settings import DEFAULT_CONFIG as conf


def saveRend(rend, time_step):
    plt.rcParams["axes.grid"] = False
    plt.axis("off")
    plt.imshow(rend)
    # plt.savefig(f"{time_step}_env.png", bbox_inches='tight')
    plt.savefig(f"{time_step}_env.png", bbox_inches="tight", dpi=300)
    plt.close()


def getArgs():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-w", "--warm-up", default=0, type=int, help="Number of warm up games "
    )
    argparser.add_argument(
        "-g", "--games", default=10, type=int, help="Games to be played"
    )
    argparser.add_argument(
        "-s",
        "--save",
        default=False,
        action="store_true",
        help="Save each rendered image",
    )
    return argparser.parse_args()


def event():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                close()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    close()
                if event.key == pg.K_LEFT:
                    return 1
                if event.key == pg.K_RIGHT:
                    return 0
                if event.key == pg.K_UP:
                    return 3
                if event.key == pg.K_DOWN:
                    return 2


def play_game(env):
    total_reward = 0.0
    observation = env.reset()
    env.render()
    for time_step in range(1000):
        action = event()
        obs, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            break
        rendered = env.render()

        if args.save:
            saveRend(rendered, time_step)

    return total_reward


def close():
    print(f"\nManual game play finished after {len(rewards)} games")
    print(f"Average reward is {np.average(rewards)}[m^2]")
    print(f"Standar deviation {np.std(rewards)}")
    env.close()
    quit()


if __name__ == "__main__":
    pg.init()
    args = getArgs()

    env = gymnasium.make("mars_explorer:exploConf-v1", conf=conf)

    rewards = []
    for game in range(args.games + args.warm_up):
        total_reward = play_game(env)
        print(f"Total reward for game:{game} is {total_reward}")
        rewards.append(total_reward)

    close()
