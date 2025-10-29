from guizero import App, PushButton, Text
import pygame

pygame.mixer.init()
click_sound = pygame.mixer.Sound("click.wav")
upgrade_sound = pygame.mixer.Sound("upgrade.wav")

app= App(title="clicker game", width=700, height=870, bg="black")
score =0 
level = 1
upgrade_cost = 50
def congdiem(amount):
    global score
    score += amount * level
    textscore.value = f"Score = {score}"
    click_sound.play()
def nangcap():
    global level, score, upgrade_cost
    if score >= upgrade_cost:
        score -= upgrade_cost
        level += 1
        upgrade_cost = int(upgrade_cost * 1.21)
        textscore.value = f"Score = {score}"
        textlevel.value = f"Level = {level}"
        textupgrade.value = f"Upgrade Cost = {upgrade_cost}"
        upgrade_sound.play()
    else:
        textupgrade.value = "Not enough score to upgrade!"

textscore = Text(app, text=f"Score = {score}", size= 50, color= "yellow")
textlevel = Text(app, text=f"Level = {level}", size= 30, color= "blue")
textupgrade = Text(app, text=f"Upgrade Cost = {upgrade_cost}", size=20, color="lightgreen")

button = PushButton(app, text="Push", image="don-cute.png", width=500, height=470, command=congdiem, args=[10])
button_level = PushButton(app, text="Level", image="don-plushie.jpg", width=210, height=200, command=nangcap)
app.display()
