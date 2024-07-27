# Zero Driver

Author : aseng

## Description

Difficulty : Easy

Description : 

Given a x64 executable to validate a single file but I don't think this problem setter has a lot of effort. However why am I seeing a bunch of Windows Driver Kit API in here? 

## TL;DR

- Obfuscation on WinAPI Arbitrary Calls.
- Realized that it's only loading a `.rsrc` buffer.
- Flag is located and extracted from resources and compared, so just export all the buffer and saves it as a file.
- The file is a Ms Docx file , flag is in there!

## Hint 

- Don't get fooled by the drivers API since there aren't any involved!
- Placing at certain breakpoint will help!

## Flag

```
LEST2024{wind0ws_4p1_i5_We1Rd}
```
