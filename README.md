Simple script to see which cards can be searched by banishing which cards in a deck using the Small World spell card.

# Usage: 
1. run script in terminal (python, requests module required)
2. enter y if you want to search for connecting handtraps between 2 cards of your choice or n if you don't
3. in the latter case, enter path of a deck in .ydk format (extension optional), if it's in the same directory as the script just enter the filename 
4. format of result:
```
card you add 1
    card you banish from hand 1
        card you can banish from deck 1
        card you can banish from deck 2
        card you can banish from deck 3
    card you banish from hand 2
        card you can banish from deck 1
        card you can banish from deck 2

card you add 2
etc...
```
Of course the card you banish from hand and the card you add from deck are interchangeable, so you can either use it to look up what cards you have to banish to search the topmost card, or what cards you can search by banishing the topmost card.