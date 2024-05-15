#Libreria Phyton
import random



#Primera variable creada donde se genera el número aleatorio entre 1 y 100
def random_number():
    return random.randint(1,100)



#Segunda variable, es donde se solicita el número al usuario y validar si es correcto o se sale del rango
def get_user_guess():
 while True:
        try:
            user_num = int(input("Go to play! Write a number from 1 to 100: "))
            if 1 <= user_num <= 100:
                return user_num
            print("Oh, try again! Please enter a number between 1 and 100")
        except ValueError:
            print("Please enter a correct number.")



#Tercera variable, para el número aleatorio generado por la computadora
def get_computer_guess():
    return random.randint(1,100)



#Cuarta variable, validar si es correcto
def check_guess(player_guess, secret_number):
    """
    Verifica si el número ingresado por el jugador es correcto, menor o mayor al número secreto.

    Args:
        player_guess (int): El número ingresado por el jugador.
        secret_number (int): El número secreto generado por el juego.

    Returns:
        tuple: Una tupla que indica si el intento fue exitoso y un mensaje asociado.
    """
    if player_guess == secret_number:
        return True, 'Congratulations! The number entered is correct.'
    elif player_guess < secret_number:
        return False, "Ups! It seems the number is lower, keep trying"
    else:
        return False, "Ups! It seems the number is higher, keep trying."



#Quinta variable, lógica del juego
def game_play():
    """Función principal que lleva a cabo la lógica del juego."""
    print("Welcome to guess the number, let's play!")
    secret_number = random_number()
    user_attempts = []
    comp_attempts = []

    while True:
        user_guess = get_user_guess()
        user_attempts.append(user_guess)
        print("User turn: ", user_guess)
        success, result_user = check_guess(user_guess, secret_number)
        if success:
            break

        comp_guess = get_computer_guess()
        comp_attempts.append(comp_guess)
        print("Computer turn: ", comp_guess)
        success, result_comp = check_guess(comp_guess, secret_number)
        print(result_comp)
        if success:
            break

    print(f"The secret number was {secret_number}.")
    print(f"You made {len(user_attempts)} attempts, and those were: {user_attempts}")
    print(f"The computer made {len(comp_attempts)} attempts, and those were: {comp_attempts}")



#Sexta variable, jugar nuevamente
def play_again():
    """Ofrece al jugador la opción de jugar nuevamente."""
    while True:
        play_again = input("Do you wanna play again? (y/n): ").strip().lower()
        if play_again == "y":
            game_play()
        elif play_again == "n":
            print("Thank you! See you next time.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

            
#comprueba si este archivo de Python se está ejecutando directamente desde la línea de comandos.
if __name__ == "__main__":
    game_play()