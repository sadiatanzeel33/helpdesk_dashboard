import streamlit as st
from db import init_db, get_all_tickets, resolve_ticket, delete_ticket

# Dummy admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Set up page
st.set_page_config(page_title="Admin Login", layout="wide")

# Initialize DB
init_db()

# Login form
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if not st.session_state.admin_logged_in:
    st.title("🔐 Admin Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login = st.form_submit_button("Login")

        if login:
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                st.session_state.admin_logged_in = True
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")

else:
    # Admin dashboard section
    st.title("🔧 Admin Dashboard")
    st.sidebar.success("Logged in as Admin")

    tickets = get_all_tickets()

    if tickets:
        for ticket in tickets:
            # Adjusted unpacking based on 6 values only
            ticket_id, name, email, dept, issue, status = ticket

            with st.expander(f"🎫 Ticket #{ticket_id} - {name}"):
                st.write(f"**Email:** {email}")
                st.write(f"**Department:** {dept}")
                st.write(f"**Issue:** {issue}")
                st.write(f"**Status:** {'✅ Resolved' if status == 'Resolved' else '❌ Open'}")
                # st.write(f"**Created At:** {created_at}")  # Remove or add if available later

                col1, col2 = st.columns(2)

                if status != "Resolved":
                    with col1:
                        if st.button("Mark as Resolved", key=f"resolve_{ticket_id}"):
                            resolve_ticket(ticket_id)
                            st.success("Ticket marked as resolved.")
                            st.rerun()

                with col2:
                    if st.button("Delete Ticket", key=f"delete_{ticket_id}"):
                        delete_ticket(ticket_id)
                        st.warning("Ticket deleted.")
                        st.rerun()
    else:
        st.info("No tickets found.")

    # Logout option
    if st.sidebar.button("Logout"):
        st.session_state.admin_logged_in = False
        st.rerun()

