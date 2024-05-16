from vpython import sphere, vector, color, rate, slider, wtext, scene


ball = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.red)

def set_speed(slider):
    speed_text.text = f'速度: {slider.value:.2f}'

speed_text = wtext(text='速度: 1')
speed_slider = slider(min=0, max=10, value=1, length=200, right=15,bind=set_speed)

def set_size(slider):
    size_text.text = f"大小: {slider.value:.2f}"
size_text = wtext(text='大小: 0.5')
size_slider = slider(min=0, max=1, value=1,length=200, right=15, bind=set_size)

def set_color(slider):
    if slider.value>=0 and slider.value<=0.2:
        ball.color = color.red
        colors = "red"
    elif slider.value>0.2 and slider.value<=0.3:
        ball.color = color.green
        colors = "green"
    elif slider.value>0.3 and slider.value<=0.4:
        ball.color = color.blue
        colors = "blue"
    elif slider.value>0.4 and slider.value<=0.5:
        ball.color = color.purple
        colors = "purple"
    else:
        colors = "orange"
        ball.color = color.orange    
    color_text.text = f"顏色:{colors}"

color_text = wtext(text='顏色: 紅色')
color_slider = slider(min=0, max=1, value=1,length=200, right=15, bind=set_color)

while True:
    rate(100)
    ball.pos.x += speed_slider.value * 0.1
    ball.radius = size_slider.value
    if ball.pos.x > 5:
        ball.pos.x = -5
