''' # Gravar o dado recebido em arquivo
            print(f'Gravando o arquivo {nome_arquivo} ({tamanho_total} bytes)')
            try:
                nome_arquivo_ = past + nome_arquivo
                arquivo = open(nome_arquivo_, 'wb')
            except:
                print(f'Erro ao salvar o arquivo... {sys.exc_info()[0]}')
            bytes_recebidos = 0
            pct = 1
            while True:
                # Recebendo o conteúdo do servidor
                dado_retorno = client.recv(BUFFER)
                if not dado_retorno: break
                print(f'Pacote ({pct}) - Dados Recebidos: {len(dado_retorno)} bytes')
                arquivo.write(dado_retorno)
                bytes_recebidos += len(dado_retorno)
                if bytes_recebidos >= tamanho_total: break
                pct += 1
    except:
        print(f'Erro ao tentar estabelecer a conexão... {sys.exc_info()[0]}')

        arquivo.close()
except:
    print(f'Erro... {sys.exc_info()[0]}')
# Fechando o socket
client.close()'''