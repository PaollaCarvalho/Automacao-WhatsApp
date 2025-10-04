import pywhatkit as kit
import pyautogui as auto
import pandas as pd
from datetime import datetime
import time

# === LENDO PLANILHA ===
df_final= pd.read_excel(r"clientes.xlsx")

# === FUNÇÃO DE ENVIO DE MENSAGENS ===
# A planilha deve conter colunas: "Nome", "Celular", "Dt. nasc."
def enviar_msg(numero, mensagem):
    """
    Envia mensagem instantaneamente usando PyWhatKit
    Parâmetros:
        numero (str): número do cliente no formato internacional (+55...)
        mensagem (str): texto da mensagem a ser enviada
    """
    try:  
        print(f"Enviando mensagens")

        kit.sendwhatmsg_instantly(numero, mensagem, wait_time= 20, tab_close= True)
        # wait_time = tempo para abrir o WhatsApp Web antes de enviar
        # tab_close = fecha a aba após envio

        time.sleep(2) # Pequena pausa para garantir processamento

        auto.press('enter')
        print(f"Mensagem enviada para {numero}")
    
    except Exception as e: 
        print(f"Erro ao enviar para {numero}: {e}")

if __name__ == '__main__':
    # Criação da lista com os aniversáriantes do dia
    hoje = datetime.today().strftime("%d/%m")
    aniversariantes_hj = df_final[df_final["Dt. nasc."].dt.strftime("%d/%m") == hoje]

    for _, row in aniversariantes_hj.iterrows():
        numero = str(row["Celular"]).strip()
        nome = row["Nome"]
        primeiro_nome = nome.split()[0]
        
        #Mensagem personalizada definida
        mensagem = f"""
        🎉 Feliz Aniversário {primeiro_nome}

        Neste mês especial, nossa equipe deseja a você muita saúde, conquistas e momentos de felicidade. 
        E para tornar seu aniversário ainda mais especial, preparamos um presente exclusivo:

        🎁 Presente.

        Atenciosamente, equipe Empresa X
    """
        # Chama função para enviar a mensagem
        enviar_msg(numero, mensagem)    
        # Pausa de 15 segundos entre mensagens para não sobrecarregar
        time.sleep(15)


