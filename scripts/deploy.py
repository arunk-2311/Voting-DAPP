from scripts.helpful_scripts import get_account
from brownie import VotingMachine, config
import yaml


def add_candidates(contract, owner):
    for c in config['candidates']:
        contract.addCandidate(c, {"from": owner})


def deploy_voting_machine():
    owner = get_account()
    vote_contract = VotingMachine.deploy({"from": owner})
    add_candidates(vote_contract, owner)
    return vote_contract


def main():
    with open('./brownie-config.yaml') as f:
        doc = yaml.load(f, Loader=yaml.FullLoader)

    doc['deployedContract']['deployedAddress'] = deploy_voting_machine().address
    doc['deployedContract']['deployedABI'] = VotingMachine[-1].abi

    with open('./brownie-config.yaml', 'w') as f:
        yaml.dump(doc, f)
