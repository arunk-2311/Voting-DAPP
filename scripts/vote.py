from brownie import Contract, config
from scripts.helpful_scripts import get_account
import yaml

# Contract is the brownie instance of the deployed contract
voting_contract = Contract.from_abi(
    "VotingMachine", config['deployedContract']['deployedAddress'], config['deployedContract']['deployedABI'])


def vote_candidate(candidate, voter_id):
    voter = get_account(voter_id)
    vote_tx = voting_contract.voteCandidate(candidate, {"from": voter})
    vote_tx.wait(1)


def view_votes():
    for c in config['candidates']:
        print(c, voting_contract.candidateToVotes(c))


def main():
    with open('./brownie-vote_like_this.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        vote_list = yaml.load(file, Loader=yaml.FullLoader)

    print(vote_list)
    for i in range(len(vote_list)):
        for key in vote_list[i].keys():
            vote_candidate(key, vote_list[i][key])
    view_votes()
