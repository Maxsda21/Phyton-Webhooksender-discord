import requests
import tkinter as tk

class DiscordWebhookGUI:
    def __init__(self, master):
        self.master = master
        master.title("Discord Webhook Sender")

        self.label = tk.Label(master, text="Enter your Discord webhook URL:")
        self.label.pack()

        self.entry = tk.Entry(master, width=50)
        self.entry.pack()

        self.button = tk.Button(master, text="Submit", command=self.show_send_message_gui)
        self.button.pack()

    def show_send_message_gui(self):
        global WEBHOOK_URL
        WEBHOOK_URL = self.entry.get()
        self.master.destroy()

        self.send_message_gui = tk.Tk()
        self.send_message_gui.title("Discord Webhook Sender")

        self.label = tk.Label(self.send_message_gui, text="Enter your message:")
        self.label.pack()

        self.entry = tk.Entry(self.send_message_gui, width=50)
        self.entry.pack()

        self.button = tk.Button(self.send_message_gui, text="Send", command=self.send_message)
        self.button.pack()

    def send_message(self):
        message = self.entry.get()
        payload = {
            "content": message
        }
        requests.post(WEBHOOK_URL, json=payload)
        self.entry.delete(0, tk.END)
        tk.messagebox.showinfo(title="Success", message="Message sent successfully!")


if __name__ == '__main__':
    root = tk.Tk()
    gui = DiscordWebhookGUI(root)
    root.mainloop()
