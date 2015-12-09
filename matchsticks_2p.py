matchsticks = 21

print('Matchstick Game!')
print('There are 21 matchsticks')
print('Each turn you can pick between 1 and 4 matchsticks')
print('The person to pick up the last matchstick loses')
print('')

number_of_players = 0
while number_of_players != 1 and number_of_players != 2:
    number_of_players = int(raw_input('How many players (1 or 2):'))
    if number_of_players != 1 and number_of_players != 2:
        print('Valid choice is either 1 or 2 players')

print('You have chosen %d players' % number_of_players)
print('There are %d matchsticks left' % matchsticks)

which_player = 1
while matchsticks > 0:

    player_choice = int(raw_input('[Player %d] How many matchsticks do you choose (1 - 4):' % which_player))  # probably best to cast and then catch
    if player_choice < 1 or player_choice > 4 or player_choice > matchsticks:
        print('Invalid entry, number must be between 1 and 4 and not exceed the number of matchsticks left!')
        continue


    matchsticks = matchsticks - player_choice

    print('You picked %d matchsticks\nThere are %d matchsticks left\n' % (player_choice, matchsticks))

    if which_player == 1:
        which_player = 2
    else:
        which_player = 1

    if matchsticks == 1:
        print('Only 1 matchstick remains, player %d loses!' % which_player)
        break
