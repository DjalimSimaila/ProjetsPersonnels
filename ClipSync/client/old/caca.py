import curses
from multiprocessing import Process

p = None
def display(stdscr):
    while True:
        stdscr.clear()
        stdscr.timeout(500)
        maxy, maxx = stdscr.getmaxyx()
        curses.newwin(2,maxx,3,1)
        # invisible cursor
        curses.curs_set(0)

        if (curses.has_colors()):
            # Start colors in curses
            curses.start_color()
            curses.use_default_colors()
            curses.init_pair(1, curses.COLOR_RED, -1)
        stdscr.refresh()

        curses.init_pair(1, 0, -1)
        curses.init_pair(2, 1, -1)
        curses.init_pair(3, 2, -1)
        curses.init_pair(4, 3, -1)

        profil = curses.newwin(maxy//4,maxx//4,0,0)
        profil.box()
        profil.addstr("profil")
        profil.refresh()

        sidebar = curses.newwin(3*maxy//4,maxx//4,maxy//4,0)
        sidebar.box()
        sidebar.addstr("amis / serveurs")
        sidebar.refresh()
        
        mainbar = curses.newwin(maxy,3*maxx//4,0,maxx//4)
        mainbar.box()
        mainbar.addstr('nom du groupe')
        mainbar.refresh()
        stdscr.refresh()
        event = stdscr.getch()
        if event == ord("q"):
            break

def hang():
    while True:
        temp = 1 + 1

if __name__ == '__main__':
    p = Process(target = hang)
    curses.wrapper(display)
