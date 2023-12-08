from fpdf import FPDF


class MyPDF(FPDF):
    def __init__(self):
        super().__init__(unit = "mm", format = "A4")

    def header(self):
        self.set_font("Arial", "B", 30)
        self.cell(0, 10, "CS50 Shirtificate", align="C")


    def new_shirt(self, name):
        # self.add_font("PressStartP2", "", "/workspaces/125621684/shirtificate/PressStart2P-Regular.ttf", uni=True)
        self.set_font("Arial", "", 15)
        self.image("shirtificate.png", x=25, y=35, w=160)
        self.set_text_color(255,255,255)
        self.set_xy(25, 80)
        self.cell(160, 10, f"{name} took CS50", ln=True, align="C")

def main():
    pdf = MyPDF()
    name = str(input("Name: "))
    pdf.add_page()
    pdf.new_shirt(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
