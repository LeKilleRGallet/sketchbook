#include <stdio.h>


int read(int *array, int size)
{
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &array[i]);
    }
}

int duplicates(int *original_array, int *tpm_array, int array_size)
{
    int counter = 0;
    for (int i = 0; i < array_size; i++)
    {
        if(i == 0){
            tpm_array[i] = original_array[i];
        }
        else{
            for (int j = 0; j < i; j++)
            {
                if(original_array[i] == tpm_array[j]){
                    counter++;
                    break;
                }
                else if(j == i-1){
                    tpm_array[i-counter] = original_array[i];
                }
            }
        }
    }
    return array_size-counter;

}

int arraysize(int *array, int array_size){
    int new_size = 0;
    for (int i = 0; i < array_size; i++)
    {
        if (array[i] != 0)
        {
            new_size++;
        }
    }
    return new_size;
}

int arrayprint(int *array, int array_size){
    for (int i = 0; i < array_size; i++)
    {
        printf("%d\t", array[i]);
    }
}

int main(){

    int n;
    scanf("%d",&n);

    //initialize a array with size n
    int a[n];
    //scan n values for the array
    read(&a, n);

    int tmp[n];

    int size = duplicates(&a, &tmp, n);

    int b[size];
    for (int i = 0; i < size; i++)
    {
        b[i] = tmp[i];
    }


    arrayprint(&b, size);


    return 0;
}