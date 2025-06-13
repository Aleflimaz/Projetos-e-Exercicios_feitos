#include <stdio.h>
#include <openssl/sha.h>
#include <string.h>
#include <openssl/bio.h>
#include <openssl/evp.h>
#include <openssl/buffer.h>
#include <stdint.h>
#include <stdlib.h>

#define TAM_PALAVRAS 12
#define QTD_PALAVRAS 24
#define MAX_COMBI 5
#define TAM_HASH 400
#define TAM_COMBI 400
#define QTD_USUARIOS 22
#define TAM_NOMES 100

void carrega_palavras_arquivo(int quantidade, int tamanho, char matriz[quantidade][tamanho], 
                              char *caminho, char *tipo, int modo) {  
    
    FILE *arquivo = fopen(caminho, tipo);
    if (arquivo == NULL) {
        perror("Não foi possível abrir o arquivo");
        exit(EXIT_FAILURE);
    }
    if (modo==1||modo==2){
        for (int i = 0; i < quantidade; i++) {
            if (fgets(matriz[i], tamanho, arquivo) != NULL) {//para os hash e nomes dos usuarios.
                matriz[i][strcspn(matriz[i], "\n")] = '\0'; // remove o '\n'
                //caso 1 para os nomes antes do ':'
                if (modo == 1) { 
                    // carrega nomes (antes do ':' )
                    char *token = strtok(matriz[i], ":");
                    if (token != NULL) {
                        strcpy(matriz[i], token); //salva o nome na matriz
                        
                    }
                //caso 2 para hash depois do ':'
                } 
                else if (modo == 2) { 
                    //carrega hashes (appos o ':')
                    char *token = strtok(matriz[i], ":");
                    if (token != NULL) {
                        token = strtok(NULL, ":"); // pega o prox. token/divisao (apos ':')
                        if (token != NULL) {
                            strcpy(matriz[i], token); // slva o hash na matriz

                        }
                    }
                }
                //printf("%s\n", matriz[i]);
            }
        }
    }//leitura normal em ==0 para palavras chaves do arquivo
    if (strcmp(tipo, "r")== 0&&modo ==0) {
        for (int i = 0; i < quantidade; i++) {
            if (fgets(matriz[i], tamanho, arquivo) != NULL) {//pegar cada linha no arquivo para matriz
                matriz[i][strcspn(matriz[i], "\n")] = '\0'; // remove o '\n'
                printf("%s\n",matriz[i]);
                
            }
        }
    }
    
    fclose(arquivo);
}

int Base64Encode(const unsigned char* buffer, size_t length, char** b64text) { 
    BIO *bio, *b64;
    BUF_MEM *bufferPtr;

    b64 = BIO_new(BIO_f_base64());
    bio = BIO_new(BIO_s_mem());
    bio = BIO_push(b64, bio);

    BIO_set_flags(bio, BIO_FLAGS_BASE64_NO_NL); 
    BIO_write(bio, buffer, length);
    BIO_flush(bio);
    BIO_get_mem_ptr(bio, &bufferPtr);
    BIO_set_close(bio, BIO_NOCLOSE);
    BIO_free_all(bio);

    *b64text = (*bufferPtr).data;
    return 0; 
}

void codeSha(char* str, char* hashGerado) {
    SHA512_CTX ctx;
    unsigned char buffer[SHA512_DIGEST_LENGTH];
    int len = strlen(str);
    FILE *arquivo = fopen("combinacoes-hash6.txt", "a");//arquivo de hash
    if (arquivo == NULL) {
        perror("Erro ao abrir o arquivo para escrita");
        return ;
    }
    SHA512_Init(&ctx);
    SHA512_Update(&ctx, str, len);
    SHA512_Final(buffer, &ctx);

    char *base64encoded;
    Base64Encode(buffer, SHA512_DIGEST_LENGTH, &base64encoded);
    strcpy(hashGerado, base64encoded); // Copia o hash gerado
    //printf("%s ###  %s\n",hashGerado,str);
    //fprintf(arquivo, "%s\n", hashGerado); // armazena no arquivo
    fclose(arquivo);
}

void verificaHash(char *hashGerado, char matriz_usuarios_hash[QTD_USUARIOS][TAM_HASH], char *combinacao,char usuarios_nomes[QTD_USUARIOS][TAM_NOMES]) {
    for (int i = 0; i < QTD_USUARIOS; i++) {
               
        if (strcmp(hashGerado, matriz_usuarios_hash[i]) == 0) {
            //abre arquivo se comparação for igual 0
            FILE *arquivo = fopen("usuarios-encontrados.txt", "a");
                if (arquivo == NULL) {
                    perror("Erro ao abrir o arquivo para escrita");
                    return ;
                }

            printf("Usuário: %s >Senha encontrada: %s (Hash: %s)\n", usuarios_nomes[i],combinacao, hashGerado);
            fprintf(arquivo, "%s : HASH:%s  PALAVRAS:%s \n", usuarios_nomes[i],hashGerado,combinacao);//joga no arquivo hash, combinação e usuario
            fclose(arquivo);
        }
    }
}

void gerarArranjos(char palavras[][TAM_PALAVRAS], char *combinacaoAtual, 
                int n, int k, int profundidade, char matriz_usuarios_hash[QTD_USUARIOS][TAM_HASH],char usuarios_nomes[QTD_USUARIOS][TAM_NOMES]) {
    //printf("Teste de combinação: %s\n", combinacaoAtual);
    //printf("Gerando hash...\n");

    FILE *arquivo = fopen("combinacoes-hash5.txt", "a");//arquivo de combinacoes
    if (arquivo == NULL) {
        perror("Erro ao abrir o arquivo para escrita");
        return ;
    }
    if (profundidade == k) {//apos completar  o nivel faz a verificaçao
        char hashGerado[TAM_HASH];
        codeSha(combinacaoAtual, hashGerado);
        verificaHash(hashGerado, matriz_usuarios_hash, combinacaoAtual,usuarios_nomes);
        //fprintf(arquivo, "%s\n", combinacaoAtual);
        fclose(arquivo);
        return;
        
    }

    for (int i = 0; i < n; i++) {//rodar as 24 palavras(QTD)
        char novaCombinacao[TAM_COMBI];
        strcpy(novaCombinacao, combinacaoAtual);//copia a combinacao atual na nova combinacao

        if (strlen(combinacaoAtual) > 0) {
            strcat(novaCombinacao, " ");// adiciona espaço no final da palavra atual
        }
        strcat(novaCombinacao, palavras[i]);//cola a palavra nova
        //chamada recursiva para adicionar mais uma palavra
        gerarArranjos(palavras, novaCombinacao, n, k, profundidade + 1, matriz_usuarios_hash,usuarios_nomes);
    }
    
}

int main() {
    char caminhoPalavras[] = "palavras.txt";
    char caminhoUsuarios[] = "usuarios_senhascodificadas.txt";

    char matriz_palavras_chave[QTD_PALAVRAS][TAM_PALAVRAS];
    char matriz_usuarios_hash[QTD_USUARIOS][TAM_HASH];
    char matriz_usuarios_nomes[QTD_USUARIOS][TAM_NOMES];

    //Carregar palavras e hashes dos arquivos
    carrega_palavras_arquivo(QTD_PALAVRAS, TAM_PALAVRAS, matriz_palavras_chave, caminhoPalavras, "r",0);
    carrega_palavras_arquivo(QTD_USUARIOS, TAM_HASH, matriz_usuarios_hash, caminhoUsuarios, "r",2);
    char caminhoUsuario2[] = "usuarios_senhascodificadas1.txt";
    carrega_palavras_arquivo(QTD_USUARIOS, TAM_NOMES, matriz_usuarios_nomes, caminhoUsuario2, "r",1);
    printf("\nNomes:\n");
    for (int i = 0; i < QTD_USUARIOS; i++) {
        printf("Usuário %d: %s\n", i + 1, matriz_usuarios_nomes[i]);
    }

    for (int i = 0; i < QTD_USUARIOS; i++) {
        printf("Hash %d carregado: '%s'\n", i + 1, matriz_usuarios_hash[i]);
    }

    // gerar de combinações e verificação de hashes
    int n = QTD_PALAVRAS;
    
    #pragma omp parallel for 
    for (int k = 1; k <= MAX_COMBI; k++) {//nivel de combinaçao até max combi 5
        char combinacaoAtual[TAM_COMBI] = "";
        gerarArranjos(matriz_palavras_chave, combinacaoAtual, n, k, 0, matriz_usuarios_hash,matriz_usuarios_nomes);
    }
    
    return 0;
}
//gcc -o main2.out TESTE1.c -lssl -lcrypto
//limpar residuos/espaços arquivo sed -i 's/[ \t\r]*$//' usuarios_senhascodificadas.txt cat -A usuarios_senhascodificadas1.txt
