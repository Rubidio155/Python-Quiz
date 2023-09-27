# Este proyecto genera un quiz o cuestionario de tipo test multi-respuesta
# This project generates a multi-answer test quiz or questionnaire

# Importamos los módulos necesarios
# Let's import the necessary modules

from tkinter import *
import pandas as pd   # Hay que instalar pandas y openpyxl / pandas and openpyxl have to be installed

# Leemos el documento plantilla de excel (Quiz-Template.xlsx) con las preguntas y respuestas deseadas
# Let's read the excel document template (Quiz-Template.xlsx) with the desired questions and answers

df = pd.read_excel('Quiz-Template.xlsx', sheet_name=0, skiprows=2)

# Separamos las columnas de las preguntas, de las opciones y de las respuestas correctas en sus respectivas variables
# Let's separate the questions, options and correct answers columns in their respective variables

questions_0 = df.iloc[:, 0]
options_0 = df.iloc[:, 1]
answers = df.iloc[:, 2]

# Convertimos la columna con las opciones en una lista
# Let's turn the column with the options into a list

options_1 = options_0.values.tolist()

# Definimos una lista en la que guardamos las listas de las distintas opciones para cada pregunta
# Let's define a list in which we store the lists of the different options for each question

options = []
for option in options_1:
	choices = option.split(" - ")
	options.append(choices)

# Convertimos la columna con las preguntas en una lista
# Let's turn the column with the questions into a list

questions_1 = questions_0.values.tolist()

# Definimos un diccionario en el que guardamos las preguntas y sus respuestas correspondientes
# Let's define a dictionary in which we store the questions and its answers

questions = {}
for element in questions_1:
	questions[element] = options[questions_1.index(element)]

# Convertimos la columna con las respuestas correctas en una lista
# Let's turn the column with the correct answers into a list

ans = answers.values.tolist()

# Definimos una variable que registra la pregunta por la que se va
# Let's define a variable that registers the current question

current_question = 0

# Definimos la función que inicia el quiz
# Let's define the function that starts the quiz


def start_quiz():
	start_button.forget()
	next_button.pack()
	next_question()

# Definimos la función que pasa a la siguiente pregunta
# Let's define the function that goes to the next question


def next_question():
	global current_question
	if current_question < len(questions):
		# Obtenemos la pregunta que toca:
		# Let's get the current question
		check_ans()
		user_ans.set('None')
		c_question = list(questions.keys())[current_question]
		# Borramos la ventana para poder actualizarla
		# Let's clear the frame to update its content
		clear_frame()
		# Imprimimos la pregunta
		# Let's print the question
		Label(f1, text=f"Pregunta : {c_question}", padx=15, font="calibre 12 normal").pack(anchor=NW)
		# Imprimimos las opciones
		# Let's print the options
		for choice in questions[c_question]:
			Radiobutton(f1, text=choice, variable=user_ans, value=choice, padx=28).pack(anchor=NW)
		current_question += 1
	else:
		next_button.forget()
		check_ans()
		clear_frame()
		output = f"{user_score.get()} de {len(questions)} puntos"
		Label(f1, text=output, font="calibre 25 bold").pack()
		Label(f1, text="Gracias por participar", font="calibre 18 bold").pack()

# Definimos la función que comprueba si las respuestas son correctas
# Let's define the function that checks if the answers are correct


def check_ans():
	temp_ans = user_ans.get()
	if temp_ans != 'None' and temp_ans == ans[current_question-1]:
		user_score.set(user_score.get()+1)


# Definimos la función que borra la ventana actual para poder avanzar a la siguiente pregunta
# Let's define the function that clears the frame to continue to next question

def clear_frame():
	for widget in f1.winfo_children():
		widget.destroy()


# Función principal:
# Main function

if __name__ == "__main__":
	root = Tk()
	# Características de la ventana
	root.title("QUIZ")
	root.geometry("850x520")
	root.minsize(800, 400)

	user_ans = StringVar()
	user_ans.set('None')
	user_score = IntVar()
	user_score.set(0)

	Label(root, text="Quiz", font="calibre 40 bold", relief=SUNKEN, background="cyan", padx=10, pady=9).pack()
	Label(root, text="", font="calibre 10 bold").pack()
	start_button = Button(root, text="Empezar", command=start_quiz, font="calibre 17 bold")
	start_button.pack()

	f1 = Frame(root)
	f1.pack(side=TOP, fill=X)

	next_button = Button(root, text="Siguiente pregunta", command=next_question, font="calibre 17 bold")

	root.mainloop()
