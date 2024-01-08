import re

def parse_cards(input_str):
    cards = []
    for line in input_str.splitlines():
        parts = line.split(":")
        card_no = int(re.findall(r'\d+', parts[0])[0])
        winning_nums, all_nums = [part.split() for part in parts[1].split("|")]
        cards.append((card_no, set(winning_nums), set(all_nums)))
    return cards

def process_cards(cards):
    card_counts = {i: 0 for i in range(1, len(cards) + 1)}
    for card_no, winning_nums, all_nums in cards:
        matches = len(winning_nums.intersection(all_nums))
        card_counts[card_no] += 1  # Original card
        for i in range(1, matches + 1):
            if card_no + i <= len(cards):
                card_counts[card_no + i] += card_counts[card_no]

    return card_counts

def count_total_cards(card_counts):
    return sum(card_counts.values())

def main(input_str):
    cards = parse_cards(input_str)
    card_counts = process_cards(cards)
    total_cards = count_total_cards(card_counts)
    print(f"Total number of cards: {total_cards}")

# Example usage
input_str = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

main(input_str)
