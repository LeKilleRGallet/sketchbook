#include <stdio.h>


int sum(int& a, int& b) {

    a = a+1;
    b = b+1;
    return a + b;
}

int main(){
    int i;
    int n;
    printf("n: ");
    scanf("%d", &n);
    printf("\ni: ");
    scanf("%d", &i);
    int sumx = sum(n, i);
    printf("n: %d\ni: %d\nsum: %d", n, i, sumx);

    return 0;
}