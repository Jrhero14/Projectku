#include <stdio.h>

unsigned int baris, kolom;
int i,j;

typedef struct {
    int vertex;
    int derajat;
}graph;

int main(){
    unsigned int jenis, totalDerajat=0, q=1,r=1;

    FILE * fpointer;

    // PENTING!!!!!!   LOKASI FILE MATRIKS.TXT
    /* "D:\\Project\\BelajarC\\Rute Graf Euler\\matriks.txt" ADALAH ALAMAT FILE DARI PEMBUAT PROGRAM
     * HARAP MENGANTI ALAMAT FILE "matriks.txt"
     * DENGAN ALAMAT FILE "matriks.txt" DI KOMPUTER ANDA YANG SEKARANG
     */
    fpointer = fopen("D:\\Project\\BelajarC\\Rute Graf Euler\\matriks.txt", "r"); // gantinya di sini ya
    if (fpointer == NULL){
        printf("TIDAK DITEMUKKAN FILE matriks.txt!!!\n"
               "Periksa dan ganti alamatnya pada source codenya segera!!!\n");
        return 0;
    }
    char output[150];
    printf("Program analisis Graf Matematika Diskrit\n");
    printf("Masukan banyak vertex:");
    scanf("%d", &baris);
    baris++;
    kolom = baris;
    int arr[baris][kolom];
    int copyArr[baris][kolom];
    graph graf[baris];

    while (!feof(fpointer)){
        fgets(output,150,fpointer);
        for (int k = 0; k < baris; ++k) {
            if (output[k] == '1'){
                arr[q][r] = 1;
            }else{
                arr[q][r] = 0;
            }
            r++;
        }
        graf[q].vertex = q;
        q++; r=1;
    }
    fclose(fpointer);

    printf("MATRIKS\n");
    for (i = 1; i < baris; ++i) { //Menampilkan matriks yg sudah dibuat
        for (j = 1; j < kolom; ++j) {
            printf("%u ", arr[i][j]);
        }
        printf("\n");
    }

    fflush(stdin);
    getchar();


    ///////////////////////////////////////////////////----1
    int hm[20] = {0};
    int T[20] = {0};
    int refleksiGraf[baris][kolom];
    for (int k = 1; k < baris; ++k) {
        for (int l = k; l < kolom; ++l) {
            refleksiGraf[k][l] = arr[k][l];
            refleksiGraf[l][k] = arr[k][l];
        }
    }

    printf("\n");
    printf("Analisis graf terhubung atau tidak?\n");
    printf("Jawabannya:");
    for (int k = 2; k < baris; ++k) {
        hm[k] = refleksiGraf[2][k];
    }
    for (int i = 2;i < baris; ++i) {
        for (int j = 2; j < baris; ++j) {
            if ((hm[j]==1) && (T[j]==0)){
                T[j] = 1;
                for (int k = 2; k < baris; ++k) {
                    if ((refleksiGraf[j][k] == 1) && (hm[k] == 0)){
                        hm[k] = 1;
                    }
                }
            }
        }
    }
    int total = 0;
    for (int k = 2; k < baris; ++k) {
        total += hm[k];
        printf("%d", hm[k]);
    }
    if (total == baris-2){
        printf("\nGraf ini terhubung\n");
        jenis = 1;
    }else{
        printf("\nGraf ini tidak terhubung");
        jenis = 0;
    }
    getchar(); fflush(stdin);
    ////////////////////////////////////////////////////--3
    int count = 0;
    printf("\nMenentukan derajat graf");
    printf("\nJawabannya:\n");
    for (i = 1; i < baris; ++i) {
        printf("Vertex-%d: ", i);
        for (j = 1; j < kolom; ++j) {
            if (arr[i][j] > 0){
                count++;
                totalDerajat++;
            }
        }
        graf[i].derajat = count;
        printf("%d \n", graf[i].derajat);
        count = 0;
    }
    count = 0;
    int parr = 1;
    int stackVer[10] = {0};
    for (int k = 1; k < baris; ++k) {
        if (graf[k].derajat % 2 == 1){
            count++;
            stackVer[parr] = k;
            parr++;
        }
    }

    /////////////////////////////////////////////////////////////////PENYELESAIAN
    printf("\n\n|::::PENCARIAN RUTE EULER::::|\n");
    if (count>2){
        printf("TIDAK DITEMUKAN!!\n");
        printf("KARENA VERTEX BERDERAJAT GANJIL ADA LEBIH DARI DUA VERTEX");
        return 0;
    }else

    for (int k = 1; k < baris; ++k) { // Copy matriks awal
        for (int l = 1; l < kolom; ++l) {
            copyArr[k][l] = arr[k][l];
        }
    }

    int curr = graf[stackVer[1]].derajat;
    int currVer = stackVer[1];
    if (count == 0){ // Vertex semua Genap
        curr = graf[1].derajat;
        currVer = graf[1].vertex;
        for (int k = 2; k < baris; ++k) {
            if (graf[k].derajat > curr){
                curr = graf[k].derajat;
                currVer = graf[k].vertex;
            }
        }
    }else{ // Vertex ada yang ganjil
        for (int k = 2; k < parr; ++k) {
            if (graf[stackVer[k]].derajat > curr){
                curr = graf[stackVer[k]].derajat;
                currVer = stackVer[k];
            }
        }
    }

    parr--;
    int tempuh = totalDerajat/2, n = 1, currVerCp = currVer, arrprev[10] = {0}, y = 1;
    while (tempuh != 0){
        printf("percobaan ke-%d:\n", n);
        printf("%d ", currVer);
        for (int k = 1; k < baris; ++k) {
            for (int l = 1; l < baris; ++l) {
                if (copyArr[currVer][l] == 1 && (arrprev[y] != l)){
                    arrprev[y] = l; y++;
                    printf("%d ", l);
                    copyArr[currVer][l] = 0; copyArr[l][currVer] = 0;
                    currVer = l;
                    tempuh--;
                }
            }
        }
        for (int k = 1; k < baris; ++k) {
            for (int l = 1; l < kolom; ++l) {
                copyArr[k][l] = arr[k][l];
            }
        }
        if (tempuh != 0) {
            n++; y = 1;
            currVer = currVerCp;
            tempuh = totalDerajat/2;
        } else{
            printf("SOLUSI DITEMUKAN!!");
        }
        printf("\n");
    }

    fflush(stdin);
    getchar();

    return 0;
}
