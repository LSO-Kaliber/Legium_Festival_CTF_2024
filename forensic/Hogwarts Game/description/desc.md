# Hogwarts Game
## Description

Author : p0t4rr

Difficulty : medium

Potar, a young investigator with a keen eye for detail, stumbles upon an old, mysterious mansion rumored to hold secrets of great value. As he explores deeper, he encounters multiple levels of challenges that test his forensic skills.

Level 1: The Broken Door

Potar discovers the mansion's front door is damaged and needs repair to gain entry. He must find the tools and materials scattered around the garden to fix the door and enter the house.

Level 2: The Hidden Room Behind the Paintings

Upon entering, Potar finds himself surrounded by a lot of paintings. Some looking almost identical to the other
Among them, he notices a peculiar painting of a HILL. Examining it closely, Potar discovers a hidden lever that reveals a secret room behind the painting.

Level 3: Hidden History

Inside the secret room, Potar is surprised to find the walls are entirely covered in white. He then felt intrigued, "Why is this room all white and spotless?", said him. He couldn't help but to think that there is something here that has been hidden from him. Luckily, he remembered that he has his wand with him. Perhaps there is a spell to undo what might have happened? 

## TL;DR

- Given a corrupted file h4rry.png. Repair the header and IHDR section to reveal flag part 1.
- Use binwalk -e h4rry.png to extract flag.png.
- Run exiftool flag.png to find flag part 2, which is encrypted using the Beaufort cipher with the key HILL.
- Extract flag.png with binwalk -e flag.png to get haHahaHa.log.
- Inside haHahaHa.log, you will find a Google Docs sharing link.
- Flag part 3 is obtained by taking the first letter of each line in the document, arranging them

## Hint

- https://sites.google.com/site/cryptocrackprogram/user-guide/cipher-types/substitution/variant-beaufort

## Flag

LEST2024{b4ng_h4rrY_b3lajar_cTf_b3eRs4maa}
