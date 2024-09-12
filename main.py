from login_UI import login_UI
from main_UI import main_UI

    def main():
        if logged == True:
            main_UI()
        else:
            login_UI()


login_UI()
main_UI()