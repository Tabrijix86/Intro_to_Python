import turtle

name = turtle.textinput("Name", "What is your name?")

greeting = "Hello. How are you today?"
if name:
    name = name.strip().lower()
    if name.startswith("mr"):
        greeting = "Hello, sir. How are you today?"
    elif name.startswith("mrs") or name.startswith("ms"):
        greeting = "Hello, ma'am. How are you today?"
    else:
        greeting = f"Hello, {name.capitalize()}. How are you today?"

print(greeting)
turtle.exitonclick()