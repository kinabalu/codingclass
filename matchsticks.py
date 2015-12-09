matchsticks = 21

print('Matchstick Game!')
print('There are 21 matchsticks')
print('Each turn you can pick between 1 and 4 matchsticks')
print('The person to pick up the last matchstick loses')
print('')

while matchsticks > 0:

    player_choice = int(raw_input('How many matchsticks do you choose (1 - 4):'))  # probably best to cast and then catch
    if player_choice < 1 or player_choice > 4 or player_choice > matchsticks:
        print('Invalid entry, number must be between 1 and 4 and not exceed the number of matchsticks left!')
        continue

    computer_choice = 5 - player_choice
    matchsticks = matchsticks - 5

    print('You picked %d matchsticks\n\nI will pick %d matchsticks, there are %d matchsticks left\n' % (player_choice, computer_choice, matchsticks))

    if matchsticks == 1:
        print('Only 1 matchstick remains, you lose!')
        break

print('You lost, re-run to try again')
