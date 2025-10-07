def rodar_estagio_deposito(jogo):
        integracao.clear_screen()
        
        print("Rodadas iniciais finalizados. Saldo acumulado convertido em saldo de jogo!")
        print("Deposite para continuar jogando.")
        try:
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            if valor_deposito > 0:
                jogo.saldo += valor_deposito
                print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
            else:
                    print("O valor do depósito deve ser positivo.")
        except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        time.sleep(2)
            
        jogadas = [1, 0, 1, 1, 0]
        porcentagens = [8, 40, 5, 3, 35]
        rodada(jogo, jogadas, porcentagens)    

        print("\n🏁 Estágio 2 Concluído!")
        time.sleep(2)
        
        jogo.estagio = "principal"
