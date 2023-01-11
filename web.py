import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    txtbox_todo = st.session_state['new_todo'] + "\n"
    todos.append(txtbox_todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""


st.title("My todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
