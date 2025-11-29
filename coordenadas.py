import pyautogui
import time

print("TESTE: Descobrir onde clicar para pesquisa...")
print("Em 5 segundos, clique no campo de pesquisa do Google")
time.sleep(5)
x, y = pyautogui.position()
print(f"Coordenadas do campo de pesquisa: X={x}, Y={y}")

print("\nAgora teste a pesquisa manualmente...")



