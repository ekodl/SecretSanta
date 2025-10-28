import copy
import random

from src.emailer import email_results
from src.file_read_writer import load_participants, load_illegal_pairs, save_matches


def matchmake(participants, illegal_pairs, please_stop):

    if please_stop == 0:
        raise ValueError("We're going crazy and stopping stack overflows")

    # make copy of list - awaiting assignment (needs giftee)
    part_sublist = [sublist[0] for sublist in participants]
    needs_giftee_list = [sublist[0] for sublist in copy.deepcopy(copy.deepcopy(participants))]
    gifting_pairs = []

    # for each participant...
    for part in part_sublist:
        # make copy of needs giftee list
        eligible_matches = copy.deepcopy(needs_giftee_list)

        # remove anyone in the illegal pairs list as options
        # each person is listed as an illegal pairing for themselves
        for illegal in illegal_pairs:
            if illegal[0] == part:
                if illegal[1] in eligible_matches:
                    eligible_matches.remove(illegal[1])

        # randomly generate an index and assign (add to return list)
        giftee = random.choice(eligible_matches)
        gifting_pairs.append([part, giftee])

        # remove person from needs giftee list
        needs_giftee_list.remove(giftee)

    # if, after for loop has executed through master list,
    # there's anyone left in the needs giftee list... we startin over
    if len(needs_giftee_list) > 0:
        gifting_pairs = matchmake(participants, illegal_pairs, please_stop - 1)

    return gifting_pairs


if __name__ == '__main__':

    # load in the list of participants
    participant_members = load_participants()

    # load in the list of illegal pairings
    illegal_matches = load_illegal_pairs()

    # do some matchmaking
    matches = matchmake(participant_members, illegal_matches, 5)

    final = []
    for match in matches:
        strMatch = f"{match[0]}--->{match[1]}"
        final.append(strMatch)

    save_matches(final)

    email_results(matches, participant_members)
