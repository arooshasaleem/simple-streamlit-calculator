import streamlit as st
st.title("calculator")
num1=st.number_input("enter first number")
num2=st.number_input("enter second number")
operation=st.radio("select operation",["+","-","*","/"])
if st.button("calculate"):
        if operation == "+":
            ans = num1 + num2
        elif operation == "-":
            ans = num1 - num2
        elif operation == "*":
            ans = num1 * num2
        elif operation == "/":
            if num2!=0:
                ans = num1 / num2
        else:
            st.warning("Division by 0 error. Please enter a non-zero number.")
            ans = "Not defined"
            st.write("Answer:",ans)

        st.success(f"Answer = {ans}")
        ans = 0

        def calculate():
            if operation == "Add":
                ans = num1 + num2
            elif operation == "Subtract":
                ans = num1 - num2
            elif operation == "Multiply":
                ans = num1 * num2
            elif operation == "Divide" and num2 != 0:
                ans = num1 / num2
            else:
                st.warning("Division by 0 error. Please enter a non-zero number.")
                ans = "Not defined"

            st.success(f"Answer = {ans}")
            if st.button("Calculate result"):
                calculate()
