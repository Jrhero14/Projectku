#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned int baris, kolom, banyakEdge;
int i,j;

typedef struct {
    int vertexBaris;
    int vertexKolom;
    int nilaiBobot;
}bobot;

typedef struct {
    int atasan;
    int bawahan;
}status;

bobot edgeGraf[12] = {0}; // [GANTI] edgeGraf[edge] | edge = banyak edge + 1
status statusVertex[8] = {0}; // [GANTI] statusVertex[vertex] | vertex = banyak vertex + 1

void swap(bobot *xp, bobot *yp)
{
    bobot temp = *xp;
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
            if (edgeGraf[j].nilaiBobot > edgeGraf[j+1].nilaiBobot)
                swap(&edgeGraf[j+1], &edgeGraf[j]);
}

int main(){
    unsigned int q=1,r=1;

    printf("Program analisis Graf Matematika Diskrit\n");
    printf("Masukan banyak vertex:");
    scanf("%d", &baris);

    printf("Masukan banyak edge:");
    scanf("%d", &banyakEdge);
    baris++;
    kolom = baris;
    int arr[baris][kolom];

    FILE * fpointer;
    fpointer = fopen("D:\\Project\\BelajarC\\matriks.txt","r");
    char output[150];
    int   x = 1, y = 1;

    // Operasi File, hilangkan koment di bawah jika ingin menggunakan operasi file
    char *token;
    while (fgets(output, sizeof(output), fpointer)){
        token = strtok(output, " ");
        while (token != NULL){
            printf("%s ", token);
            arr[x][y] = atoi(token);
            token = strtok(NULL, " ");
            y += 1;
        }
        y = 1;
        x += 1;
    }

    // Input bobot secara manual, hilangan komen di bawah jika ingin menggunakan input manual
//    for (i = 1; i < baris; ++i) { //Input matriks
//        for (j = 1; j < kolom; ++j) {
//            printf("Bobot edge vertex %d dengan vertex %d:", i, j); fflush(stdin);
//            scanf("%u", &arr[i][j]);
//        }
//    }

    int iter = 1;
    for (int k = 1; k < baris; ++k) {
        for (int l = k; l < kolom; ++l) {
            if((arr[k][l] > 0) && (arr[k][l] < 99)){
                edgeGraf[iter].vertexBaris = k;
                edgeGraf[iter].vertexKolom = l;
                edgeGraf[iter].nilaiBobot = arr[k][l];
                iter++;
                if (iter == banyakEdge){
                    break;
                }
            }
        }
    }

    printf("\nMATRIKS BOBOT\n");
    for (i = 1; i < baris; ++i) { //Menampilkan matriks yg sudah dibuat
        for (j = 1; j < kolom; ++j) {
            printf("%u ", arr[i][j]);
        }
        printf("\n");
    }

    printf("\nBobot edge sebelum diurutkan:\n");
    for (int k = 1; k < banyakEdge; ++k) {
        printf("[%d][%d] : %d\n", edgeGraf[k].vertexBaris, edgeGraf[k].vertexKolom,edgeGraf[k].nilaiBobot);
    }

    bubbleSort(banyakEdge);

    printf("\nBobot edge setelah diurutkan:\n");
    for (int k = 1; k < banyakEdge; ++k) {
        printf("[%d][%d] : %d\n", edgeGraf[k].vertexBaris, edgeGraf[k].vertexKolom,edgeGraf[k].nilaiBobot);
    }
    /////////////////////////////////////////////////////////////////PENYELESAIAN
    int count = 0;
    int dump;
    int hitungSpanning[6] = {0}; // [GANTI] hitungSpanning[vertex-1]
    printf("\nSOLUSI ALGORITMA KRUSKAL\n");
    printf("\n---- DEBUGGING ---\n");
    for (int k = 1; k < banyakEdge+1; ++k) {
        printf("         1|2|3|4|5|6|7\n"
               "Atasan:  %d|%d|%d|%d|%d|%d|%d\n", statusVertex[1].atasan, statusVertex[2].atasan, statusVertex[3].atasan, statusVertex[4].atasan,
               statusVertex[5].atasan, statusVertex[6].atasan, statusVertex[7].atasan);
        printf("Bawahan: %d|%d|%d|%d|%d|%d|%d\n\n", statusVertex[1].bawahan, statusVertex[2].bawahan, statusVertex[3].bawahan, statusVertex[4].bawahan,
               statusVertex[5].bawahan, statusVertex[6].bawahan, statusVertex[7].bawahan);

        if ((statusVertex[edgeGraf[k].vertexBaris].bawahan == statusVertex[edgeGraf[k].vertexKolom].bawahan)
            && (statusVertex[edgeGraf[k].vertexBaris].bawahan != 0 && statusVertex[edgeGraf[k].vertexKolom].bawahan != 0)){
            continue;
        }
        else if ((statusVertex[edgeGraf[k].vertexBaris].bawahan == edgeGraf[k].vertexKolom) &&
                    statusVertex[edgeGraf[k].vertexBaris].bawahan != 0){
            continue;
        }
        else if ((statusVertex[edgeGraf[k].vertexKolom].bawahan == edgeGraf[k].vertexBaris) &&
                statusVertex[edgeGraf[k].vertexKolom].bawahan != 0){
            continue;
        }
        else if (statusVertex[edgeGraf[k].vertexBaris].atasan == 1 && statusVertex[edgeGraf[k].vertexKolom].atasan == 1){
            statusVertex[edgeGraf[k].vertexKolom].atasan = 0;
            dump = edgeGraf[k].vertexKolom;
            statusVertex[edgeGraf[k].vertexKolom].bawahan = edgeGraf[k].vertexBaris;
            for (int l = 1; l < banyakEdge; ++l) {
                if (statusVertex[l].bawahan == dump && statusVertex[l].atasan != 1){
                    statusVertex[l].bawahan = edgeGraf[k].vertexBaris;
                }
            }
            printf("1 [%d][%d] : %d\n", edgeGraf[k].vertexBaris, edgeGraf[k].vertexKolom, edgeGraf[k].nilaiBobot);
            count += 1;
            hitungSpanning[count] = edgeGraf[k].nilaiBobot;
        }
        else if ((statusVertex[edgeGraf[k].vertexBaris].bawahan != 0 && statusVertex[edgeGraf[k].vertexKolom].bawahan != 0)
                    && (statusVertex[edgeGraf[k].vertexBaris].bawahan != statusVertex[edgeGraf[k].vertexKolom].bawahan))
        {
            statusVertex[statusVertex[edgeGraf[k].vertexKolom].bawahan].atasan = 0;
            statusVertex[statusVertex[edgeGraf[k].vertexKolom].bawahan].bawahan = statusVertex[edgeGraf[k].vertexBaris].bawahan;
            dump = statusVertex[edgeGraf[k].vertexKolom].bawahan;
            statusVertex[edgeGraf[k].vertexKolom].bawahan = statusVertex[edgeGraf[k].vertexBaris].bawahan;
            for (int l = 1; l < banyakEdge; ++l) {
                if (statusVertex[l].bawahan == dump && statusVertex[l].atasan != 1){
                    statusVertex[l].bawahan = statusVertex[edgeGraf[k].vertexBaris].bawahan;
                }
            }
            printf("2 [%d][%d] : %d\n", edgeGraf[k].vertexBaris, edgeGraf[k].vertexKolom, edgeGraf[k].nilaiBobot);
            count += 1;
            hitungSpanning[count] = edgeGraf[k].nilaiBobot;
        }
        else if ((statusVertex[edgeGraf[k].vertexBaris].atasan == 0) && (statusVertex[edgeGraf[k].vertexKolom].atasan == 0) &&
                (statusVertex[edgeGraf[k].vertexBaris].bawahan == 0) && (statusVertex[edgeGraf[k].vertexKolom].bawahan == 0)){
            statusVertex[edgeGraf[k].vertexBaris].atasan = 1;
            statusVertex[edgeGraf[k].vertexKolom].bawahan = edgeGraf[k].vertexBaris;
            printf("3 [%d][%d] : %d\n", edgeGraf[k].vertexBaris, edgeGraf[k].vertexKolom, edgeGraf[k].nilaiBobot);
            count += 1;
            hitungSpanning[count] = edgeGraf[k].nilaiBobot;
        }
        else if (statusVertex[edgeGraf[k].vertexBaris].atasan == 1 && statusVertex[edgeGraf[k].vertexKolom].bawahan == 0 && statusVertex[edgeGraf[k].vertexKolom].atasan == 0){
            statusVertex[edgeGraf[k].vertexKolom].bawahan = edgeGraf[k].vertexBaris;
            printf("4 [%d][%d] : %d\n", edgeGraf[k].vertexBaris, edgeGraf[k].vertexKolom, edgeGraf[k].nilaiBobot);
            count += 1;
            hitungSpanning[count] = edgeGraf[k].nilaiBobot;
        }
        else if (statusVertex[edgeGraf[k].vertexKolom].atasan == 1 && statusVertex[edgeGraf[k].vertexBaris].bawahan == 0 && statusVertex[edgeGraf[k].vertexBaris].atasan == 0){
            statusVertex[edgeGraf[k].vertexBaris].bawahan = edgeGraf[k].vertexKolom;
            printf("5 [%d][%d] : %d\n", edgeGraf[k].vertexBaris, edgeGraf[k].vertexKolom, edgeGraf[k].nilaiBobot);
            count += 1;
            hitungSpanning[count] = edgeGraf[k].nilaiBobot;
        }
        else if (statusVertex[edgeGraf[k].vertexBaris].bawahan != 0 && statusVertex[edgeGraf[k].vertexKolom].bawahan == 0){
            statusVertex[edgeGraf[k].vertexKolom].bawahan = statusVertex[edgeGraf[k].vertexBaris].bawahan;
            printf("6 [%d][%d] : %d\n", edgeGraf[k].vertexBaris, edgeGraf[k].vertexKolom, edgeGraf[k].nilaiBobot);
            count += 1;
            hitungSpanning[count] = edgeGraf[k].nilaiBobot;
        }
        else if (statusVertex[edgeGraf[k].vertexKolom].bawahan != 0 && statusVertex[edgeGraf[k].vertexBaris].bawahan == 0){
            statusVertex[edgeGraf[k].vertexBaris].bawahan = statusVertex[edgeGraf[k].vertexKolom].bawahan;
            printf("7 [%d][%d] : %d\n", edgeGraf[k].vertexBaris, edgeGraf[k].vertexKolom, edgeGraf[k].nilaiBobot);
            count += 1;
            hitungSpanning[count] = edgeGraf[k].nilaiBobot;
        }
        printf("\n");
        if (count == baris-2){
            printf("Selesai\n");
            break;
        }
    }

    printf("\nSOLUSINYA ADALAH\n");
    for (int k = 1; k < baris-1; ++k) {
        printf("%d ", hitungSpanning[k]);
    }

    return 0;
}