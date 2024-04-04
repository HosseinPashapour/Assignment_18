import sys
from functools import partial
from random import randint
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

app = QApplication(sys.argv)
player = 1
player_1_score = 0
player_2_score = 0
draw = 0
loader = QUiLoader()
main_window = loader.load("Tic_Tac_Toe.ui")


def check():
    if "X" == buttons[0][0].text() == buttons[1][1].text() == buttons[2][2].text() or "X" == buttons[0][2].text() == buttons[1][1].text() == buttons[2][0].text():
        return "player 1"
    elif "O" == buttons[0][0].text() == buttons[1][1].text() == buttons[2][2].text() or "O" == buttons[0][2].text() == buttons[1][1].text() == buttons[2][0].text():
        return "player 2"
    for i in range(3):
        if "X" == buttons[i][0].text() == buttons[i][1].text() == buttons[i][2].text() or "X" == buttons[0][i].text() == buttons[1][i].text() == buttons[2][i].text():
            return "player 1"
        elif "O" == buttons[i][0].text() == buttons[i][1].text() == buttons[i][2].text() or "O" == buttons[0][i].text() == buttons[1][i].text() == buttons[2][i].text():
            return "player 2"
    
    draw_flag = True
    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            if buttons[i][j].text() == "":
                draw_flag = False
                break
    if draw_flag:
        return "draw"
    return False

def reset_game():
    global player
    player = 1
    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            buttons[i][j].setText("")

def new_game():
    global player_1_score, player_2_score, draw
    player_1_score = 0
    main_window.player_1_scoreboard.setText(str(player_1_score))
    player_2_score = 0
    main_window.player_2_scoreboard.setText(str(player_2_score))
    draw = 0
    main_window.draw_scoreboard.setText(str(draw))
    reset_game()

def show_info():
    msg_box = QMessageBox(text=""" تیک تاک یک بازی ساده برای دو بازیکن است.
اولین بازیکنی که بتواند به سرعت یک سطر یا یک ستون یا مربع مورب را پر کند، برنده بازی است.
اگر تمام خانه های جدول پر شده باشد و هیچکس موفق به تکمیل شرایط ذکر شده نشود،
بازی مساوی خواهد شد
    """)
    msg_box.exec()

def update_labels(winner):
    global player_1_score
    global player_2_score
    global draw
    if winner == "player 1":
        player_1_score += 1
        main_window.player_1_scoreboard.setText(str(player_1_score))
        msg_box = QMessageBox(text="😍 You wins! 🫡")
    elif winner == "player 2":
        player_2_score += 1
        main_window.player_2_scoreboard.setText(str(player_2_score))
        if game_mode == "vs-player":
            msg_box = QMessageBox(text="😯 Player 2 wins! 😶‍🌫️")
        else:
            msg_box = QMessageBox(text="😅 CPU wins! 😁")
    else:
        draw += 1
        main_window.draw_scoreboard.setText(str(draw))
        msg_box = QMessageBox(text="Draw!")
    msg_box.exec()
    reset_game()

def change_player(player):
    global game_mode
    if player != game_mode:
        game_mode = player
        if player == "vs-cpu":
            main_window.seccond_player_btn.setText("O (CPU)")
        else:
            main_window.seccond_player_btn.setText("O (PLAYER 2)")
        new_game()

def play(row, col):
    global player
    global buttons
    if buttons[row][col].text() == "":
        if player == 1:
            buttons[row][col].setStyleSheet("color: #31C4BE; background-color: #1f3540;")
            buttons[row][col].setText("X")
            if game_mode != "vs-cpu":
                player = 2
        else:
            buttons[row][col].setStyleSheet("color: #EFB238; background-color: #1f3540;")
            buttons[row][col].setText("O")
            player = 1
        winner = check()
        if winner:
            update_labels(winner)
        elif game_mode == "vs-cpu":
            row = randint(0, 2)
            col = randint(0, 2)
            while buttons[row][col].text() != '':
                row = randint(0, 2)
                col = randint(0, 2)
            buttons[row][col].setStyleSheet("color: #EFB238; background-color: #1f3540;")
            buttons[row][col].setText('O')
            winner = check()
            if winner:
                update_labels(winner)
    else:
        msg = QMessageBox(text="It can't be done here! choose again.")
        msg.exec()


game_mode = "vs-cpu" if main_window.play_vs_cpu.isChecked() else "vs-player"
main_window.show()
buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
         [main_window.btn_4, main_window.btn_5, main_window.btn_6],
         [main_window.btn_7, main_window.btn_8, main_window.btn_9]]
for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))
main_window.reset_btn.clicked.connect(new_game)
main_window.play_vs_cpu.clicked.connect(partial(change_player, "vs-cpu"))
main_window.play_vs_player.clicked.connect(partial(change_player, "vs-player"))
main_window.about_btn.clicked.connect(show_info)

app.exec()
