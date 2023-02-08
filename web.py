import streamlit as st
import functions

todos = functions.read_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-do app")
st.write("Add a to-do by typing it and then pressing enter.")
st.write("Click the checkbox to mark to-do completed")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new to-do...",
              on_change=add_todo, key="new_todo")
