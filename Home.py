import streamlit as st
import uuid
import streamlit.components.v1 as components
from utils.razorpay_utils import create_razorpay_order

def show_home():
    st.title("📦 Choose Your Plan")

    plans = {
        "Free": {"label": "Free - Send up to 50 mails (5MB attachments)", "price": 0},
        "Standard": {"label": "Standard - Send up to 200 mails (10MB attachments)", "price": 40},
        "Premium": {"label": "Premium - Send up to 400 mails (25MB attachments)", "price": 70},
    }

    plan_label = st.radio("Select a plan to continue:", [p["label"] for p in plans.values()])
    selected_plan = next(key for key, val in plans.items() if val["label"] == plan_label)
    price = plans[selected_plan]["price"]

    user_email = st.text_input("Enter your email for receipt")
    user_name = st.text_input("Enter your full name")
    user_phone = st.text_input("Enter your phone number")

    if selected_plan == "Free":
        if st.button("Continue"):
            st.session_state.plan_selected = True
            st.session_state.MAX_EMAILS_ALLOWED = 50
            st.session_state.MAX_ATTACHMENT_SIZE_MB = 5
            st.rerun()
    else:
        if st.button(f"Pay ₹{price} to Continue"):
            order = create_razorpay_order(user_email, user_name, price)
            payment_id = order['id']
            components.html(f"""
                <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
                <button id="rzp-button1">Pay Now</button>
                <script>
                var options = {{
                    "key": "{order['key']}",
                    "amount": "{order['amount']}",
                    "currency": "INR",
                    "name": "Mail Automation",
                    "description": "Plan Purchase",
                    "order_id": "{order['id']}",
                    "handler": function (response){{
                        fetch(window.location.href + "?payment_success=true").then(() => {{
                            window.location.href = window.location.href + "?payment_success=true"
                        }})
                    }},
                    "prefill": {{
                        "name": "{user_name}",
                        "email": "{user_email}",
                        "contact": "{user_phone}"
                    }},
                    "theme": {{"color": "#3399cc"}}
                }};
                var rzp1 = new Razorpay(options);
                document.getElementById('rzp-button1').onclick = function(e){{
                    rzp1.open();
                    e.preventDefault();
                }}
                </script>
            """, height=300)

    query_params = st.query_params
    if query_params.get("payment_success"):
        if selected_plan == "Standard":
            st.session_state.MAX_EMAILS_ALLOWED = 200
            st.session_state.MAX_ATTACHMENT_SIZE_MB = 10
        elif selected_plan == "Premium":
            st.session_state.MAX_EMAILS_ALLOWED = 400
            st.session_state.MAX_ATTACHMENT_SIZE_MB = 25
        st.session_state.plan_selected = True
        st.query_params.clear()
        st.rerun()
