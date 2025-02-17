import streamlit as st
import functions

todos = functions.get_todos()
# my to do app

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my To-Do App")
st.write("Check the To-Do to complete it.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a To-Do:", placeholder="Add...", on_change=add_todo,
              key="new_todo")