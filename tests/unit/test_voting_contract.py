from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_voting_machine
import pytest
from brownie import exceptions


def test_vote_candidate(candidate, voter_id):
    # Arrange
    contract, _ = deploy_voting_machine()
    voter = get_account(voter_id)
    contract.voteCandidate(candidate, {"from": voter})
    # Assert
    assert contract.candidateToVotes(candidate) == 1
    with pytest.raises(exceptions.VirtualMachineError):
        # it should be not possible,so the test will pass
        contract.voteCandidate(candidate, {"from": voter})
