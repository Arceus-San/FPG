from tkinter import *
import pygame

def clic(event):
    global rank, L,L2,L3, clicx, clicy
    rank=0
    clicx=event.x
    clicy=event.y
    if(238<=clicx<=300 and 734<=clicy<=792):
        L=accueil
        afficher(L)
    if(118<=clicx<=184 and 734<=clicy<=795):
        L3=L           
        L=L2
        L2=L3
        afficher(L)
    if(L==audiorisitas or L==audio1 or L==audio2):
        son(L)
  
    for i in range(0,len(L[1])):
        if(L[1][i][0]<=clicx<=L[1][i][1] and L[1][i][2]<=clicy<=L[1][i][3]):
            rank=i
            L2=L
            L=L[2][rank]
            afficher(L)

def afficher(L):
	global y
	if(len(L[0])==1):
	    ecran= PhotoImage(file=L[0][0])
	    cadre.create_image(230,400, image=ecran)
	    
	else:
	    ecran= PhotoImage(file=L[0][1])
	    cadre.create_image(230,y, image=ecran)
	    layout= PhotoImage(file=L[0][0])
	    cadre.create_image(230,400, image=layout)
	thehouse.mainloop()

def son(L):
    global playsound, clicx, clicy
    if(93<=clicx<=354 and 184<=clicy<=445 and L==audiorisitas):
        if(playsound==0):
            risitas.play()
            playsound=1
        else:
            risitas.stop()
            playsound=0
    
def scroll(event):
	global y
	print(event.delta)
	decal=event.delta

	if(L==smsaurelie):
		y=y+(decal*40)
		if(y>1050):
			y=1050
			afficher(L)
		else:
			afficher(L)


#Sms: 21,107  / 117,227
#Galerie: 12,114  / 276 ,396
#Audio: 18,114 / 442,565
#Retour: 118,184  /  734,795
#Home : 238,300  /  734,792
#meme: 50,440 / 150,310
#photos: 50,440 / 340,490
#secret: 50,440 / 520,660

accueil=[["mainfinal.gif"],[[13,114,442,565],[12,114,276,396],[21,107,117,227]]]
galerie=[["galeriefinal.gif"],[[50,440,150,310],[50,440,340,390],[20,440,520,660]]]
meme=[["galeriefinal2.gif"],[[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
secret=[["galeriesecret.gif"],[[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
photos=[["galeriephotos.gif"],[[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
audio=[["audiomain.gif"],[[48,433,173,243],[47,448,274,357],[48,409,375,458]]]
audio1=[["audio1.gif"],[[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
audio2=[["audio2.gif"],[[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
audiorisitas=[["audiorisitas.gif"],[[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
sms=[["smsmain.gif"],[[47,439,158,248],[49,425,267,356],[48,438,379,477]]]
smsaurelie=[["layoutsms.gif","smsaurelie.gif"],[[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
smsmaman=[["smsmaman.gif"],[[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
smstimothe=[["smstimothe.gif"],[[0,0,0,0],[0,0,0,0],[0,0,0,0]]]


accueilv=[audio,galerie,sms]
galeriev=[meme,photos,secret]
memev=[]
secretv=[]
photosv=[]
audiov=[audio1,audio2,audiorisitas]
audio1v=[]
audio2v=[]
audiorisitasv=[]
smsv=[smsaurelie,smsmaman,smstimothe]
smsaureliev=[]
smsmamanv=[]
smstimothev=[]

accueil.append(accueilv)
galerie.append(galeriev)
meme.append(memev)
secret.append(secretv)
photos.append(photosv)
audio.append(audiov)
audio1.append(audio1v)
audio2.append(audio2v)
audiorisitas.append(audiorisitasv)
sms.append(smsv)
smsaurelie.append(smsaureliev)
smsmaman.append(smsmamanv)
smstimothe.append(smstimothev)

playsound=0
L=accueil
L2=accueil
L3=[]
y=1050

pygame.mixer.init(44100, -16, 2, 2048)
risitas = pygame.mixer.Sound("risitas.wav")



thehouse = Tk()
thehouse.title('The House') 

cadre = Canvas(thehouse, width =460, height =800)
cadre.pack(side =TOP)

cadre.bind("<Button-1>", clic)
cadre.bind("<MouseWheel>", scroll)

ecran= PhotoImage(file="mainfinal.gif")
cadre.create_image(230,400, image=ecran)
thehouse.mainloop()



thehouse.mainloop()
