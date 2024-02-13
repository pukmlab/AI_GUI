import PySimpleGUI as sg
from PIL import Image, ImageDraw, ImageOps

# 描画で使っている変数
white = (255, 255, 255)
draw_color='white'
app_size = (600, 700)
draw_canvas_size =(600, 490)
draw_thickness = 10
im = Image.new('RGB', draw_canvas_size, white)
draw = ImageDraw.Draw(im)
filename = "my_drawing.png"

layout = [
    [
        sg.Graph(
            canvas_size=draw_canvas_size,
            graph_top_right=(0, 0),
            graph_bottom_left=draw_canvas_size,
            key="graph",
            change_submits=True,
            background_color=draw_color,
            # enabling drag_submits enables mouse_drags, but disables mouse_up events
            drag_submits=True
        )
    ],
    [sg.Button('undo', key='__UNDO__',  size=(35,2)), sg.Button('clear', key='_CLEAR_', size=(35,2))],
    [sg.Text('No input',background_color='red', size=(100,2), key='_RESULT_', text_color='white') ],
]
window = sg.Window("drawing", layout,size=app_size)
graph = window.Element("graph")
while True:
    event, values = window.read()
    graph.DrawCircle(values['graph'], draw_thickness, fill_color='black',line_color='black') 
    draw.ellipse((draw_canvas_size[0]-values['graph'][0]-draw_thickness,values['graph'][1]-draw_thickness, draw_canvas_size[0]-values['graph'][0]+draw_thickness,values['graph'][1]+draw_thickness), fill=(0, 0, 0), outline=(0, 0, 0))
    if event == sg.WIN_CLOSED or event == "OK":
        break
window.close()