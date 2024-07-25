#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>

#define KEY_LENGTH 16
#define ROUNDS 1337

void initialize_seed(int seed) {
    srand(seed);
}

int deterministic_number(int i) {
    return (i * i + 33 * i + 1337 + i); 
}

void generate_deterministic_integers(int *buffer, size_t length, int initial_value) {
    for (size_t i = 0; i < length; i++) {
        buffer[i] = deterministic_number(initial_value + i);
    }
}

void hash_function(const int *input, size_t length, int *output) {
    for (size_t i = 0; i < length; i++) {
        output[i] = input[i] ^ 0x2A;
    }
}

void xor_arrays(const int *array1, const int *array2, int *output, size_t length) {
    for (size_t i = 0; i < length; i++) {
        output[i] = array1[i] ^ array2[i];
    }
}

void transform_integers(int *buffer, size_t length) {
    for (size_t i = 0; i < length; i++) {
        buffer[i] = (buffer[i] * 3 + 7);
    }
}

void permute_integers(int *buffer, size_t length) {
    for (size_t i = 0; i < length; i++) {
        size_t j = deterministic_number(i) % length;
        int temp = buffer[i];
        buffer[i] = buffer[j];
        buffer[j] = temp;
    }
}

void mix_integers(const int *array1, const int *array2, int *output, size_t length) {
    for (size_t i = 0; i < length; i++) {
        output[i] = (array1[i] + array2[i]);
    }
}

void derive_key_part1(const int *input, int *output) {
    int temp[KEY_LENGTH];
    hash_function(input, KEY_LENGTH, temp);
    transform_integers(temp, KEY_LENGTH);
    memcpy(output, temp, KEY_LENGTH * sizeof(int));
}

void derive_key_part2(const int *input, int *output) {
    int temp[KEY_LENGTH];
    hash_function(input, KEY_LENGTH, temp);
    permute_integers(temp, KEY_LENGTH);
    memcpy(output, temp, KEY_LENGTH * sizeof(int));
}

void derive_key_part3(const int *input, int *output) {
    int temp[KEY_LENGTH];
    hash_function(input, KEY_LENGTH, temp);
    mix_integers(input, temp, output, KEY_LENGTH);
}

void combine_key_parts(const int *part1, const int *part2, const int *part3, int *key) {
    int temp1[KEY_LENGTH];
    int temp2[KEY_LENGTH];
    xor_arrays(part1, part2, temp1, KEY_LENGTH);
    xor_arrays(temp1, part3, temp2, KEY_LENGTH);
    memcpy(key, temp2, KEY_LENGTH * sizeof(int));
}

void finalize_key(int *key, size_t length) {
    transform_integers(key, length);
    permute_integers(key, length);
}

void print_key(const int *key, size_t length) {
    printf("Generated Key: ");
    for (size_t i = 0; i < length; i++) {
        printf("%d ", key[i]);
    }
    printf("\n");
}

void generate_encryption_key(int *key, int initial_value) {
    int deterministic_integers[KEY_LENGTH];
    int part1[KEY_LENGTH];
    int part2[KEY_LENGTH];
    int part3[KEY_LENGTH];

    generate_deterministic_integers(deterministic_integers, KEY_LENGTH, initial_value);

    derive_key_part1(deterministic_integers, part1);
    derive_key_part2(deterministic_integers, part2);
    derive_key_part3(deterministic_integers, part3);

    combine_key_parts(part1, part2, part3, key);
    finalize_key(key, KEY_LENGTH);
}

void key_expansion(int *initial_key, int round_keys[ROUNDS][KEY_LENGTH]) {
    for (int i = 0; i < ROUNDS; i++) {
        for (int j = 0; j < KEY_LENGTH; j++) {
            round_keys[i][j] = (initial_key[j] + 7 * i);
        }
    }
}

void reverse_transform_bytes(unsigned char *buffer, size_t length, unsigned char *key, size_t key_length) {
    for (size_t i = 0; i < length; i++) {
        unsigned char temp = (buffer[i] - key[i % key_length]);
        buffer[i] = ((temp >> 3) | (temp << 5));
    }
}

void reverse_permute_bytes(unsigned char *buffer, size_t length) {
    unsigned char temp[length];
    for (size_t i = 0; i < length; i++) {
        temp[(i * 7) % length] = buffer[i];
    }
    memcpy(buffer, temp, length);
}

void reverse_obscure_function(unsigned char *buffer, size_t length) {
    for (size_t i = 0; i < length; i++) {
        buffer[i] = ~buffer[i];
    }
}

void xor_with_key(unsigned char *buffer, size_t length, int *key) {
    for (size_t i = 0; i < length; i++) {
        buffer[i] ^= key[i % KEY_LENGTH];
    }
}

void custom_decrypt(unsigned char *ciphertext, size_t length, int initial_key[KEY_LENGTH], unsigned char *plaintext) {
    int round_keys[ROUNDS][KEY_LENGTH];
    key_expansion(initial_key, round_keys);

    memcpy(plaintext, ciphertext, length);

    for (int round = ROUNDS - 1; round >= 0; round--) {
        reverse_obscure_function(plaintext, length);
        xor_with_key(plaintext, length, round_keys[round]);
        reverse_permute_bytes(plaintext, length);
        reverse_transform_bytes(plaintext, length, (unsigned char *)round_keys[round], KEY_LENGTH);
    }
}

int main() {
    int key[KEY_LENGTH];
    int initial_value = 1337;
    generate_encryption_key(key, initial_value);
    print_key(key, KEY_LENGTH);

    unsigned char ciphertext[] = {243, 36, 117, 88, 109, 57, 143, 180, 178, 75, 121, 55, 98, 213, 216, 226, 114, 166, 206, 206, 75, 202, 107, 40, 197, 11, 219, 169, 165, 41, 69, 137, 143, 244, 245, 15, 21, 192, 66, 170};
    size_t length = sizeof(ciphertext) / sizeof(ciphertext[0]);
    unsigned char decrypted[length + 1];

    custom_decrypt(ciphertext, length, key, decrypted);
    decrypted[length] = '\0'; 
    printf("Decrypted  : ");
    for (int i = 0; i < length; i++) {
        printf("%d ", decrypted[i]);
    }
    puts("");
    printf("Decrypted  : %s\n", decrypted);

    return 0;
}

