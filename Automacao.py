import pyautogui
from time import sleep

# 1 - Clicar e digitar meu usuário
pyautogui.click(966,541, duration =0.5)
pyautogui.write('matheus')
# 2 - Clicar e digitar minha senha
pyautogui.click(964,575, duration = 0.5)
pyautogui.write('123456')
# 3 - Clicar em "Entrar"
pyautogui.click(851,613, duration = 0.5)
# 4 - Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preço = linha.split(',')[2]
        # 1 - clicar e digitar produtoProduto 1
        pyautogui.click(616,526, duration = 0.5)
        pyautogui.write(produto)
        # 2 - clicar e digitar quantidade
        pyautogui.click(619,559, duration = 0.5)
        pyautogui.write(quantidade)
        # 3 - clicar e digitar preço
        pyautogui.click(621,591, duration = 0.5)
        pyautogui.write(preço)
        # 4 - clicar em registrar
        pyautogui.click(514,784, duration = 1)
        sleep(1)
