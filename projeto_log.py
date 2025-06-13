## Programa que ler os logs de um site e exibe quantas vezes foi acessado no dia, tempo medio resposta, e usuario mais frequente.
## Feito para projeto da disciplina de algoritmos e programação I.
import os

def main ():
    print(f' Total de acessos diarios: {len(dados_retornados)}')
    print(f' Tempo médio de resposta do servidor {round(tempo_medio(dados_retornados,5),2)} milisegundos')
    site= contador_acessos(dados_retornados)
    top10_usuarios=contador_usuario(dados_retornados,10)

def carregar_dados(path):
    dados=[]
    with open (path,"r",encoding="utf-8") as arquivo:
        for linha in arquivo:
            campos=linha.strip().split("\t")
            dados.append(campos)

        return dados

def tempo_medio(base,posicao):
    soma=0
    for milisegundo in base:
        soma +=int(milisegundo[posicao].replace(".",""))
    ##print (soma)
    return (soma)/len(dados_retornados)

def contador_acessos(base):
    contar_acessos={}
    base1=[]
    for lista_interna in base:
        for item in lista_interna:
            posicao_http=item.strip('\"').find("http")
            if posicao_http !=-1:
                base1.append(item[posicao_http:])
    
    for log in base1:    
       ##if "http://" in log or "httss://" in log:
            if log in contar_acessos:
                contar_acessos[log]+=1
            else:
                contar_acessos[log]=1
       
    site_acessado= max(contar_acessos,key=contar_acessos.get)
    print(f' O URL mais acessado foi: {site_acessado} com {max(contar_acessos.values())} acessos.') 

    return site_acessado

def contador_usuario(base,posicao):
    contar_acessos={}
    for log in base:
        dados=log[posicao]
        if "-" not in dados: 
            if dados in contar_acessos:
                contar_acessos[dados]+=1
            else:
                contar_acessos[dados]=1

    usuario_acessos= max(contar_acessos,key=contar_acessos.get) 
    print(f' O usuário mais ativo foi: {usuario_acessos}')
    top10_usuarios=dict(sorted(contar_acessos.items(),key=lambda item:item[1],reverse=True)[0:10])
    print(f' ### Top 10 usuários mais ativos ###')

    i=1
    while i <11:
        for elemento, valor in top10_usuarios.items():
            print(f' Top ({i})- Usuário: {elemento}, fez {valor} requisições')
            i +=1

    return usuario_acessos

print("#############################################################")
print("##################-RELATORIO DE LOG's SITE-##################")
caminho_arquivo="@@@@@@@@@@@@@@@@@"###endereço arquio log no computador
dados_retornados=carregar_dados(caminho_arquivo)

print(f' Relatório referente ao arquivo log no endereço em {(caminho_arquivo)}')
main()
