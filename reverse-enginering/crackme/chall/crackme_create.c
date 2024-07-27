#include <stdio.h>
#include <string.h>
#include <unistd.h>

void lestcrackme(char *m1, char *m2, char *m3, char *m4, char *m5, char *f1, char *f2, char *f3, char *jj){

    strcpy(m1, "Apakah kamu tau indonesia mempunyai banyak");
    strcpy(m2, "pantai-pantai yang indah?");
    strcpy(m3, "Masukkan flag: ");
    strcpy(m4, "Oopss salah flag!");
    strcpy(m5, "Woww Flag benar!");

    int i;
    char b1[100];
    char b2[100];
    char b3[100];
    char b4[100];
    char b5[100];
    char g1[100];
    char g2[100];
    char g3[100];
    jj[0] = '\0';

    strcpy(f1, "OFPW1317xfu0qz\\`q7`H\\J\\g");
    strcpy(f2, "YtyB1~|sB~o)~vBdrhooBu.|o");
    strcpy(f3, "{{Pmef}}c;gggP?lj9><mnj:r");
    
    for (i = 0; i < strlen(f1); i++){
        f1[i] = f1[i] ^ m1[7] ^ m2[23];
    }
    for (i = 0; i < strlen(f2); i++){
        f2[i] = f2[i] ^ m1[20] ^ m4[6];
    }
    for (i = 0; i < strlen(f3); i++){
        f3[i] = f3[i] ^ m3[12] ^ m4[10];
    }

    strcat(jj, f1);
    strcat(jj, f2);
    strcat(jj, f3);

}

void logolest(){
	puts("");
    puts("██╗     ███████╗███████╗████████╗    ██████╗  ██████╗ ██████╗ ██╗  ██╗");
    puts("██║     ██╔════╝██╔════╝╚══██╔══╝    ╚════██╗██╔═████╗╚════██╗██║  ██║");
    puts("██║     █████╗  ███████╗   ██║        █████╔╝██║██╔██║ █████╔╝███████║");
    puts("██║     ██╔══╝  ╚════██║   ██║       ██╔═══╝ ████╔╝██║██╔═══╝ ╚════██║");
    puts("███████╗███████╗███████║   ██║       ███████╗╚██████╔╝███████╗     ██║");
    puts("╚══════╝╚══════╝╚══════╝   ╚═╝       ╚══════╝ ╚═════╝ ╚══════╝     ╚═╝");
    puts("                          crackme");
    puts("");
}


int main(int argc, char *argv[])
{
    char m1[100];
    char m2[100];
    char m3[100];
    char m4[100];
    char m5[100];
    char f1[100];
    char f2[100];
    char f3[100];
    char jj[300];
    char flag[100];
    logolest();
    lestcrackme(m1, m2, m3, m4, m5, f1, f2, f3, jj);
    printf("%s\n", m1);
    printf("%s\n", m2);
    if (argc > 1 && strcmp(argv[1], "true") == 0){
        printf("%s", m3);
        scanf("%s", flag);
        if (strcmp(flag, jj) == 0){
            printf("%s", m5);
        } else {
            printf("%s", m4);
        }
    } else {
        sleep(4);
        return 0;
    }
    
    return 0;
}