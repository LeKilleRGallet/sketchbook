#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int read(int *array, int size)
{
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &array[i]);
    }
}

int* sort(int *array, int array_size){
    int temp;
    for (int i = 0; i < array_size; i++)
    {
        for (int j = 0; j < array_size; j++)
        {
            if (array[i] < array[j])
            {
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
    return array;
}

//union of two arrays without duplicates
int* union_array(int *array1, int *array2, int size1, int size2, int k)
{
    int tpm[size1 + size2];
    k = 0;
    for (int i = 0; i < size1; i++)
    {
        if (i == 0){
            tpm[k++] = array1[i];
        } else {
            for (int j = 0; j < size1; j++)
            {
                if (array1[i] == tpm[j])
                {
                    break;
                } else if (j == i-1)
                {
                    tpm[k++] = array1[i];
                }
            }
        }
    }
    for (int i = 0; i < size2; i++){
            for (int j = 0; j < size2; j++)
            {
                if (array2[i] == tpm[j])
                {
                    break;
                } else if (j == i-1)
                {
                    tpm[k++] = array2[i];
                }
            }
    }
    return tpm;


}







int main(){

    int n, m; //array size

    scanf("%d",&n);

    int a[n];
    read(a, n);

    scanf("%d",&m);
    int b[n];
    read(b, n);
    int k = 0;

    // int exi[2] = union_array(a, b, n, m);
    //get ex from function union_array
    int *tpm = union_array(a, b, n, m, k);


    
    tpm = sort(tpm, k);

    int c[k];
    //copy the tpm array to the c array
    for (int i = 0; i < k; i++)
    {
        c[i] = &tpm[i];
    }

    for (int i = 0; i < k; i++)
    {
        printf("%d ", c[i]);
    }

   return 0;

}