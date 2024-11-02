import random as rng
from collections import Counter
import re
import os
from datetime import datetime

def main():
    
    greeting()
    print('Let\'s roll these bones, shall we?')

    print('1. Show Rules'
          '\n2. Show Leaderboard'
          '\n3. Play'
          '\n4. Exit')
    choice = int(input('Select an option by typing the corresponding numeral: '))

    while choice != 4:

        try: 

            if choice == 1:
                rules()
            elif choice == 2:
                read_leaderboard(filename='highscores.txt', top_n=10)
            elif choice == 3:
                prep_match()
            elif choice < 1 or choice > 4:
                print('Input must be "1", "2", "3" or "4" corresponding to the list above.')
                choice = int(input('Select an option by typing the corresponding numeral: '))

            print('\nLet\'s roll these bones, shall we?')
            print('1. Show Rules'
                  '\n2. Show Leaderboard'
                  '\n3. Play'
                  '\n4. Exit')
            choice = int(input('Select an option by typing the corresponding numeral: ')) 

        except ValueError:
            print('Input must be an integer, not a string.')
            choice = int(input('Select an option by typing the corresponding numeral: '))
    
    
    goodbye()


def rules():

    print('Listen up now, here is how Yatzy is played:')
    print('\nSetup'
          '\nYatzy is played with 2 or more players (up to six in this iteration),'
          '\n5 standard six-sided dice, a special Yatzy scorecard and a single session'
          '\nis 15 rounds long, one for each category of the scorecard')
    
    print('\nObjective'
          '\nThe objective of the game is to score as many points as possible'
          '\nby rolling the dice and meeting the scoring categorys as best as possible.'
          '\nThe player with the most points wins the game.')
    
    print('\nHow to play'
          '\nOn a players turn, they roll all five dice. The player may reroll one, some or all dice'
          '\nup to two more times (so max. 3 rolls in total) to achieve a better combination.'
          '\nAfter the third roll, the player must choose a category on the scorecard where they will'
          '\nrecord the score (even if the resulting score is 0). Once a category is used, it may not'
          '\nbe used again.')
    
    print('\nThe scorecard'
          '\nThe scorecard is divided into two sections, the Upper Section (also "Bonus Section") and the'
          '\nLower Section (also "Combination Section")')
    
    print('\nThe Upper Section'
          '\nThe Upper Section has 6 categories, one for each eye-count on the die. In these categories the'
          '\nrolled numbers on the dice corresponding to the chosen category are summed up (i.e. if Twos is chosen'
          '\nall 2s rolled are summed up for the score of the category)'
          '\nExample: 2, 2, 3, 5, 2 are rolled and Twos is chosen --> Score = 2 + 2 + 2 = 6'
          '\nIf the total score of a player in the Upper Section is 63 or more, that player gets a 50-Point bonus.')
    
    print('\nThe Lower Section'
          '\nThe Lower Section is divided into 9 categories for different combinations:'
          '\nOne Pair: Two dice showing the same number --> for example 2, 2, 4, 6, 1 are rolled --> Score = 2 + 2 = 4'
          '\nTwo Pairs: Four dice showing two different pairs --> for example 2, 2, 6, 6, 1 are rolled --> Score = 2 + 2 + 6 + 6 = 16'
          '\nThree of a Kind: Three dice showing the same number --> for example 2, 2, 2, 4, 6 are rolled --> Score = 2 + 2 + 2 = 6'
          '\nFour of a Kind: Four dice showing the same number --> for example 2, 2, 2, 2, 6 are rolled --> Score = 2 + 2 + 2 + 2 = 8'
          '\nSmall Straight: smaller sequence of 5 consecutive numbers (1, 2, 3, 4, 5) --> Score: 15 Points'
          '\nLarge Straight: larger sequence of 5 consecutive numbers (2, 3, 4, 5, 6) --> Score: 20 Points'
          '\nFull House: Combination of Three of a Kind and One Pair --> for example 2, 2, 2, 4, 4 --> Score: Sum of all dice'
          '\nChance: Any combination of dice --> Score: Sum of all dice'
          '\nYatzy/Five of a Kind: All dice show the same number --> for example 2, 2, 2, 2, 2 --> Score: 50 Points')

    print('\nWinning the Game'
          '\nWhen all 15 rounds are played, the scores are totaled. The highest score including the bonuses wins.'
          '\nThe highest possible score is 375 points, everything over 300 is considered really good and a "normal" score usually'
          '\nis between 150 and 250. A player scoring below 150 has to do the dishes the rest of the week *wink wink*.')


def greeting():

    greeting_phrases = [
        'It was the worst torture in the world. Waiting to see if you\'d come back.',
        'Lok\'tar Ogar!',
        'Mok\'ra',
        'Dabu!',
        'Lok\'narash!',
        'For the Horde!',
        'Welcome to the home of true science, where we embrace what the living fear.',
        'Take a seat, though it\'s not a cozy one.',
        'What do you want? Make it quick.',
        'You\'re looking a little pale. Have you been out in the sun?',
        'Welcome, but don\'t linger. The living are not welcome here.',
        'You have an interesting smell... what is it?',
        'Ah, a customer! Or a meal?',
        'The Forsaken will rise again! Now, what do you want?',
        'You got coin? Me got deals!',
        'You need something? Me help!',
        'Me always open for business!',
        'Welcome to da ziggurat, mon!',
        'Wot\'s happening, mon?',
        'You be needin\' somethin\'?',
        'You tink ya be tough, eh?',
        'I be watchin\' you, friend.',
        'Me not got all day, mon!',
        'I don\'t got it, you don\'t want it.',
        'Anaria shola.',
        'Bal\'a dash, malanore.',
        'Anu belore dela\'na.',
        'Shorel\'aran.',
        'Your arrival is most fortuitous.',
        'Hello, traveler. What brings you to our lands?',
        'May your heart be light and your spirit strong.',
        'The plains whisper of your arrival.',
        'Welcome, friend. The ancestors are pleased to see you.',
        'Hey, you! Need something?',
        'You look like you got coin!',
        'Keep your eyes open, or you might miss a steal!',
        'Don\'t be shy! I don\'t bite... much.',
        'What\'s your fancy today, eh?',
        'Hello there!',
        'Greetings, my young Padawan.',
        'I\'ve got a bad feeling about this.',
        'Welcome to the Resistance.',
        'Hey, what are you doing here?',
        'You\'re a Jedi, aren\'t you?',
        'Welcome to Rivendell.',
        'Frodo, my dear!',
        'Gandalf! Is that you?',
        'What news from the North?',
        'Welcome to the realm of Gondor.',
        'You have come at a time of great need.',
        'Let this be the hour when we draw swords together. Fell deeds awake.',
        'Courage will now be your best defence against the storm that is at hand - that and such hope as I bring.',
        'The Beacons of Minas Tirith! The Beacons are lit! Gondor calls for aid.',
    ]
    
    selection = rng.randint(0, len(greeting_phrases) - 1)
    print(f'{greeting_phrases[selection]}')


def goodbye():

    goodbye_phrases = [
        'The Force will be with you, always.',
        'Goodbye, old friend. May the Force be with you.',
        'Remember, the Force will be with you. Always.',
        'You were my brother, Anakin! I loved you!',
        'See you around, kid.',
        'I go to my fathers, in whose mighty company I shall not now feel ashamed.',
        'I will not say: do not weep; for not all tears are an evil.',
        'It is time, Frodo.',
        'End? No, the journey doesn\'t end here. Death is just another path, one that we all must take.',
        'May the odds be ever in your favor.',
        'Stay alive.',
        'Watch your back.',
        'Trust no one.',
        'Beware the living.',
        'The Dark Lady watches over you.',
        'Death is just the beginning.',
        'The grave is the only resting place.',
        'Stay away from da voodoo.',
        'Be seein\' ya.',
        'Spirits be with ya, mon.',
        'Da Loa be watchin\' ya.',
        'You be carefull now, mon.',
        'Go in peace.',
        'Walk with the Earth Mother.',
        'Lok\'tar, friend.',
        'Strength and honor.',
        'For the Horde!',
        'Go with honor.',
        'May your blades never dull.',
        'May the Eternal Sun guide your path.',
        'Glory to the Sin\'dorei!',
        'Until we meet again.',
        'Stay vigilant.',
        'The day of reckoning is at hand.',
        'Time is money, friend!',
        'I\'ve got mouths to feed, pal!',
        'Come back anytime!',
        'The pleasure was all mine.',
        'Don\'t let the door hit you on the way out!',
        'Don\'t do anything I wouldn\'t do!',
        'Gotta run! Money won\'t make itself!',
        'G-E-L friend: gambling, tinkering, laundering.',
        'A turtle made it to the water!!',
        'Don\'t adventures ever have an end? I suppose not. Someone else always has to carry on the story.',
    ]

    selection = rng.randint(0, len(goodbye_phrases) - 1)

    print(f'{goodbye_phrases[selection]}')


def prep_match():

    print('\nStarting a match of Yatzy...')

    while True: #sometimes easy > pretty

        try:

            players = int(input('How many players are participating this match? Enter the number of players (1-6) or 0 to exit: '))

            if players == 0:
                break
            else:
                play_yatzy(players)
                break

        except ValueError:
            print('Input must be a number (not a string) between 1 and 6 to play or 0 to exit to the main menu.')
            players = int(input('How many players are participating this match? Enter the number of players (1-6) or 0 to exit: '))

def play_yatzy(number):
    
    score_categories = [
        '1. Ones (sum ones from the dice)',
        '2. Twos (sum twos from the dice)',
        '3. Threes (sum threes)',
        '4. Fours (sum fours)',
        '5. Fives (sum fives)',
        '6. Sixes (sum sixes)',
        '7. One Pair (i.e. <2, 2>, 3, 4, 5)',
        '8. Two Pairs (<2, 2, 3, 3>, 4)',
        '9. Three of a Kind (<2, 2, 2>, 3, 4)',
        '10. Four of a Kind (<2, 2, 2, 2>, 3)',
        '11. Small Straight (1, 2, 3, 4, 5)',
        '12. Large Straight (2, 3, 4, 5, 6)',
        '13. Full House (One Pair and Three of a Kind)',
        '14. Chance (Sum of all dice)',
        '15. Yatzy (Five of one Kind)',
        'Bonus',
        'Total',
    ]

    player_list = []

    for i in range(number):
        player_name = input(f'Enter a name for Player {i + 1}: ')
        player_scorecard = {
            'Player': player_name,
            'Scores': [{'Category': score_categories[j], 'Score': 0} for j in range(17)]
        }
        player_list.append(player_scorecard)
        print(f'{player_name} has been added to your scorecard.\n')

    print('Here is the scorecard for your match:')
    show_scorecard(player_list, score_categories)

    print('\nBefore you head into the match, do you want to review the rules once again?')
    answer = int(input('Enter "1" to see the rules or "2" to continue with the match (enter as number, not as word): '))

    while answer != 2:
        
        try:

            if answer == 1:
                rules()
                answer = 2
            elif answer < 1 or answer > 2:
                print('Input must either be "1" or "2".')
                answer = int(input('Enter "1" to see the rules or "2" to continue with the match (enter as number, not as word): '))

        except ValueError:
            print('Input must be an integer, not a string.')
            answer = int(input('Enter "1" to see the rules or "2" to continue with the match (enter as number, not as word): '))

    print('\nLet\'s get this match started then, shall we? Buckle up, here we go!')

    for k in range(15):
        print(f'Round {k + 1} is about to beginn.')
        
        for l in range(number):
            print(f'Player {l + 1}, your turn.')

            print('\nWould you like to check the score before you continue? It will also display the different score Categories with examples to provide some help.')
            check = int(input('Enter "1" to see the scorecard or "2" to continue the game.'))

            while check != 2:

                try:

                    if check == 1:
                        show_scorecard(player_list, score_categories)
                        check = 2
                    elif check > 2 or check < 1:
                        print('Input must be either "1" or "2".')
                        check = int(input('Enter "1" to see the scorecard or "2" to continue the game.'))
                
                except ValueError:
                    print('Input must be "1" or "2" (without quotations) as integers. not as string.')
                    check = int(input('Enter "1" to see the scorecard or "2" to continue the game.'))

            input('Press enter to roll your dice.')

            roll_1 = []
            roll_2 = []
            roll_3 = []
            die_1 = rng.randint(1, 6)
            die_2 = rng.randint(1, 6)
            die_3 = rng.randint(1, 6)
            die_4 = rng.randint(1, 6)
            die_5 = rng.randint(1, 6)
            roll_1.extend([die_1, die_2, die_3, die_4, die_5])
            print(f'Your roll: {roll_1}')

            roll_check = str(input('Enter the indexes of the dice you want to keep (1-5) seperated with a comma or space (for example: 1, 3, 5 or 2 4 5), "6" to keep all (and forfeiting both rerolls) or "0" to reroll all: '))
            reroll = []

            while roll_check != "6":

                if roll_check == "0":
                    die_1_2 = rng.randint(1, 6)
                    die_2_2 = rng.randint(1, 6)
                    die_3_2 = rng.randint(1, 6)
                    die_4_2 = rng.randint(1, 6)
                    die_5_2 = rng.randint(1, 6)
                    roll_2.extend([die_1_2, die_2_2, die_3_2, die_4_2, die_5_2])
                    print(f'Your dice after the first reroll: {roll_2}')

                    roll_check_2 = str(input('Enter the indexes of the dice you want to keep (1-5) seperated with a comma or space (for example: 1, 3, 5 or 2 4 5), "6" to keep all (and forfeiting the last reroll) or "0" to reroll all: '))
                    reroll_2 = []

                    while roll_check_2 != "6":

                        if roll_check_2 == "0":
                            die_1_3 = rng.randint(1, 6)
                            die_2_3 = rng.randint(1, 6)
                            die_3_3 = rng.randint(1, 6)
                            die_4_3 = rng.randint(1, 6)
                            die_5_3 = rng.randint(1, 6)
                            roll_3.extend([die_1_3, die_2_3, die_3_3, die_4_3, die_5_3])
                            print(f'Your final dice: {roll_3}\n')
                            print('\nWhat category would you like to fill in this turn? See the above scorecard for the possible categorys and their respective meaning.'
                                  '\nRemember, each category can only be chosen once.')
                            add_score(player_list, l, roll_3)
                            roll_check = "6"
                            roll_check_2 = "6"
                            
                        else:

                            reroll_2 = [int(num) for num in re.findall(r'\b[1-5]\b', roll_check_2)]

                            for indice in reroll_2:
                                roll_3.append(roll_2[indice - 1])

                            for z in range(5 - len(roll_3)):
                                die = rng.randint(1, 6)
                                roll_3.append(die)

                            print(f'Your final dice: {roll_3}\n')
                            print('\nWhat category would you like to fill in this turn? See the above scorecard for the possible categorys and their respective meaning.'
                                  '\nRemember, each category can only be chosen once.')
                            add_score(player_list, l, roll_3)
                            roll_check = "6"
                            roll_check_2 = "6"
                    
                    if not roll_3:
                        add_score(player_list, l, roll_2)
                        roll_check = "6"

                else:

                    reroll = [int(num) for num in re.findall(r'\b[1-5]\b', roll_check)]

                    for index in reroll:
                        roll_2.append(roll_1[index - 1])

                    for y in range(5 - len(roll_2)):
                        new_die = rng.randint(1, 6)
                        roll_2.append(new_die)

                    print(f'Your dice after the first reroll: {roll_2}\n')
                    
                    roll_check_2 = str(input('Enter the indexes of the dice you want to keep (1-5) seperated with a comma or space (for example: 1, 3, 5 or 2 4 5), "6" to keep all (and forfeiting the last reroll) or "0" to reroll all: '))
                    reroll_2 = []

                    while roll_check_2 != "6":

                        if roll_check_2 == "0":
                            die_1_3 = rng.randint(1, 6)
                            die_2_3 = rng.randint(1, 6)
                            die_3_3 = rng.randint(1, 6)
                            die_4_3 = rng.randint(1, 6)
                            die_5_3 = rng.randint(1, 6)
                            roll_3.extend([die_1_3, die_2_3, die_3_3, die_4_3, die_5_3])
                            print(f'Your final dice: {roll_3}\n')
                            print('\nWhat category would you like to fill in this turn? See the above scorecard for the possible categorys and their respective meaning.'
                                  '\nRemember, each category can only be chosen once.')
                            add_score(player_list, l, roll_3)
                            roll_check = "6"
                            roll_check_2 = "6"
                            
                        else:

                            reroll_2 = [int(num) for num in re.findall(r'\b[1-5]\b', roll_check_2)]

                            for indice in reroll_2:
                                roll_3.append(roll_2[indice - 1])

                            for z in range(5 - len(roll_3)):
                                die = rng.randint(1, 6)
                                roll_3.append(die)

                            print(f'Your final dice: {roll_3}\n')
                            print('\nWhat category would you like to fill in this turn? See the above scorecard for the possible categorys and their respective meaning.'
                                  '\nRemember, each category can only be chosen once.')
                            add_score(player_list, l, roll_3)
                            roll_check = "6"
                            roll_check_2 = "6"
                    
                    if not roll_3:
                        add_score(player_list, l, roll_2)
                        roll_check = "6" 
                        roll_check_2 = "6"   

            if not roll_3 and not roll_2:
                print('\nWhat category would you like to fill in this turn? See the above scorecard for the possible categorys and their respective meaning.'
                      '\nRemember, each category can only be chosen once.')
                add_score(player_list, l, roll_1)
                roll_check = "6"
                

        update_bonus_total(player_list)

    show_scorecard(player_list, score_categories)
    display_winner(player_list)
    collect_highscores(player_list, filename='highscores.txt')
    input('\nPress enter to return to the main menu: ')


def add_score(participants_list, turn, roll):

    while True:

        try:

            choice = int(input('Enter an integer corresponding to the number of the category you want to fill in (1-15, see scorecard above): '))

            if choice > 15 or choice < 1:
                print('Input must be an integer between and including 1 and 15.')
                continue

            elif choice == 1:

                if participants_list[turn]['Scores'][0]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                else:
                    score_sum = 0
                    for d in roll:
                        if d == 1:
                            score_sum += d

                    if score_sum == 0:
                        participants_list[turn]['Scores'][0]['Score'] = "x"
                        print('You scored 0 points in this category, so it has been crossed out.')
                        break
                    
                    else:
                        participants_list[turn]['Scores'][0]['Score'] = score_sum
                        print(f'"Ones" successfully filled in. You scored a total of {score_sum} points for the Category "Ones".')                        
                        break

            elif choice == 2:
                
                if participants_list[turn]['Scores'][1]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                else:
                    score_sum = 0
                    for d in roll:
                        if d == 2:
                            score_sum += d

                    if score_sum == 0:
                        participants_list[turn]['Scores'][1]['Score'] = "x"
                        print('You scored 0 points in this category, so it has been crossed out.')                        
                        break
                    
                    else:
                        participants_list[turn]['Scores'][1]['Score'] = score_sum
                        print(f'"Twos" successfully filled in. You scored a total of {score_sum} points for the Category "Twos".')                        
                        break

            elif choice == 3:

                if participants_list[turn]['Scores'][2]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                else:
                    score_sum = 0
                    for d in roll:
                        if d == 3:
                            score_sum += d
                    
                    if score_sum == 0:
                        participants_list[turn]['Scores'][2]['Score'] = "x"
                        print('You scored 0 points in this category, so it has been crossed out.')                        
                        break
                    
                    else:
                        participants_list[turn]['Scores'][2]['Score'] = score_sum
                        print(f'"Threes" successfully filled in. You scored a total of {score_sum} points for the Category "Threes".')                        
                        break

            elif choice == 4:

                if participants_list[turn]['Scores'][3]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                else:
                    score_sum = 0
                    for d in roll:
                        if d == 4:
                            score_sum += d

                    if score_sum == 0:
                        participants_list[turn]['Scores'][3]['Score'] = "x"
                        print('You scored 0 points in this category, so it has been crossed out.')                        
                        break
                    
                    else:
                        participants_list[turn]['Scores'][3]['Score'] = score_sum
                        print(f'"Fours" successfully filled in. You scored a total of {score_sum} points for the Category "Fours".')                        
                        break

            elif choice == 5:

                if participants_list[turn]['Scores'][4]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                else:
                    score_sum = 0
                    for d in roll:
                        if d == 5:
                            score_sum += d

                    if score_sum == 0:
                        participants_list[turn]['Scores'][4]['Score'] = "x"
                        print('You scored 0 points in this category, so it has been crossed out.')                        
                        break
                    
                    else:
                        participants_list[turn]['Scores'][4]['Score'] = score_sum
                        print(f'"Fives" successfully filled in. You scored a total of {score_sum} points for the Category "Fives".')                        
                        break

            elif choice == 6:

                if participants_list[turn]['Scores'][5]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                else:
                    score_sum = 0
                    for d in roll:
                        if d == 6:
                            score_sum += d

                    if score_sum == 0:
                        participants_list[turn]['Scores'][5]['Score'] = "x"
                        print('You scored 0 points in this category, so it has been crossed out.')                        
                        break
                    
                    else:
                        participants_list[turn]['Scores'][5]['Score'] = score_sum
                        print(f'"Sixes" successfully filled in. You scored a total of {score_sum} points for the Category "Sixes".')                        
                        break

            elif choice == 7:

                if participants_list[turn]['Scores'][6]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                else:
                    dice_count = Counter(roll)
                    score_sum = max(die * 2 for die, count in dice_count.items() if count >= 2)

                    if score_sum == 0:
                        participants_list[turn]['Scores'][6]['Score'] = "x"
                        print('You scored 0 points in this category, so it has been crossed out.')                        
                        break

                    else:
                        participants_list[turn]['Scores'][6]['Score'] = score_sum
                        print(f'"One Pair" successfully filled in. You scored a total of {score_sum} points for the Category "One Pair".')                        
                        break

            elif choice == 8:

                if participants_list[turn]['Scores'][7]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                else:
                    dice_count = Counter(roll)
                    score_sum = sum(die * 2 for die, count in dice_count.items() if count >= 2)

                    if score_sum == 0:
                        participants_list[turn]['Scores'][7]['Score'] = "x"
                        print('You scored 0 points in this category, so it has been crossed out.')                        
                        break

                    else:
                        participants_list[turn]['Scores'][7]['Score'] = score_sum
                        print(f'"Two Pair" successfully filled in. You scored a total of {score_sum} points for the Category "Two Pair".')                        
                        break

            elif choice == 9:

                if participants_list[turn]['Scores'][8]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                else:
                    dice_count = Counter(roll)
                    score_sum = sum(die * 3 for die, count in dice_count.items() if count >= 3)

                    if score_sum == 0:
                        participants_list[turn]['Scores'][8]['Score'] = "x"
                        print('You scored 0 points in this category, so it has been crossed out.')                        
                        break

                    else:
                        participants_list[turn]['Scores'][8]['Score'] = score_sum
                        print(f'"Three of a Kind" successfully filled in. You scored a total of {score_sum} points for the Category "Three of a Kind".')                        
                        break

            elif choice == 10:

                if participants_list[turn]['Scores'][9]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                else:
                    dice_count = Counter(roll)
                    score_sum = sum(die * 4 for die, count in dice_count.items() if count >= 4)

                    if score_sum == 0:
                        participants_list[turn]['Scores'][9]['Score'] = "x"
                        print('You scored 0 points in this category, so it has been crossed out.')                        
                        break

                    else:
                        participants_list[turn]['Scores'][9]['Score'] = score_sum
                        print(f'"Four of a Kind" successfully filled in. You scored a total of {score_sum} points for the Category "Four of a Kind".')                        
                        break

            elif choice == 11:
                small_straight = [1, 2, 3, 4, 5]

                if participants_list[turn]['Scores'][10]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                elif set(small_straight).issubset(set(roll)):
                    participants_list[turn]['Scores'][10]['Score'] = 15
                    print('You scored 15 for your Small Straight!')                    
                    break

                else:
                    participants_list[turn]['Scores'][10]['Score'] = "x"
                    print('You scored 0 points in this category, so it has been crossed out.')                   
                    break

            elif choice == 12:
                large_straight = [2, 3, 4, 5, 6]

                if participants_list[turn]['Scores'][11]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                elif set(large_straight).issubset(set(roll)):
                    participants_list[turn]['Scores'][11]['Score'] = 20
                    print('You scored 20 for your Large Straight!')                   
                    break

                else:
                    participants_list[turn]['Scores'][11]['Score'] = "x"
                    print('You scored 0 points in this category, so it has been crossed out.')                   
                    break

            elif choice == 13:

                if participants_list[turn]['Scores'][12]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                elif any(count == 3 for count in Counter(roll).values()) and any(count == 2 for count in Counter(roll).values()):
                    score_sum = sum(roll)
                    participants_list[turn]['Scores'][12]['Score'] = score_sum
                    print(f'Your Full House equals a score of {score_sum} and has been added to the scorecard.')                   
                    break

                else:
                    participants_list[turn]['Scores'][12]['Score'] = "x"
                    print('You scored 0 points in this category, so it has been crossed out.')                    
                    break

            elif choice == 14:

                if participants_list[turn]['Scores'][13]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                else:
                    score_sum = sum(roll)
                    participants_list[turn]['Scores'][13]['Score'] = score_sum
                    print(f'Your dice equal a score of {score_sum}, which has been added to the scorecard.')                    
                    break

            elif choice == 15:

                if participants_list[turn]['Scores'][14]['Score'] != 0:
                    print('Oi, no cheating! I said every category may only be filled once, did I not? Be better and try again.')
                    continue

                elif any(count == 5 for count in Counter(roll).values()):
                    participants_list[turn]['Scores'][14]['Score'] = 50
                    print('You have been awarded 50 points for your Yatzy! Congratulations!')                   
                    break
                
                else:
                    participants_list[turn]['Scores'][14]['Score'] = "x"
                    print('You scored 0 points in this category, so it has been crossed out.')                    
                    break


        except ValueError:
            print('Input must be an integer, not a string.')
            choice = int(input('Enter an integer corresponding to the number of the category you want to fill in (1-15, see scorecard above): '))
                           

def update_bonus_total(lst):

    for player_scorecard in lst:

        upper_section_total = sum(score['Score'] for score in player_scorecard['Scores'][:6] if isinstance(score['Score'], int))
        player_scorecard['Scores'][15]['Score'] = 50 if upper_section_total >= 63 else 0

        total_score = sum(score['Score'] for score in player_scorecard['Scores'][:15] if isinstance(score['Score'], int)) + player_scorecard['Scores'][15]['Score']
        player_scorecard['Scores'][16]['Score'] = total_score


def show_scorecard(lst_1, lst_2):

    header = 'Category'.ljust(45) + '|' + ''.join(name.center(15) + '|' for name in [player['Player'] for player in lst_1]) #comprehension to extract player names from player_list/lst_1
    print(header)                                                                                                           #->gets player dictionarys, extracts values associated to ['Player']
    header_lenght = len(header)
    print('_' * header_lenght)
    
    for category in lst_2:
        category_row = category.ljust(45) + '|'

        for player in lst_1:
            score = next((score['Score'] for score in player['Scores'] if score['Category'] == category))
            category_row += str(score).center(15) + '|'

        print(category_row)

        if category in ['Sixes (sum sixes)', 'Yatzy (Five of a Kind)', 'Bonus']:
            print('_' * header_lenght)

    print('_' * header_lenght)


def collect_highscores(participants, filename):

    final_scores = []

    for player in participants:
        player_name = player['Player']
        total_score = player['Scores'][16]['Score']
        now = datetime.now.strftime('%Y-%m-%d %H:%M:%S')
        final_scores.append((total_score, player_name))

    if os.path.exists(filename):
        existing_scores = []
        with open(filename, 'r') as file:
            for line in file:
                score, name, date_time = line.strip().split(' - ')
                existing_scores.append((int(score), name, date_time))

        final_scores.extend(existing_scores)

    final_scores.sort(key=lambda x: x[0], reverse=True)

    with open(filename, 'w') as file:
        for score, name, date_time in final_scores:
            file.write(f'{score} - {name} - {date_time}\n')


def read_leaderboard(filename, top_n):

    if not os.path.exists(filename):
        print('No highscores recorded yet.')
        return

    print(f'{'Rank':<5} {'Score':<10} {'Player':<20} {'Date of the Match':<20}')
    print('=' * 65)

    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i >= top_n:
                break
            print(f'{i + 1:<5} {line.strip.strip()}')


def display_winner(participants):
    highest_score = 0
    winner = ''

    for player in participants:
        player_name = player['Player']
        total_score = player['Scores'][16]['Score']

        if total_score > highest_score:
            highest_score = total_score
            winner = player_name

    print(f'\nAnd the winner is {winner} with a total score of {highest_score}! Congratulations!')