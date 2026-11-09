Web VPython 3.2



label(pos=vec(0, 3, 0), text='N형 반도체 시뮬레이터', color= color.white)


wafer = []


for x in range(-2, 3, 2):
    for y in range(-2, 3, 2):
        if x==0 and y==0 :
            a = sphere(texture = "https://i.postimg.cc/kMhqZ4V6/p.png&quot;, pos = vec(x,y,0), radius = 0.4, color=vec(0.2,1,0), axis=vec(0,1,-2.5))
           
        else :
            a = sphere(texture = "https://i.postimg.cc/wMYYkt4T/si.png&quot;, pos = vec(x,y,0), radius = 0.4, color=vec(0.5,0.5,0.5), axis=vec(-1,1,-2.5))
            wafer.append(a)
           
           
import random
e = sphere(pos=vector(0.5, 0.5, 0), radius=0.15, color=color.yellow, make_trail=True, retain=13)
l = label( pos=e.pos, text="자유전자", color=color.black, background=color.white, opacity=1.0, height=10,border=3, box=True)



while True :
    rate(1000)
    l.pos = e.pos
    k=keysdown()
    if ' ' in k:
        e.pos.x = random.uniform(-2.5,2.5)
        e.pos.y = random.uniform(-2.5,2.5)
        e.trail_color= vec(1,1,0.7)
       
    for s in wafer :
        if mag(s.pos - e.pos) < 0.7 :
            s.color = color.red
        else :
            s.color = vec(0.5,0.5,0.5)
