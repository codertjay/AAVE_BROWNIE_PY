from brownie import network, config, interface

from scripts.helpful_scripts import get_account


def get_weth():
    """
    Mints WETH by depositing ETH.
    :return:
    """
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(
        config['networks'][network.show_active()]['weth_token'])
    tx = weth.deposit({'from': account, 'value': 0.01 * 10 ** 18})
    tx.wait(1)
    print("Received 0.1 weth")
    return tx



def get_dai():
    """
    Mints WETH by depositing ETH.
    :return:
    """
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(
        config['networks'][network.show_active()]['dai_token'])
    tx = weth.deposit({'from': account, 'value': 0.001 * 10 ** 18})
    tx.wait(1)
    print("Received 0.1 weth")
    return tx



