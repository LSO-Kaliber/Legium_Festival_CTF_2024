# Zero Knowledge

Author : aseng

## Description

Difficulty : Medium

Description : 

A self-proclaimed community just stated themself that they already implemented a very secure admin authentication with **optimized** shared objects library and they want you to audit their code in a black-box method since you're only given their initial access script and binary. Although we know that they are most likely fraud, can you try to login as an administrator?

Additional notes: Developed in `Python 3.11` environment.

## TL;DR

- Custom FNV Hash is used to determine admin password, this can be found from the shared object library at `zkhash` function, with FNV constants but different multiplier.
- Use inverse FNV and brute force possible combinations that satisfy the hash value.
- Chall & WU References -> https://ctf-wiki.mahaloz.re/crypto/hash/fnv/ & ductf.

## Hint 

- References -> https://github.com/cython/cython/releases/tag/3.0.8
- Proof them that they have zero knowledge since their login system is rigged, and you may find "additional" solutions that the password may contain more than just 1 valid combination (iykm ~)

## Flag

Two flags since there are 2 known collisions:

```
LEST2024{bb9ffc75adbf0509cc1ff39eb0dd5272}

LEST2024{c62cb767bb74ab235b1ec3782c326c6d}
```
