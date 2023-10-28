# Este proyecto genera un quiz o cuestionario de tipo test multi-respuesta
# This project generates a multi-answer test quiz or questionnaire

# Importamos los módulos necesarios
# Let's import the necessary modules

from tkinter import *
import random
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
	choices = option.split(" & ")
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

question_list = list(questions.keys())
temporal_zip = list(zip(question_list, ans))

random.shuffle(temporal_zip)

question_list, ans = zip(*temporal_zip)
question_list, ans = list(question_list), list(ans)

# Definimos una variable que registra la pregunta por la que se va
# Let's define a variable that registers the current question

current_question = 0

global questions_to_answer

# Definimos la función que inicia el quiz
# Let's define the function that starts the quiz


def start_quiz():
	start_button.forget()
	question_menu1.forget()
	submit1.forget()
	next_button.pack()
	next_question()

# Definimos la función que pasa a la siguiente pregunta
# Let's define the function that goes to the next question


def next_question():
	global current_question
	if current_question < questions_to_answer:
		# Obtenemos la pregunta que toca:
		# Let's get the current question
		check_ans()
		user_ans.set('None')
		c_question = question_list[current_question]
		# Borramos la ventana para poder actualizarla
		# Let's clear the frame to update its content
		clear_frame()
		# Imprimimos la pregunta
		# Let's print the question
		Label(f1, text=f"{current_question + 1}. {c_question}", padx=15, font="calibre 12 normal", justify="left", wraplength=800).pack(anchor=W)
		# Imprimimos las opciones
		# Let's print the options
		options_now = questions[c_question]
		random.shuffle(options_now)
		for choice in options_now:
			Radiobutton(f1, text=choice, variable=user_ans, value=choice, padx=28, justify="left", wraplength=800).pack(anchor=W)
		current_question += 1
	else:
		next_button.forget()
		check_ans()
		clear_frame()
		output = f"{user_score.get()} de {questions_to_answer} preguntas correctas"
		output2 = f"{len(mistakes)} fallos"
		output3 = f"{blank} preguntas en blanco"
		grade = f"Nota: {round(((user_score.get()-len(mistakes)*0.33)/questions_to_answer)*10,2)}"
		Label(f1, text=output, font="calibre 25 bold").pack()
		Label(f1, text=output2, font="calibre 20 bold").pack()
		Label(f1, text=output3, font="calibre 20 bold").pack()
		Label(f1, text=grade, font="calibre 18 bold").pack()
		Label(f1, text="Gracias por participar", font="calibre 18 bold").pack()


# Definimos la función que comprueba si las respuestas son correctas
# Let's define the function that checks if the answers are correct

mistakes = {}
blank = -1


def check_ans():
	temp_ans = user_ans.get()
	if temp_ans != 'None' and temp_ans == ans[current_question-1]:
		user_score.set(user_score.get()+1)
	elif temp_ans != 'None' and temp_ans != ans[current_question-1]:
		mistakes[current_question-1] = ans[current_question-1]
	else:
		global blank
		blank += 1


# Definimos la función que borra la ventana actual para poder avanzar a la siguiente pregunta
# Let's define the function that clears the frame to continue to next question

def clear_frame():
	for widget in f1.winfo_children():
		widget.destroy()


def selection():
	global questions_to_answer
	if value_inside1.get() == "Todas":
		questions_to_answer = len(questions)
	elif int(value_inside1.get()) > len(questions):
		questions_to_answer = len(questions)
	else:
		questions_to_answer = int(value_inside1.get())
	return questions_to_answer


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

	size_options = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, "Todas"]
	value_inside1 = StringVar(root)
	value_inside1.set("Select the number of questions")  # default value

	Label(root, text="Quiz", font="calibre 40 bold", relief=SUNKEN, background="cyan", padx=10, pady=9).pack()
	Label(root, text="", font="calibre 10 bold").pack()
	question_menu1 = OptionMenu(root, value_inside1, *size_options)
	question_menu1.pack()
	submit1 = Button(root, text="Submit", command=selection)
	submit1.place(x=500, y=250)
	submit1.pack(pady=20)
	Label(root, text="", font="calibre 10 bold").pack()
	start_button = Button(root, text="Empezar", command=start_quiz, font="calibre 17 bold")
	start_button.pack()
	f1 = Frame(root)
	f1.pack(side=TOP, fill=X)
	Label(root, text="", font="calibre 10 bold").pack()
	next_button = Button(root, text="Siguiente pregunta", command=next_question, font="calibre 17 bold")

	root.mainloop()
