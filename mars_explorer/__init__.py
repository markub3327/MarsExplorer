from gymnasium.envs.registration import register

register(
    id="explorer-v1",
    entry_point="mars_explorer.envs:Explorer",
)

register(
    id="exploConf-v1",
    entry_point="mars_explorer.envs:ExplorerConf",
)
