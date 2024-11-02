from pyfiglet import Figlet

figlets = Figlet()

userInput = input("Enter your text : ")

print(userInput)

font = figlets.getFonts()

print(figlets.renderText(userInput))