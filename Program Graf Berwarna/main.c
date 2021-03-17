#include <stdio.h>

typedef struct {
    int identy;
    int derajat;
}template;
template arr2[10];

unsigned int baris, kolom;
int i,j;

void swap(template *xp, template *yp)
{
    template temp = *xp;
    *xp = *yp;
    *yp = temp;
}

// A function to implement bubble sort
void bubbleSort(int n)
{
    int i, j;
    for (i = 0; i < n-1; i++)

        // Last i elements are already in place
        for (j = 0; j < n-i-1; j++)
            if (arr2[j].derajat < arr2[j+1].derajat)
                swap(&arr2[j+1], &arr2[j]);
}

int main(){
    unsigned int x;
    printf("Program Implementasi pewarnaan Graf\n");
    printf("Masukkan jumlah vertex:");
    scanf("%u", &baris);
    baris++;
    kolom = baris;
    int arr[baris][kolom];
    int warna[baris];

    for (int k = 1; k <= baris; ++k) { // Mengisi semua nilai element array warna dengan 0
        warna[k] = 0;
    }

    for (i = 1; i < baris; ++i) { //Input matriks
        for (j = 1; j < kolom; ++j) {
            printf("Apakah v%d berhubungan dengan v%d? (1/0):", i, j); fflush(stdout);
            scanf("%u", &arr[i][j]);
        }
    }

    printf("\n");
    for (i = 1; i < baris; ++i) { //Menampilkan matriks yg sudah dibuat
        for (j = 1; j < kolom; ++j) {
            printf("%u ", arr[i][j]);
        }
        printf("\n");
    }

    fflush(stdin);
    getchar();

    int count = 0;
    printf("Menentukan derajat graf");
    printf("\nJawabannya:\n");
    for (i = 1; i < baris; ++i) {
        printf("Vertex-%d: ", i);
        for (j = 1; j < kolom; ++j) {
            if (arr[i][j] > 0){
                count++;
            }
        }
        arr2[i-1].identy = i;
        arr2[i-1].derajat = count;
        printf("%d \n", count);
        count = 0;
    }
    getchar(); fflush(stdin);

    //////////////////////////////////////////////// Alogirtma Welch Powell - BEGIN
    int currentwarna=1, curr;
    bubbleSort(baris-1);
    for (int k = 0; k < baris-1; ++k) {
        curr = arr2[k].identy;
        if (warna[curr] == 0){
            warna[curr] = currentwarna;
            for (int l = 1; l < baris; ++l) {
                if (arr[curr][l] == 0){
                    if (warna[l] == 0){
                        warna[l] = currentwarna;
                    }
                }
            }
            currentwarna++;
        }
    }
    ///////////////////////////////////////////////// Alogirtma Welch Powell - END

    printf("\nWarna Vertex\n");
    for (int k = 1; k < baris; ++k) {
        printf("Vertex/Anjing-%d : %d\n", k, warna[k]);
    }

    printf("\nKandang yang terpakai sejumlah: %d\n", currentwarna-1);
    for (int k = 1; k < currentwarna; ++k) {
        printf("Kandang-%d : ", k);
        for (int l = 0; l < baris; ++l) {
            if (warna[l] == k){
                printf("A%d ", l);
            }
        }
        printf("\n");
    }
    return 0;
}