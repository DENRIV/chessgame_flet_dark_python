# python chesstest.py
# chessgame
import chess
##import chess.pg
import ChessBoard

#board=chess.Board()
#legal_moves = board.legal_moves
board=ChessBoard()

chessgame = ['e4', 'e5', 'Nf3', 'f6', 'Nxe5', 'fxe5', 'Qh5+', 'Ke7', 'Qxe5+', 'Kf7', 'Bc4+', 'd5', 'Bxd5+', 'Kg6', 'h4', 'h5', 'Bxb7', 'Bxb7', 'Qf5+', 'Kh6', 'd4+', 'g5', 'Qf7', 'Qe7', 'hxg5+', 'Qxg5', 'Rxh5']
#chessgame = ['e4', 'e5', 'Nf3', 'f6', 'Nxe5']

def is_legal_move(coordmove, legal_moves):
    r = False
    '''
    for i in legal_moves:
        if coordmove == i:
            return True
    return r
    '''
    return next((True for i in legal_moves if coordmove == i), r)

def test():
    for m in chessgame: 
        coordmove = board.parse_san(m)
        print(m, "=>" , coordmove)
        #print(m)
        islegal = is_legal_move(coordmove, board.legal_moves)
        print("islegalmove:",islegal)
        if islegal:
            board.push_san(m)
            
    r = board.is_checkmate()
    print(r)

    # draw board
    board

_GLOBAL_MODE = 1

# main
def main(page):
    test()

mode=_GLOBAL_MODE
'''
if mode==1: # app
	ft.app(target=main,assets_dir="assets", upload_dir="assets/uploads")	
elif mode==2: # web")
	ft.app(target=main,port=8550,view=ft.WEB_BROWSER,assets_dir="assets", upload_dir="assets/uploads")
'''


