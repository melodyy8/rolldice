# RollDice
### About
RollDice is a fun, text-based dice rolling game coded in Python. Originally coded for CalHacks, I added some more options and increased readability in this version. It features music and interactive gameplay. The goal of the game is to play against the computer, rolling a number of dice (which can be determined by the player) and betting an amount of money (also determined by the player). Whoever rolls the higher total sum wins the money for that round, and the game continues until the player has either earned $1 million, or ran out of money. 

### System Requirements
Rolldice uses playsound, which can be installed by running:
```
pip install playsound
```
If the game does not work due to a playsound MCI error, try uninstalling playsound and then re-installing:
```
pip install playsound==1.2.2
```
