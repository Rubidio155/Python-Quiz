# Este proyecto genera un quiz o cuestionario de tipo test multi-respuesta
# This project generates a multi-answer test quiz or questionnaire

# Importamos los módulos necesarios
# Let's import the necessary modules
from tkinter import *

# Definimos el diccionario con las preguntas y sus respuestas correspondientes
# Let's define the dictionary with the questions and its answers

questions = {"2+3": ['2', '3', '5', '9'], "2-1": ['2', '1', '5'], "3+3": ['3', '6', '9', '7']}

# Definimos la lista con las respuestas correctas
# Let's define the list with the correct answers

ans = ['5', '1', '6']

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
		for option in questions[c_question]:
			Radiobutton(f1, text=option, variable=user_ans, value=option, padx=28).pack(anchor=NW)
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
