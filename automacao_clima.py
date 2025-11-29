import pyautogui
import time

pyautogui.FAILSAFE = True

print("Iniciando automação em 5 segundos...")
time.sleep(5)

try:
   
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.write('chrome')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(4)  
    
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)
    pyautogui.write('https://www.google.com')
    pyautogui.press('enter')
    time.sleep(5) 
    
   
    pyautogui.hotkey('ctrl', 'k')  # pesquisa no Google
    time.sleep(2)
    pyautogui.write('clima hoje')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(6) 
    
   
    pyautogui.scroll(-5)  
    time.sleep(2)
    
    screenshot = pyautogui.screenshot()
    screenshot.save('previsao.png')
    
    print("Print salvo como 'previsao.png'")
    print("A previsão deve estar visível no arquivo!")
    
except Exception as e:
    print(f"Erro: {e}")