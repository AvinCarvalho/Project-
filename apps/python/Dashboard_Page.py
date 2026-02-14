import streamlit as st
from datetime import datetime

USER = {
    "name": "Alice Johnson",
    "nickname": "Ally",
}

DATA = {
    "daily_expense": 45.60,
    "monthly_expense": 870.35,
    "pending_tasks": 3,
    "quick_notes": "Buy groceries, call bank, schedule dentist appointment.",
}

st.set_page_config(page_title="User Dashboard", layout="wide")

st.markdown("""
<style>
/* Background gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #8e7ca4 0%, #c4aac9 100%);
    height: 100vh;
    overflow: hidden;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Sidebar styling */
.css-1d391kg {
    background-color: #e2e3e5 !important;
    border-top-right-radius: 25px;
    border-bottom-right-radius: 25px;
    padding-top: 20px;
    padding-left: 25px;
    padding-right: 25px;
}

/* Sidebar links */
.css-1d391kg a, .css-1d391kg label {
    font-weight: 600;
    font-size: 14px;
    color: #6a4f58;
    padding: 10px 15px;
    border-radius: 15px;
    display: block;
    margin-bottom: 10px;
    cursor: pointer;
    text-decoration: none;
    user-select: none;
}
.css-1d391kg a:hover {
    background-color: #b87f8f;
    color: white;
}

/* Active sidebar link */
.sidebar-active {
    background-color: #b87f8f !important;
    color: white !important;
}

/* Top bar */
.topbar {
    background-color: #b87f8f;
    color: white;
    padding: 10px 20px;
    font-weight: 700;
    font-size: 16px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    border-radius: 0 0 20px 20px;
}

/* Sign out button */
.signout-btn {
    background-color: #9c5e68;
    border: none;
    color: white;
    border-radius: 15px;
    padding: 6px 16px;
    font-weight: 600;
    font-size: 14px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
.signout-btn:hover {
    background-color: #7e4751;
}

/* Content container */
.content {
    padding: 25px 50px;
    flex-grow: 1;
    overflow-y: auto;
}

/* Welcome and date */
.welcome-msg {
    font-size: 26px;
    font-weight: 700;
    color: #4a3c4a;
    margin-bottom: 4px;
    user-select: none;
}
.date-msg {
    font-size: 14px;
    color: #6a5f6d;
    margin-bottom: 30px;
    user-select: none;
}

/* Cards container */
.cards-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
}

/* Each card */
.card {
    background-color: #e2e3e5;
    border-radius: 20px;
    padding: 20px 25px;
    box-shadow: 2px 3px 15px rgba(0,0,0,0.12);
    cursor: pointer;
    transition: box-shadow 0.25s ease;
    user-select: none;
}
.card:hover {
    box-shadow: 4px 6px 20px rgba(0,0,0,0.25);
}

/* Card title */
.card-title {
    font-weight: 600;
    font-size: 16px;
    margin-bottom: 8px;
    color: #5c4a58;
}

/* Card value */
.card-value {
    font-size: 28px;
    font-weight: 700;
    color: #8c6b75;
}

/* Placeholder text for empty data */
.placeholder {
    font-style: italic;
    color: #9c7d8d;
}

/* Footer with Help/Contact */
.footer {
    background-color: #e2e3e5;
    padding: 15px 25px;
    text-align: center;
    font-size: 12px;
    color: #6a4f58;
    border-top-left-radius: 25px;
    border-top-right-radius: 25px;
    user-select: none;
}

.footer a {
    color: #b87f8f;
    text-decoration: none;
    margin: 0 10px;
    font-weight: 600;
}
.footer a:hover {
    text-decoration: underline;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("### Navigation")
pages = ["Dashboard", "Expenses", "Profile Settings", "Help / Contact"]
selection = st.sidebar.radio("", pages)

for page in pages:
    if page == selection:
        st.sidebar.markdown(f'<a class="sidebar-active">{page}</a>', unsafe_allow_html=True)
    else:
        st.sidebar.markdown(f'<a>{page}</a>', unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
    <button class="signout-btn" onclick="alert('Signed out!')">Sign Out</button>
</div>
""", unsafe_allow_html=True)


st.markdown('<div class="content">', unsafe_allow_html=True)

if selection == "Dashboard":
    
    name_display = USER["nickname"] if USER.get("nickname") else USER["name"]
    today_str = datetime.now().strftime("%A, %B %d, %Y")
    st.markdown(f'<div class="welcome-msg">Welcome back, {name_display}!</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="date-msg">{today_str}</div>', unsafe_allow_html=True)

   
    st.markdown('<div class="cards-container">', unsafe_allow_html=True)

    def card(title, value, key, placeholder="No data available", url="#"):
        if value is None or (isinstance(value, str) and not value.strip()):
            display_val = f'<div class="placeholder">{placeholder}</div>'
        else:
            display_val = f'<div class="card-value">{value}</div>'

        card_html = f"""
        <div class="card" onclick="window.open('{url}', '_self')" tabindex="0" role="button" aria-label="{title} card">
            <div class="card-title">{title}</div>
            {display_val}
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

    
    daily_expense_val = f"${DATA['daily_expense']:.2f}" if DATA.get("daily_expense") else None
    card("Daily Expense", daily_expense_val, "daily", url="/expenses")

  
    monthly_expense_val = f"${DATA['monthly_expense']:.2f}" if DATA.get("monthly_expense") else None
    card("Monthly Expense", monthly_expense_val, "monthly", url="/expenses")

    pending_tasks_val = str(DATA.get("pending_tasks")) if DATA.get("pending_tasks") else None
    card("Pending Tasks", pending_tasks_val, "pending", url="/tasks")

    
    quick_notes_val = DATA.get("quick_notes", "")
    if len(quick_notes_val) > 45:
        quick_notes_val = quick_notes_val[:42] + "..."
    card("Quick Notes", quick_notes_val, "notes", placeholder="No notes yet", url="/notes")

    st.markdown('</div>', unsafe_allow_html=True) 

elif selection == "Expenses":
    st.title("Expenses")
    st.info("Detailed expenses view coming soon.")

elif selection == "Profile Settings":
    st.title("Profile Settings")
    st.info("Profile settings page coming soon.")

elif selection == "Help / Contact":
    st.title("Help & Contact")
    st.markdown("""
    For assistance, please email support@example.com or call 123-456-7890.
    """)

st.markdown('</div>', unsafe_allow_html=True) 


st.markdown("""
<div class="footer">
    <a href="#">Help</a> | <a href="#">Contact</a>
</div>
""", unsafe_allow_html=True)
