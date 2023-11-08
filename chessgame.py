# python chessgame.py
# pip install python-chess
# - pip install chess

# flet
#import flet
import flet as ft
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    FilePickerUploadEvent,
    FilePickerUploadFile,
    Page,
    ProgressRing,
    Ref,
    Row,
    Text,
    icons,
    Column,
    Draggable,
    Container,
    border,
    colors,  
    Draggable,
    DragTarget,
    DragTargetAcceptEvent,
)

import time

# chessgame
import chess
board=chess.Board()

#board=chess.board
chessgame = ['e4', 'e5', 'Nf3', 'f6', 'Nxe5', 'fxe5', 'Qh5+', 'Ke7', 'Qxe5+', 'Kf7', 'Bc4+', 'd5', 'Bxd5+', 'Kg6', 'h4', 'h5', 'Bxb7', 'Bxb7', 'Qf5+', 'Kh6', 'd4+', 'g5', 'Qf7', 'Qe7', 'hxg5+', 'Qxg5', 'Rxh5']
chessgamexy =[[4, 6, 4, 4], [4, 1, 4, 3], [6, 7, 5, 5], [5, 1, 5, 2], [5, 5, 4, 3], [5, 2, 4, 3], [3, 7, 7, 3], [4, 0, 4, 1], [7, 3, 4, 3], [4, 1, 5, 1], [5, 7, 2, 4], [3, 1, 3, 3], [2, 4, 3, 3], [5, 1, 6, 2], [7, 6, 7, 4], [7, 1, 7, 3], [3, 3, 1, 1], [2, 0, 1, 1], [4, 3, 5, 3], [6, 2, 7, 2], [3, 6, 3, 4], [6, 1, 6, 3], [5, 3, 5, 1], [3, 0, 4, 1], [7, 4, 6, 3], [4, 1, 6, 3], [7, 7, 7, 3]]

_GLOBAL_MODE = 2  # 1 app, 2 web

pieces = [
        {"name": "rook", "symbol": "♖", "color":1, "nm":"r", "val":4, "img":"rw.png", "char":"R"},
        {"name": "knight", "symbol": "♘", "color":1, "nm":"n", "val":2, "img":"hw.png", "char":"N"},
        {"name": "bishop", "symbol": "♗", "color":1, "nm":"b", "val":3, "img":"bw.png", "char":"B"},
        {"name": "queen", "symbol": "♕", "color":1, "nm":"q", "val":5, "img":"qw.png", "char":"Q"},
        {"name": "king", "symbol": "♔", "color":1, "nm":"k", "val":6, "img":"kw.png", "char":"K"},
        {"name": "pawn", "symbol": "♙", "color":1, "nm":"p", "val":1, "img":"pw.png", "char":"P"},
        {"name": "rook", "symbol": "♜", "color":0, "nm":"r", "val":-4, "img":"rb.png", "char":"r"},
        {"name": "knight", "symbol": "♞", "color":0, "nm":"n", "val":-2, "img":"hb.png", "char":"n"},
        {"name": "bishop", "symbol": "♝", "color":0, "nm":"b", "val":-3, "img":"bb.png", "char":"b"},
        {"name": "queen", "symbol": "♛", "color":0, "nm":"q", "val":-5, "img":"qb.png", "char":"q"},
        {"name": "king", "symbol": "♚", "color":0, "nm":"k", "val":-6, "img":"kb.png", "char":"k"},
        {"name": "pawn", "symbol": "♟", "color":0, "nm":"p", "val":-1, "img":"pb.png", "char":"p"},
]

board = [ 
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

def pieces_search_image(letter_piece):
    r = ""
    return next((p["img"] for p in pieces if p["char"]==letter_piece), r)

START_END = -1 # -1 # 0 START MOVE, 1 END MOVE, -1 None
INI_MOVE = -1
END_MOVE = -1
SPACE = " "

# 47 = 4 , 7
def get_ten_unit(num):
    div = int(num/10) # ten
    module = num%10   # unit(s)
    return div, module    

def getboardxy(x,y):
    return board[y][x]

def setboardxy(x,y, value):
    board[y][x] = value

def do_movexy(x1,y1 ,x2,y2):
    piece = getboardxy(x1,y1)
    setboardxy(x1,y1, SPACE)
    setboardxy(x2,y2, piece)

def do_move(page: ft.Page):
    global START_END, INI_MOVE, END_MOVE, SPACE
    #
    y1,x1 = get_ten_unit(INI_MOVE)
    y2,x2 = get_ten_unit(END_MOVE)
    #    
    do_movexy(x1,y1 ,x2,y2)
    #
    print("move",x1,y1 ,x2,y2)
    #
    draw_board(page)

def draw_board(page: ft.Page):
    clean_controls(page)

    audiofile = "computer-click.mp3"
    source_file = f"/sound/{audiofile}"
    source_file = "D:/flet/FletSqlAlchemySQliteCRUDPlotgallery/assets/sound/computer-click.mp3"  
    print(source_file)
    audio1 = ft.Audio(src=source_file, autoplay=True)	
    page.overlay.append(audio1)

    def on_click_on_square(e,page: ft.Page):
        global START_END, INI_MOVE, END_MOVE
        idx = e.control.data
        print(idx)
        if  START_END==-1: 
            print(-1)
            START_END=0
            INI_MOVE = idx
        elif START_END==0:
            print(0)
            START_END=1
            END_MOVE = idx
        elif START_END==1:
            print(1)
            print("call->do_move")
            do_move(page)
            audio1.pause()
            START_END = -1
            INI_MOVE = -1
            END_MOVE = -1
    
    container1 = Container(
            width=50,
            height=50,
            bgcolor=colors.WHITE,
            border_radius=1,
        )
    container2 = Container(
            width=50,
            height=50,
            bgcolor=colors.BLUE,
            border_radius=1,
        )
    
    col_select = ft.Row() # horizontal squares
    row_select = ft.Column() # vertical squares
    #
    list_row = []
    list_column = []
    #
    for i in range(8): # vert.
        list_row = [] 
        for j in range(8): # horiz
            x=j;y=i
            letter_piece = getboardxy(x,y) # boardxy(x,y) # board[y][x]
            #
            if (i+j)%2==0:
                backcolor_square = colors.WHITE
                container_empty = container1
            else:
                backcolor_square = colors.BLUE
                container_empty = container2
            #
            if letter_piece.strip() != "":
                image_png = pieces_search_image(letter_piece)
                source_file = f"/chesspieces/{image_png}"
                container_with_piece = Container(
                        width=50,
                        height=50,
                        bgcolor=backcolor_square,
                        border_radius=1,
                        content=ft.Image(src=source_file,fit=ft.ImageFit.CONTAIN),
                    )                 
                container_to_draw = container_with_piece
            else:
                container_to_draw = container_empty         
            #
            list_row.append(ft.Container(content=container_to_draw,data=i*10+j,on_click=lambda e: on_click_on_square(e,page)))
        col_select = ft.Row(list_row)
        list_column.append(col_select)
    #
    row_select = ft.Column(list_column)
    page.add(row_select)

    b = ft.ElevatedButton("flet: View a ChessGame", on_click=lambda e: play_game(e,page), data=0)
    page.add(b)

def play_game(e,page: ft.Page):
    print("play_game")
    for m in chessgamexy:
        x1,y1 ,x2,y2 = m[0],m[1],m[2],m[3]
        do_movexy(x1,y1 ,x2,y2)
        print("move",x1,y1 ,x2,y2)
        draw_board(page)
        time.sleep(2)

def draw_main(page: ft.Page):
    
    draw_board(page)

    def drag_will_accept(e):
        e.control.content.border = border.all(
            2, colors.BLACK45 if e.data == "true" else colors.RED
        )
        e.control.update()

    def drag_accept(e: DragTargetAcceptEvent):
        src = page.get_control(e.src_id)
        e.control.content.bgcolor = src.content.bgcolor
        e.control.content.border = None
        e.control.update()

    def drag_leave(e):
        e.control.content.border = None
        e.control.update()
    page.add(
        Row(
            [
                #Column(
                #    [
                        Draggable(
                            group="color",
                            content=Container(
                                content=ft.Text("F",size=15,bgcolor=ft.colors.BLUE),
                                width=50,
                                height=50,
                                bgcolor=colors.CYAN,
                                border_radius=5,
                            ),
                            content_feedback=Container(
                                width=20,
                                height=20,
                                bgcolor=colors.CYAN,
                                border_radius=3,
                            ),
                        ),
                        Draggable(
                            group="color",
                            content=Container(
                                content=ft.Text("L",size=15,bgcolor=ft.colors.BLUE),
                                width=50,
                                height=50,
                                bgcolor=colors.YELLOW,
                                border_radius=5,
                            ),
                        ),
                        Draggable(
                            group="color1",
                            content=Container(
                                content=ft.Text("E",size=15,bgcolor=ft.colors.BLUE),
                                width=50,
                                height=50,
                                bgcolor=colors.GREEN,
                                border_radius=5,
                            ),
                        ),
                    #]
                #),
                Container(width=100),
                DragTarget(
                    group="color",
                    content=Container(
                        content=ft.Text("T",size=15,bgcolor=ft.colors.BLUE),
                        width=50,
                        height=50,
                        bgcolor=colors.BLUE_GREY_100,
                        border_radius=5,
                    ),
                    on_will_accept=drag_will_accept,
                    on_accept=drag_accept,
                    on_leave=drag_leave,
                ),
            ]
        )
    )

# clean controls
def clean_controls(page):
	tot_controls = len(page.controls)
	for _ in range(tot_controls):
		#print(page.controls.__str__()) 
		page.controls.pop()
	# page.update()

# main
def main(page):
	# GENERAL SETTING
	page.title = "Chess"
	page.scroll = "always" # scroll
    #
    #
	draw_main(page)

mode=_GLOBAL_MODE
if mode==1: # app
	ft.app(target=main,assets_dir="assets", upload_dir="assets/uploads")	
elif mode==2: # web
	#ft.app(target=main,port=8881,view=ft.WEB_BROWSER,assets_dir="assets", upload_dir="assets/uploads")
	ft.app(target=main,port=8550,view=ft.WEB_BROWSER,assets_dir="assets", upload_dir="assets/uploads")

