def readInpText(filename):
    fileContent = open(filename, 'r')
    hands, bids = [], []
    for line in fileContent.readlines():
        hand, bid = line.strip().split(' ')
        hands.append(hand)
        bids.append(int(bid))
    return hands, bids


def getHandTypeRank(hand):
    unique_cards = list(set(hand))
    if len(unique_cards) == 1:
        return 7    # Five of a kind
    if len(unique_cards) == 2:
        if hand.count(unique_cards[0]) == 4 or  hand.count(unique_cards[1]) == 4:
            return 6    # Four of a kind
        if (hand.count(unique_cards[0]) == 3 and hand.count(unique_cards[1]) == 2) or (hand.count(unique_cards[1])
                == 2 and hand.count(unique_cards[1]) == 3):
            return 5    # Full house
    if len(unique_cards) == 3:
        if hand.count(unique_cards[0]) == 3 or hand.count(unique_cards[1]) == 3 or hand.count(unique_cards[2]) == 3:
            return 4    # Three of a kind
        else:
            return 3    # Two pair
    if len(unique_cards) == 4:
        return 2    # One pair
    return 1    # High vard

def smallerHand(hand1, hand2):
    order = '23456789TJQKA'
    # print(hand1, hand2)
    for i in range(5):
        # print(hand1, order.index(hand1[i]))
        # print(hand2, order.index(hand2[i]))
        if order.index(hand1[i]) == order.index(hand2[i]):
            continue
        elif order.index(hand1[i]) < order.index(hand2[i]):
            return hand1
        else:
            return hand2
    # return hand1

def sortHands(hands, bids):
    for i in range(0, len(hands)):
        for j in range(i+1, len(hands)):
            if getHandTypeRank(hands[i]) > getHandTypeRank(hands[j]):
                hands[i], hands[j] = hands[j], hands[i]
                bids[i], bids[j] = bids[j], bids[i]
            if getHandTypeRank(hands[i]) == getHandTypeRank(hands[j]):
                if smallerHand(hands[i], hands[j]) != hands[i]:
                    hands[i], hands[j] = hands[j], hands[i]
                    bids[i], bids[j] = bids[j], bids[i]
    return hands, bids

def getTotalWinnings(hands, bids):
    hands, bids = sortHands(hands, bids)
    return sum([bids[i] * (i + 1) for i in range(len(bids))])

handsList, bidsList = readInpText('inp11.txt')
sortedHandsList, sortedBidsList = sortHands(handsList, bidsList)
# print(sortedHandsList, sortedBidsList)
print(getTotalWinnings(sortedHandsList, sortedBidsList))

# print(smallerHand('KK677', 'KTJJT'))
# print(smallerHand('T55J5', 'QQQJA'))



