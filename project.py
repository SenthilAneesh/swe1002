from tkinter import *
from PIL import ImageTk, Image


class Form:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718")
        self.window.state("zoomed")
        self.window.resizable(0, 0)
        # ======================background image=========================================
        self.bg_frame = Image.open(r"C:\Users\anees\Downloads\Screenshot 2024-09-17 093231.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand=False)
        # ============================  TOP RED COLOUR  =====================================================================================
        self.lgn_frame = Frame(self.window, bg='red', width='100000', height='81')
        self.lgn_frame.place(x=0, y=0)
        # ===============================  CRICY LOGO =======================================================================================================
        self.side_image = Image.open(r"C:\Users\anees\Downloads\Screenshot 2024-09-17 103124FFFFFFFFFFF (1).png")
        side_photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.window, image=side_photo, bg="red")
        self.side_image_label.image = side_photo
        self.side_image_label.place(x=10, y=4)
        # ====================WALLET BUTTON=========================================
        self.wallet_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\png-clipart-wallet-computer-icons-handbag-leather-wallet-angle-rectangle-removebg-preview (1).png")
        wallet_button_photo = ImageTk.PhotoImage(self.wallet_button)
        self.lgn_wallet_label = Label(self.window, image=wallet_button_photo)
        self.lgn_wallet_label.image = wallet_button_photo
        self.wallet = Button(self.window, image=wallet_button_photo, width=50, bd=0, bg="red", cursor="hand2",
                             activebackground="red", fg="white",command=lambda:wallet(),)
        self.wallet.place(x=1130, y=16)
        def wallet():
            win = Toplevel()
            window_width = 350
            window_height = 350
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()
            position_top = int(screen_height / 4 - window_height / 4)
            position_right = int(screen_width / 2 - window_width / 2)
            win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
            win.title('Wallet')
            win.configure(background='white')
            win.resizable(False, False)
            bg_frame = Image.open(r"C:\Users\anees\Downloads\Screenshot 2024-09-17 093231.png")
            photo = ImageTk.PhotoImage(bg_frame)
            bg_panel = Label(win, image=photo)
            bg_panel.image = photo
            bg_panel.pack(fill='both', expand=False)
            # ============================  Current Balance  ====================================================================
            cb_label3 = Label(win, text='• Current Balance', fg="black", bg='white', font=("yu gothic ui", 13))
            cb_label3.place(x=40, y=30)
            balance_label3 = Label(win, text='₹0', fg="black", bg='white', font=("yu gothic ui", 24, 'bold'))
            balance_label3.place(x=250, y=22)
            # ===========================  amount entry ====================================================================================
            amount_entry = Entry(win, bg="white", font=("yu gothic ui", 14), highlightthickness=1, bd=0)
            amount_entry.place(x=50, y=115, width=230, height=40)
            amount_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
            amount_label = Label(win, text='• Amount to add', fg="black", bg='white', font=("yu gothic ui", 13))
            amount_label.place(x=40, y=85)
            # ==================================  coupon entry =========================================================================================
            coupon_entry = Entry(win, bg="white", font=("yu gothic ui", 14), highlightthickness=1, bd=0)
            coupon_entry.place(x=50, y=200, width=230, height=40)
            coupon_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
            coupon_label = Label(win, text='• Enter Coupon Code', fg="black", bg='white', font=("yu gothic ui", 12))
            coupon_label.place(x=40, y=165)
            # ==================================== proceedddddd==========================================================
            new_verify_label = Label(win, text='Proceed to verify your details and join the contest', fg="black",
                                     bg='white', font=("yu gothic ui", 10))
            new_verify_label.place(x=20, y=260)
            # =========================  ADD MONEY BUTTON  ===================================================================================================================
            add_money = Button(win, fg='white', text='Add Money', bg='red', font=("yu gothic ui", 12, "bold"),
                               cursor='hand2', relief="flat", bd=0,
                               highlightthickness=0, activebackground="red")
            add_money.place(x=70, y=290, width=200, height=35)

        # ==========================================progfile button===================================================================================
        self.profile_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\user-profile-person-icon-in-flat-isolated-in-suitable-for-social-media-man-profiles-screensavers-depicting-male-face-silhouettes-for-apps-website-vector-removebg-preview (1).png")
        profile_button_photo = ImageTk.PhotoImage(self.profile_button)
        self.lgn_profile_label = Label(self.window, image=profile_button_photo)
        self.lgn_profile_label.image = profile_button_photo
        self.profile = Button(self.window, image=profile_button_photo, width=50, bd=0, bg="red", cursor="hand2",
                              activebackground="red", fg="white")
        self.profile.place(x=1060, y=16)
        # ============================================NOTIFICATION BUTTON   =================================================================================
        self.noti_button = Image.open(r"C:\Users\anees\OneDrive\Desktop\4305482-removebg-preview (1).png")
        noti_button_photo = ImageTk.PhotoImage(self.noti_button)
        self.lgn_noti_label = Label(self.window, image=noti_button_photo)
        self.lgn_noti_label.image = noti_button_photo
        self.profile = Button(self.window, image=noti_button_photo, width=50, bd=0, bg="red", cursor="hand2",
                              activebackground="red", fg="white",command=lambda:noti(),)
        self.profile.place(x=1200, y=16)

        def noti():
            win = Toplevel()
            window_width = 350
            window_height = 350
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()
            position_top = int(screen_height / 4 - window_height / 4)
            position_right = int(screen_width / 2 - window_width / 2)
            win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
            win.title('Notification')
            win.configure(background='white')
            win.resizable(False, False)
            bg_frame = Image.open(r"C:\Users\anees\Downloads\Screenshot 2024-09-17 093231.png")
            photo = ImageTk.PhotoImage(bg_frame)
            bg_panel = Label(win, image=photo)
            bg_panel.image = photo
            bg_panel.pack(fill='both', expand=False)
            no_noti_label = Label(win, text='No Notifications found.\n Watch this space for exciting offers',
                                  fg="black", bg='white', font=("yu gothic ui", 13))
            no_noti_label.place(x=40, y=200)

            def close_window():
                win.destroy()

            ok_button = Button(win, fg='white', text='Okay', bg='red', font=("yu gothic ui", 12, "bold"),
                               cursor='hand2', relief="flat", bd=0,
                               highlightthickness=0, activebackground="red", command=close_window)
            ok_button.place(x=160, y=280)

        #=========================================================================================================================


        # ============================================ cricket BUTTON   =================================================================================
        self.cricket_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\Screenshot_2024-09-17_110756-removebg-preview (1).png")
        cricket_button_photo = ImageTk.PhotoImage(self.cricket_button)
        self.lgn_cricket_label = Label(self.window, image=cricket_button_photo)
        self.lgn_cricket_label.image = cricket_button_photo
        self.profile = Button(self.window, image=cricket_button_photo, width=190, bd=0, bg="red", cursor="hand2",
                              activebackground="red", fg="white",command=lambda:cricket())
        self.profile.place(x=230, y=92)

        def cricket():
            win = Tk()
            win.geometry("1166x718")
            win.state("zoomed")
            win.resizable(0, 0)
            win.title('Cricket')
            win.configure(background='white')
            win.resizable(False, False)
            bg_frame = Image.open(r"C:\Users\anees\OneDrive\Desktop\HORBAT.jpeg")
            photo = ImageTk.PhotoImage(bg_frame)
            bg_panel = Label(win, image=photo)
            bg_panel.image = photo
            bg_panel.pack(fill='both', expand=False)
            # ============================  TOP RED COLOUR  =====================================================================================
            lgn_frame = Frame(win, bg='red', width='100000', height='81')
            lgn_frame.place(x=0, y=0)
            # ===============================  CRICY LOGO =======================================================================================================
            side_image = Image.open(r"C:\Users\anees\Downloads\Screenshot 2024-09-17 103124FFFFFFFFFFF (1).png")
            side_photo = ImageTk.PhotoImage(side_image)
            side_image_label = Label(win, image=side_photo, bg="red")
            side_image_label.image = side_photo
            side_image_label.place(x=10, y=4)
            # ====================WALLET BUTTON=========================================
            wallet_button = Image.open(
                r"C:\Users\anees\OneDrive\Desktop\png-clipart-wallet-computer-icons-handbag-leather-wallet-angle-rectangle-removebg-preview (1).png")
            wallet_button_photo = ImageTk.PhotoImage(wallet_button)
            lgn_wallet_label = Label(win, image=wallet_button_photo)
            lgn_wallet_label.image = wallet_button_photo
            wallet = Button(win, image=wallet_button_photo, width=50, bd=0, bg="red", cursor="hand2",
                            activebackground="red", fg="white", command=lambda: wallet(), )
            wallet.place(x=1130, y=16)

            def wallet():
                win = Toplevel()
                window_width = 350
                window_height = 350
                screen_width = win.winfo_screenwidth()
                screen_height = win.winfo_screenheight()
                position_top = int(screen_height / 4 - window_height / 4)
                position_right = int(screen_width / 2 - window_width / 2)
                win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
                win.title('Wallet')
                win.configure(background='white')
                win.resizable(False, False)
                bg_frame = Image.open(r"C:\Users\anees\Downloads\Screenshot 2024-09-17 093231.png")
                photo = ImageTk.PhotoImage(bg_frame)
                bg_panel = Label(win, image=photo)
                bg_panel.image = photo
                bg_panel.pack(fill='both', expand=False)
                # ============================  Current Balance  ====================================================================
                cb_label3 = Label(win, text='• Current Balance', fg="black", bg='white', font=("yu gothic ui", 13))
                cb_label3.place(x=40, y=30)
                balance_label3 = Label(win, text='₹0', fg="black", bg='white', font=("yu gothic ui", 24, 'bold'))
                balance_label3.place(x=250, y=22)
                # ===========================  amount entry ====================================================================================
                amount_entry = Entry(win, bg="white", font=("yu gothic ui", 14), highlightthickness=1, bd=0)
                amount_entry.place(x=50, y=115, width=230, height=40)
                amount_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
                amount_label = Label(win, text='• Amount to add', fg="black", bg='white', font=("yu gothic ui", 13))
                amount_label.place(x=40, y=85)
                # ==================================  coupon entry =========================================================================================
                coupon_entry = Entry(win, bg="white", font=("yu gothic ui", 14), highlightthickness=1, bd=0)
                coupon_entry.place(x=50, y=200, width=230, height=40)
                coupon_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
                coupon_label = Label(win, text='• Enter Coupon Code', fg="black", bg='white', font=("yu gothic ui", 12))
                coupon_label.place(x=40, y=165)
                # ==================================== proceedddddd==========================================================
                new_verify_label = Label(win, text='Proceed to verify your details and join the contest', fg="black",
                                         bg='white', font=("yu gothic ui", 10))
                new_verify_label.place(x=20, y=260)
                # =========================  ADD MONEY BUTTON  ===================================================================================================================
                add_money = Button(win, fg='white', text='Add Money', bg='red', font=("yu gothic ui", 12, "bold"),
                                   cursor='hand2', relief="flat", bd=0,
                                   highlightthickness=0, activebackground="red")
                add_money.place(x=70, y=290, width=200, height=35)

            # ==========================================progfile button===================================================================================
            profile_button = Image.open(
                r"C:\Users\anees\OneDrive\Desktop\user-profile-person-icon-in-flat-isolated-in-suitable-for-social-media-man-profiles-screensavers-depicting-male-face-silhouettes-for-apps-website-vector-removebg-preview (1).png")
            profile_button_photo = ImageTk.PhotoImage(profile_button)
            lgn_profile_label = Label(win, image=profile_button_photo)
            lgn_profile_label.image = profile_button_photo
            profile = Button(win, image=profile_button_photo, width=50, bd=0, bg="red", cursor="hand2",
                             activebackground="red", fg="white")
            profile.place(x=1060, y=16)
            # ============================================NOTIFICATION BUTTON   =================================================================================
            noti_button = Image.open(r"C:\Users\anees\OneDrive\Desktop\4305482-removebg-preview (1).png")
            noti_button_photo = ImageTk.PhotoImage(noti_button)
            lgn_noti_label = Label(win, image=noti_button_photo)
            lgn_noti_label.image = noti_button_photo
            profile = Button(win, image=noti_button_photo, width=50, bd=0, bg="red", cursor="hand2",
                             activebackground="red", fg="white", command=lambda: noti(), )
            profile.place(x=1200, y=16)

            def noti():
                win = Toplevel()
                window_width = 350
                window_height = 350
                screen_width = win.winfo_screenwidth()
                screen_height = win.winfo_screenheight()
                position_top = int(screen_height / 4 - window_height / 4)
                position_right = int(screen_width / 2 - window_width / 2)
                win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
                win.title('Notification')
                win.configure(background='white')
                win.resizable(False, False)
                bg_frame = Image.open(r"C:\Users\anees\Downloads\Screenshot 2024-09-17 093231.png")
                photo = ImageTk.PhotoImage(bg_frame)
                bg_panel = Label(win, image=photo)
                bg_panel.image = photo
                bg_panel.pack(fill='both', expand=False)
                no_noti_label = Label(win, text='No Notifications found.\n Watch this space for exciting offers',
                                      fg="black", bg='white', font=("yu gothic ui", 13))
                no_noti_label.place(x=40, y=200)

                def close_window():
                    win.destroy()

                ok_button = Button(win, fg='white', text='Okay', bg='red', font=("yu gothic ui", 12, "bold"),
                                   cursor='hand2', relief="flat", bd=0,
                                   highlightthickness=0, activebackground="red", command=close_window)
                ok_button.place(x=160, y=280)

            # ==================================================================================================
            cricket1_button = Image.open(
                r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\cricket\Screenshot 2024-09-18 150429 (1).png")
            cricket1_button_photo = ImageTk.PhotoImage(cricket1_button)
            lgn_cricket1_label = Label(win, image=cricket1_button_photo)
            lgn_cricket1_label.image = cricket1_button_photo
            cricket1 = Button(win, image=cricket1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                              activebackground="red", fg="white")
            cricket1.place(x=50, y=130)

            # ==================================================================================================
            cricket2_button = Image.open(
                r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\cricket\Screenshot 2024-09-18 160733.png")
            cricket2_button_photo = ImageTk.PhotoImage(cricket2_button)
            lgn_cricket2_label = Label(win, image=cricket2_button_photo)
            lgn_cricket2_label.image = cricket2_button_photo
            cricket2 = Button(win, image=cricket2_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                              activebackground="red", fg="white")
            cricket2.place(x=470, y=123)

            # ==================================================================================================
            cricket3_button = Image.open(
                r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\cricket\Screenshot 2024-09-18 184251.png")
            cricket3_button_photo = ImageTk.PhotoImage(cricket3_button)
            lgn_cricket3_label = Label(win, image=cricket3_button_photo)
            lgn_cricket3_label.image = cricket3_button_photo
            cricket3 = Button(win, image=cricket3_button_photo, width=270, bd=0, bg="white", cursor="hand2",
                              activebackground="red", fg="white")
            cricket3.place(x=900, y=130)

            # ==================================================================================================
            football1_button = Image.open(
                r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\cricket\Screenshot 2024-09-18 195548.png")
            football1_button_photo = ImageTk.PhotoImage(football1_button)
            lgn_football1_label = Label(win, image=football1_button_photo)
            lgn_football1_label.image = football1_button_photo
            football1 = Button(win, image=football1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                               activebackground="red", fg="white")
            football1.place(x=50, y=330)

            # ==================================================================================================
            football1_button = Image.open(
                r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\cricket\Screenshot 2024-09-18 230852.png")
            football1_button_photo = ImageTk.PhotoImage(football1_button)
            lgn_football1_label = Label(win, image=football1_button_photo)
            lgn_football1_label.image = football1_button_photo
            football1 = Button(win, image=football1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                               activebackground="red", fg="white")
            football1.place(x=470, y=330)

            # ==================================================================================================
            football1_button = Image.open(
                r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\basketball\Screenshot 2024-09-19 005130.png")
            football1_button_photo = ImageTk.PhotoImage(football1_button)
            lgn_football1_label = Label(win, image=football1_button_photo)
            lgn_football1_label.image = football1_button_photo
            football1 = Button(win, image=football1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                               activebackground="red", fg="white")
            football1.place(x=900, y=330)

            # ==================================================================================================
            football1_button = Image.open(
                r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\basketball\Screenshot 2024-09-19 005451.png")
            football1_button_photo = ImageTk.PhotoImage(football1_button)
            lgn_football1_label = Label(win, image=football1_button_photo)
            lgn_football1_label.image = football1_button_photo
            football1 = Button(win, image=football1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                               activebackground="red", fg="white")
            football1.place(x=50, y=500)

            # ==================================================================================================
            football1_button = Image.open(
                r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\basketball\Screenshot 2024-09-19 010431.png")
            football1_button_photo = ImageTk.PhotoImage(football1_button)
            lgn_football1_label = Label(win, image=football1_button_photo)
            lgn_football1_label.image = football1_button_photo
            football1 = Button(win, image=football1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                               activebackground="red", fg="white")
            football1.place(x=470, y=500)

            # ==================================================================================================
            football1_button = Image.open(
                r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\football\Screenshot 2024-09-19 000610.png")
            football1_button_photo = ImageTk.PhotoImage(football1_button)
            lgn_football1_label = Label(win, image=football1_button_photo)
            lgn_football1_label.image = football1_button_photo
            football1 = Button(win, image=football1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                               activebackground="red", fg="white")
            football1.place(x=900, y=500)

        # ============================================ FOOTBALL BUTTON   =================================================================================
        self.football_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\Screenshot_2024-09-17_110225-removebg-preview (1).png")
        football_button_photo = ImageTk.PhotoImage(self.football_button)
        self.lgn_football_label = Label(self.window, image=football_button_photo)
        self.lgn_football_label.image = football_button_photo
        self.profile = Button(self.window, image=football_button_photo, width=190, bd=0, bg="red", cursor="hand2",
                              activebackground="red", fg="white")
        self.profile.place(x=20, y=92)

        # ============================================ BASKETBALL BUTTON   =================================================================================
        self.basket_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\Screenshot 2024-09-17 110501.png")
        basket_button_photo = ImageTk.PhotoImage(self.basket_button)
        self.lgn_basket_label = Label(self.window, image=basket_button_photo)
        self.lgn_basket_label.image = basket_button_photo
        self.profile = Button(self.window, image=basket_button_photo, width=190, bd=0, bg="red", cursor="hand2",
                              activebackground="red", fg="white")
        self.profile.place(x=440, y=92)

        # ============================================ KABBADI BUTTON   =================================================================================
        self.kabbadi_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\Screenshot_2024-09-17_110710-removebg-preview (1).png")
        kabbadi_button_photo = ImageTk.PhotoImage(self.kabbadi_button)
        self.lgn_kabbadi_label = Label(self.window, image=kabbadi_button_photo)
        self.lgn_kabbadi_label.image = kabbadi_button_photo
        self.profile = Button(self.window, image=kabbadi_button_photo, width=190, bd=0, bg="red", cursor="hand2",
                              activebackground="red", fg="white")
        self.profile.place(x=650, y=92)

        # ============================================ BASEBALL BUTTON   =================================================================================
        self.baseball_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\Screenshot 2024-09-17 110106.png")
        baseball_button_photo = ImageTk.PhotoImage(self.baseball_button)
        self.lgn_baseball_label = Label(self.window, image=baseball_button_photo)
        self.lgn_baseball_label.image = baseball_button_photo
        self.profile = Button(self.window, image=baseball_button_photo, width=190, bd=0, bg="red", cursor="hand2",
                              activebackground="red", fg="white")
        self.profile.place(x=860, y=92)
        # ============================================ HOCKEY BUTTON   =================================================================================
        self.hockey_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\Screenshot_2024-09-17_110710-removebg-preview (1).png")
        hockey_button_photo = ImageTk.PhotoImage(self.hockey_button)
        self.lgn_hockey_label = Label(self.window, image=hockey_button_photo)
        self.lgn_hockey_label.image = hockey_button_photo
        self.profile = Button(self.window, image=hockey_button_photo, width=190, bd=0, bg="red", cursor="hand2",
                              activebackground="red", fg="white")
        self.profile.place(x=1070, y=92)
        # =========================================== Upcomming game ======================================================================================================
        self.txt1 = 'Upcoming Matches'
        self.heading = Label(self.window, text=self.txt1, font=("yu gothic ui", 25, 'bold'), bg="white", fg="black")
        self.heading.place(x=450, y=150, width=300, height=50)
        #=========================================
        #self.side_image = Image.open(r"C:\Users\anees\Downloads\Screenshot 2024-09-18 150429 (1).png")
       # side_photo = ImageTk.PhotoImage(self.side_image)
       # self.side_image_label = Label(self.window, image=side_photo, bg="white")
        #self.side_image_label.image = side_photo
       # self.side_image_label.place(x=50, y=240)
        #==================================================================================================
        self.cricket1_button = Image.open(r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\cricket\Screenshot 2024-09-18 150429 (1).png")
        cricket1_button_photo = ImageTk.PhotoImage(self.cricket1_button)
        self.lgn_cricket1_label = Label(self.window, image=cricket1_button_photo)
        self.lgn_cricket1_label.image = cricket1_button_photo
        self.cricket1 = Button(self.window, image=cricket1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                             activebackground="red", fg="white")
        self.cricket1.place(x=50, y=240)

        # ==================================================================================================
        self.cricket2_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\cricket\Screenshot 2024-09-18 160733.png")
        cricket2_button_photo = ImageTk.PhotoImage(self.cricket2_button)
        self.lgn_cricket2_label = Label(self.window, image=cricket2_button_photo)
        self.lgn_cricket2_label.image = cricket2_button_photo
        self.cricket2 = Button(self.window, image=cricket2_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                               activebackground="red", fg="white")
        self.cricket2.place(x=470, y=240)

        # ==================================================================================================
        self.cricket3_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\cricket\Screenshot 2024-09-18 184251.png")
        cricket3_button_photo = ImageTk.PhotoImage(self.cricket3_button)
        self.lgn_cricket3_label = Label(self.window, image=cricket3_button_photo)
        self.lgn_cricket3_label.image = cricket3_button_photo
        self.cricket3 = Button(self.window, image=cricket3_button_photo, width=270, bd=0, bg="white", cursor="hand2",
                               activebackground="red", fg="white")
        self.cricket3.place(x=900, y=240)

        # ==================================================================================================
        self.football1_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\football\Screenshot 2024-09-19 000610.png")
        football1_button_photo = ImageTk.PhotoImage(self.football1_button)
        self.lgn_football1_label = Label(self.window, image=football1_button_photo)
        self.lgn_football1_label.image = football1_button_photo
        self.football1 = Button(self.window, image=football1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                               activebackground="red", fg="white")
        self.football1.place(x=50, y=440)

        # ==================================================================================================
        self.football1_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\football\Screenshot 2024-09-19 000148.png")
        football1_button_photo = ImageTk.PhotoImage(self.football1_button)
        self.lgn_football1_label = Label(self.window, image=football1_button_photo)
        self.lgn_football1_label.image = football1_button_photo
        self.football1 = Button(self.window, image=football1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                                activebackground="red", fg="white")
        self.football1.place(x=470, y=440)

        # ==================================================================================================
        self.football1_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\basketball\Screenshot 2024-09-19 005130.png")
        football1_button_photo = ImageTk.PhotoImage(self.football1_button)
        self.lgn_football1_label = Label(self.window, image=football1_button_photo)
        self.lgn_football1_label.image = football1_button_photo
        self.football1 = Button(self.window, image=football1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                                activebackground="red", fg="white")
        self.football1.place(x=900, y=440)

        # ==================================================================================================
        self.football1_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\basketball\Screenshot 2024-09-19 005451.png")
        football1_button_photo = ImageTk.PhotoImage(self.football1_button)
        self.lgn_football1_label = Label(self.window, image=football1_button_photo)
        self.lgn_football1_label.image = football1_button_photo
        self.football1 = Button(self.window, image=football1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                                activebackground="red", fg="white")
        self.football1.place(x=50, y=640)

        # ==================================================================================================
        self.football1_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\basketball\Screenshot 2024-09-19 010431.png")
        football1_button_photo = ImageTk.PhotoImage(self.football1_button)
        self.lgn_football1_label = Label(self.window, image=football1_button_photo)
        self.lgn_football1_label.image = football1_button_photo
        self.football1 = Button(self.window, image=football1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                                activebackground="red", fg="white")
        self.football1.place(x=470, y=640)

        # ==================================================================================================
        self.football1_button = Image.open(
            r"C:\Users\anees\OneDrive\Desktop\tkinter pics\page2\matchh\football\Screenshot 2024-09-19 000610.png")
        football1_button_photo = ImageTk.PhotoImage(self.football1_button)
        self.lgn_football1_label = Label(self.window, image=football1_button_photo)
        self.lgn_football1_label.image = football1_button_photo
        self.football1 = Button(self.window, image=football1_button_photo, width=300, bd=0, bg="white", cursor="hand2",
                                activebackground="red", fg="white")
        self.football1.place(x=900, y=640)

def page():
    window = Tk()
    Form(window)
    window.mainloop()


if __name__ == "__main__":
    page()
