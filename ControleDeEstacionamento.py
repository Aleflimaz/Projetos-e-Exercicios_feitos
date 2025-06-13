import math
print("PROGRAMA DE CONTROLE DE ESTACIONAMENTO")

carroP_entrada= 0
carroP_saida= 0
carroP_valor_acumulado= 0
carroG_entrada = 0        
carroG_saida=0
carroG_valor_acumulado=0
moto_entrada = 0
moto_saida = 0
moto_valor_acumulado=0
valorfinal_acumulado=0
tempo_acumulado =0
while(True):
    iniciar=int(input(" Digite [ 1 ] para menu de CADASTRO DE TARIFAS.\n Digite [ 2 ] Para Registros de entrada ou saída \n Digite [3] para Gerar Relatórios\n Digite [4] para encerrar o programa\n "))
    tarifaCarroG = 40
    tarifaCarroG2= 20
    tarifaCarroP =30
    tarifaCarroP2= 15
    tarifaMotos= 30
    tarifaMotos2=15

    if iniciar == 1:
        while(True):
            tarifaopcao=int(input("   CONTROLE DE TARIFAS \n Para cadastrar novas tarifas Digite [ 1 ] \n Para verificar tarifas Digite [ 2 ] \n Para Voltar ao menu inicial Digite [ 3 ] "))
            
            if tarifaopcao == 1:
                tarifaCarroP= float(input("Digite o valor de 3H de permanência em R$ para a TARIFA DE CARROS PEQUENOS: "))
                tarifaCarroP2= float(input("Digite o valor a ser pago por cada hora adicional de permanência em R$ para CARROS PEQUENOS: "))
              
                print("TARIFA DE CARROS PEQUENOS CADASTRADA")

                tarifaCarroG= float(input("Digite o valor em R$ para a TARIFA DE CARROS GRANDES: "))
                tarifaCarroG2= float(input("Digite o valor a ser pago por cada hora adicional de permanência em R$ para CARROS GRANDES: "))
                print("TARIFA DE CARROS GRANDES CADASTRADA")
            

                tarifaMotos= float(input("Digite o valor em R$ para a TARIFA DE MOTOS: "))
                tarifaMotos2= float(input("Digite o valor a ser pago por cada hora adicional de permanência em R$ para MOTOS: "))
             
                print("TARIFA DE MOTOS CADASTRADA")

            elif tarifaopcao == 2:
                print (" TARIFA DE CARROS PEQUENOS: ",tarifaCarroP,"\n TARIFA DE CARROS GRANDES: ",tarifaCarroG,"\n TARIFA DE MOTOS: ", tarifaMotos)
            
            elif tarifaopcao == 3 :
                break

            else:
                print("DIGITE UMA DAS OPÇÕES ")


    if iniciar == 2:
        while(True):
            controle_opcao= int(input(" Digite [1] para registrar ENTRADA de veiculo.\n Digite [2] para registrar SAÍDA de veiculo.\n Digite [3] para voltar ao menu"))
            

            if controle_opcao== 1:
                while (True):

                    placa= int(input(" Digite [1] para voltar ao menu\n Digite a placa do veiculo : \n"))
                    if placa == 1:
                        break

                    tipo_veiculo=int(input(" Para CARRO PEQUENO digite [1].\n Para CARRO GRANDE digite [2].\n Para MOTOS digite [3] \n"))

                    if tipo_veiculo == 1:
                        carroP_entrada = carroP_entrada+1
                        tipo_veiculo="CARRO PEQUENO"
                    elif tipo_veiculo == 2:
                        carroG_entrada= carroG_entrada+1   
                        tipo_veiculo="CARRO GRANDE"
                    elif tipo_veiculo == 3:
                        moto_entrada= moto_entrada+1
                        tipo_veiculo="MOTO"
                    else:
                        print(" DIGITE UMA DAS OPÇÕES ")    
                    
                    data= input(" Digite a data entrada do veiculo ")
                    hora= input(" Digite a hora de entrada do veiculo ")
                    print("*********************RECIBO*********************")
                    print("TIPO DE VEICULO: ",tipo_veiculo,"DATA: ",data)
                    print("Placa:",placa,"HORA DE ENTRADA: ",hora)
                    
            elif controle_opcao== 3:
                break                                                       
            elif controle_opcao == 2:                
                while(True):
                    print("\n REGISTRAR SAÍDA DE VEICULO")
                    tipo_veiculo_saida= int(input(" Para CARRO PEQUENO digite [1].\n Para CARRO GRANDE digite [2].\n Para MOTOS digite [3] \n Para voltar ao menu anterior digite [4]"))
                    
                    tipo_veiculo= tipo_veiculo_saida

                    if tipo_veiculo == 1:
                        carroP_saida += 1
                        tipo_veiculo="CARRO PEQUENO"
                        
                    elif tipo_veiculo == 2:
                        carroG_saida += 1
                        tipo_veiculo="CARRO GRANDE"

                    elif tipo_veiculo == 3:
                        moto_saida += 1
                        tipo_veiculo="MOTO"

                    elif tipo_veiculo_saida == 4:
                        break

                    else:
                        print(" DIGITE UMA DAS OPÇÕES ")
                        continue
                    ###@@@@dias_total=input(" Digite a quantidade de dias que ele permaneceu ")
                    hora_entrada, minutos_entrada= input(" Digite a hora de ENTRADA do veiculo formato hh:mm ").split(':')
                    hora_saida, minutos_saida= input(" Digite a hora de SAÍDA do veiculo formato hh:mm ").split(':')

                    conv=int(hora_entrada)
                    convv=int(minutos_entrada)

                    conv1= int(hora_saida)
                    convv1=int(minutos_saida)

                    horafinalentrada= conv+(convv/60)

                    horafinalsaida= conv1+(convv1/60)

                    if horafinalsaida < horafinalentrada:
                        horafinalsaida += 24

                        ####@@@@horafinalsaida *=(dias_total+1)
                        ###@@@@Se precisar opção dias^^
                    horafinal = horafinalsaida - horafinalentrada
                    valorfinal2=0
                    
                    ###@Como no exercicio pede registrar o valor referente a 3H e depois o Hora/adicional
                    ###@assumi que seria o valor minimo que um carro poderia pagar
                    ###@então mesmo não ficando as 3H completas seria pago o valor completo.

                    if tipo_veiculo_saida ==1:
                        tarifa_final = tarifaCarroP
                        ###@valorfinal= horafinal* tarifa_final
                    elif tipo_veiculo_saida ==2:
                        tarifa_final = tarifaCarroG
                        ###@valorfinal = horafinal*tarifa_final
                    elif tipo_veiculo_saida ==3:
                        tarifa_final = tarifaMotos
                        ###@valorfinal = horafinal* tarifa_final

                    if horafinal > 3:
                        horafinal0= horafinal - 3

                        ###@@Se será cobrado a hora inteira independente dos minutos 
                        ###@@aplica-se o math.ceil para arredondar para cima.

                        ###@@horafinal0 = math.ceil(horafinal0)
        
                        if tipo_veiculo_saida ==1:
                            tarifa_final2= tarifaCarroP2                                                                               
                            valorfinal2= horafinal0 * tarifaCarroP2

                        elif tipo_veiculo_saida ==2:
                            tarifa_final2= tarifaCarroG2
                            valorfinal2 = horafinal0 * tarifaCarroG2
                            
                        elif tipo_veiculo_saida ==3:
                            tarifa_final2= tarifaMotos2
                            valorfinal2 = horafinal0 * tarifaMotos2

                    ###@valorfinal0= valorfinal + valorfinal2   
                    valorfinal0= tarifa_final + valorfinal2

                    opcao_pix=int(input(' Cliente vai pagar com pix? (5% deesconto)\n Digite [1] para Sim \n Digite [0] para Não'))
                    if opcao_pix==1:
                        desconto_pix = valorfinal0 * 0.05
                        valorfinal0 -= desconto_pix
                        tarifa_final -= desconto_pix
                    else:
                        print(" Digite a opção correta !")
                    if horafinal <= 3:
                        valorfinal0= tarifa_final
                        print("******************RECIBO******************")
                        print("Valor a ser pago: ",tarifa_final)
                        print("Valor referente as 3Horas minimas: ",tarifa_final,"Veiculo: ",tipo_veiculo)
                        if opcao_pix==1:
                            print("Desconto pelo pix = {:.2f} Horas,".format(desconto_pix))
                        print("Voce permaneceu por","{:.2f} Horas,".format(horafinal),"( {:.0f} Minutos)".format(horafinal*60))
                       

                    else:
                        print("******************RECIBO******************")
                        print("Valor a ser pago: ","{:.2f} R$".format(valorfinal0))
                        if opcao_pix==1:
                            print("Desconto pelo pix = {:.2f} Horas,".format(desconto_pix))
                        print("Valor referente as 3Horas: ",tarifa_final," R$"," (Hora adicional: {:.2f} R$)".format(tarifa_final2)) 
                        print("Voce permaneceu por","{:.2f}".format(horafinal0*60),"Minutos adicionais")
                        print("Valor referente ao tempo adicional: ","{:.2f} R$".format(valorfinal2))
                        print("TOTAL de: ","{:.2f} Horas,".format(horafinal),"({:.0f} Minutos)".format(horafinal*60))                        
                    valorfinal_acumulado = valorfinal_acumulado + valorfinal0
                    tempo_acumulado += horafinal
                    if tipo_veiculo_saida == 1:
                        carroP_valor_acumulado += valorfinal0
                    elif tipo_veiculo_saida == 2:
                        carroG_valor_acumulado += valorfinal0
                    elif tipo_veiculo_saida == 3:
                        moto_valor_acumulado += valorfinal0
                    
    elif iniciar == 3:  
        opcao_relatorio= int(input("Digite qual tipo de relatório deseja:\n Digite [1] para Gerar Relatório diário\n Digite [2] para Gerar Relatório por tipo de veículo\n "))
        if opcao_relatorio == 1:
            print("*************RELATÓRIO DIÁRIO*************")
            print("Recebemos",(carroP_entrada + carroG_entrada + moto_entrada),"veículos")
            print("Tempo médio de permanencia: ",(tempo_acumulado/(carroP_entrada + carroG_entrada + moto_entrada)))
            print("Hoje foi arrecadado: ","{:.2f} R$".format(valorfinal_acumulado))
        elif opcao_relatorio == 2:
            print("*************RELATÓRIO POR TIPO DE VEÍCULO*************")
            print("Carros Pequenos: ",(carroP_entrada+carroP_saida)," Valor gasto em média: ","{:.2f} R$".format(carroP_valor_acumulado))
            print("Carros Grandes: ",(carroG_entrada+carroG_saida)," Valor gasto em média: ","{:.2f} R$".format(carroG_valor_acumulado))
            print("Motos: ",(moto_entrada+moto_saida)," Valor gasto em média: ","{:.2f} R$".format(moto_valor_acumulado))
        else:
            print("DIGITE UMA DAS OPÇÕES ")
    elif iniciar ==4:
        break
    else:
        print("DIGITE UMA DAS OPÇÕES ")
        

