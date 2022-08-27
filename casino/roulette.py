import random

roulette_sectors = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22,18, 29, 7, 28, 12, 35, 3, 26]
sort_roulette_sectors = sorted(roulette_sectors)

def get_number():
    number = random.randint(0, 36)
    return number

def get_zero():
    zero_sector = roulette_sectors[0]
#outside_bets    
def get_low_high():
    low_sector = sort_roulette_sectors[1:19]
    high_sector = sort_roulette_sectors[18:37]

def get_red_black():
    red_sector = roulette_sectors[1::2]
    black_sector = roulette_sectors[2::2]

def get_even_odd():
    even_sector = sort_roulette_sectors[2::2]
    odd_sector = sort_roulette_sectors[1::2]

def get_dozens():
    first_dozens = sort_roulette_sectors[1:13]
    second_dozens = sort_roulette_sectors[13:25]
    third_dozens = sort_roulette_sectors[25:37]

def snake():
    snake_bet = [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34]