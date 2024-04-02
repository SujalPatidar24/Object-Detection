def findPokerHand(hand):

    ranks = []
    suits = []
    possibleRanks = []

    for card in hand:
        if(len(card)==2):
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]

        if rank == 'A':
            rank = 14

        if rank == 'K':
            rank = 13

        if rank == 'Q':
            rank = 12

        if rank == 'J':
            rank = 11

        ranks.append(int(rank))
        suits.append(suit)

    sortedRanks = sorted(ranks)
    print(sortedRanks)

    # Royal Flush, Staright Flush,  Flush

    if suits.count(suits[0])==5:

        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks :
            possibleRanks.append(10)
        elif all(sortedRanks[i] == sortedRanks[i-1]+1 for i in range(1,len(sortedRanks))):
            possibleRanks.append(9)
        else :
            possibleRanks.append(6)


    # Straight
    if all(sortedRanks[i] == sortedRanks[i - 1] + 1 for i in range(1, len(sortedRanks))):
        possibleRanks.append(5)

    handUniqueVals = list(set(sortedRanks))

    # Four of a Kind, Full House
    if len(handUniqueVals) ==2:
        for val in handUniqueVals:
            if sortedRanks.count(val)==4:
                possibleRanks.append(8)
            if sortedRanks.count(val)==3:
                possibleRanks.append(7)

    # Three of a Kind, Two Pair
    if len(handUniqueVals) == 3:
        for val in handUniqueVals:
            if sortedRanks.count(val) == 3:
                possibleRanks.append(4)
            if sortedRanks.count(val) == 2:
                possibleRanks.append(3)


    # Pair
    if len(handUniqueVals)==4 :
        possibleRanks.append(2)

    if not possibleRanks:
        possibleRanks.append(1)

    pokerHnadRanks = {10:"Royal Flush", 9: "Straight Flush", 8:"Four of a Kind", 7:"Full House", 6:"Flush", 5:"Straight", 4:"Three of a Kind", 3:"Two Pair", 2:"Pair", 1:"High Card"}

    output = pokerHnadRanks[max(possibleRanks)]
    print(hand, output)

    return output



if __name__ == "__main__":
    findPokerHand(["AH","KH","QH","JH","10H"])    # ROYAL FLUSH
    findPokerHand(["QC", "JC", "10C", "9C", "8C"])  # STRAIGHT FLUSH
    findPokerHand(["5C", "5S", "5H", "5D", "QH"])  # FOUR OF A KIND
    findPokerHand(["2H", "2D", "2S", "10H", "10C"])  # FULL HOUSE
    findPokerHand(["2D", "KD", "7D", "6D", "5D"])  # FLUSH
    findPokerHand(["JC", "10C", "9C", "8C", "7D"])  # STRAIGHT
    findPokerHand(["10H", "10C", "10D", "2D", "5S"])  # THREE OF A KIND
    findPokerHand(["KD", "KH", "5C", "5S", "6D"])  # TWO PAIR
    findPokerHand(["2D", "2S", "9C", "KD", "10C"])  # PAIR
    findPokerHand(["KD", "5H", "2D", "10C", "JH"])  # HIGH CARD
