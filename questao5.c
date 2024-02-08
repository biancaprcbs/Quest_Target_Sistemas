#include <stdio.h>
#include <string.h>

void inverterString(char string[]) {
    int comprimento = strlen(string);
    int esquerda = 0;
    int direita = comprimento - 1;
    
    while (esquerda < direita) {
        char temp = string[esquerda];
        string[esquerda] = string[direita];
        string[direita] = temp;
        
        esquerda++;
        direita--;
    }
}

int main() {
    char string[100];
    
    printf("Digite uma string para inverter: ");
    scanf("%s", string);

    inverterString(string);
    
    printf("String invertida: %s\n", string);

    return 0;
}

