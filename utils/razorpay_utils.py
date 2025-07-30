import razorpay

razorpay_key_id = "YOUR_RAZORPAY_KEY_ID"
razorpay_key_secret = "YOUR_RAZORPAY_SECRET"

def create_razorpay_order(email, name, price):
    client = razorpay.Client(auth=(razorpay_key_id, razorpay_key_secret))
    order = client.order.create({
        "amount": price * 100,
        "currency": "INR",
        "receipt": f"receipt_{email}",
        "payment_capture": 1,
        "notes": {"email": email, "name": name},
    })
    order['key'] = razorpay_key_id
    return order
