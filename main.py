import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("Goal Smasher")


for index, todo in enumerate(todos):
    check = st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._experimental_rerun()

st.text_input(label="", placeholder="Add new goal...",
              on_change=add_todo, key='new_todo')

