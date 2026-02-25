import argparse
import time

import gymnasium

from mars_explorer.envs.settings import DEFAULT_CONFIG as conf



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


if __name__ == "__main__":
    args = getArgs()

    env = gymnasium.make("mars_explorer:exploConf-v1", conf=conf)
    observation = env.reset()
    for _ in range(20):
        env.render()
        action = (
            env.action_space.sample()
        )  # your agent here (this takes random actions)
        observation, reward, done, info = env.step(action)

        if done:
            observation = env.reset()
        time.sleep(0.3)
    env.close()
