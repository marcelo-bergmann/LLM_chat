

########################################
from gemini import GeminiAI

model_name = "gemini-1.5-flash"
instruction = "\
    você vai ser meu asisntente para escrever textos \
    vamos começar a escrever um texto nas seguintes condições: \
        1. vou escrever em portugues ou em inglês e você vai traduzindo para o ingles e acrescentando ao original \
        2. não crie nada \
        3. a cada interação chat apresente apenas o texto em inglês que estamos produzindo \
        4. vou te pedir para melhorar o texto assim que achar pertinente \
        5. aguarde a nova intrução ou o novo texto \
        6. apresente na sua resposta o texto criado desde o início \
    "
temperature = 0.4
Driven_ai = GeminiAI(model_name=model_name, instruction=instruction, temperature=temperature)

query = "Vamos começar o texto Agora"
resposta = Driven_ai.generate_response(query)
print(resposta.text)

### com generate_response ###
# query = "Inclua no texto: Era uma vez um garoto feliz."
# resposta = Driven_ai.generate_response(query)
# print(resposta.text)

# query = "Ele resolveu andar de motocicleta."
# resposta = Driven_ai.generate_response(query)
# print(resposta.text)

### com send_message ###
# query = "Inclua no texto: Era uma vez um garoto feliz."
# resposta = Driven_ai.send_message(query)
# print(resposta.text)

# query = "Ele resolveu andar de motocicleta."
# resposta = Driven_ai.send_message(query)
# print(resposta.text)

# query = "Escolha um lugar para ele ir e diga onde ele foi."
# resposta = Driven_ai.send_message(query)
# print(resposta.text)

# query = "Modifique o texto pois era um menino triste."
# resposta = Driven_ai.send_message(query)
# print(resposta.text)

# query = "Modifique o texto pois ele foi para Porto Alegre."
# resposta = Driven_ai.send_message(query)
# print(resposta.text)

# query = "Agora seja criativo e invente uma história de 2 paragrafos que ele fez em Porto Alegre envolvendo a moto e uma garota."
# resposta = Driven_ai.send_message(query)
# print(resposta.text)


#history = Driven_ai.get_history()
#print(history)
chat_count = 0
while True:
    query = input("User: ")
    if query == "exit":
        break
    if query == "history":
        history = Driven_ai.get_history()
#        print(history)
        historico = history[-1].parts[-1].text
        arquivo = open("./historico.txt", "w", encoding="utf-8")
        arquivo.write(str(historico))  # Converte a variável para string e escreve no arquivo
        arquivo.close()
        print(historico)
        continue
    if query == "markdown":
        resposta = Driven_ai.send_message("faça markdown neste texto para linhas de 80 caracteres")
        print("Gemini: \n", resposta.text)
        continue
    if query == "list":
        Driven_ai.listar_modelos_gemini()
        continue

    resposta = Driven_ai.send_message(query)
    print("Gemini: \n", resposta.text)

