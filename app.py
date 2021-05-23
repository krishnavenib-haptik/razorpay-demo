import razorpay
import json

from flask import Flask, render_template, request

app = Flask(__name__,static_folder = "static", static_url_path='')
razorpay_client = razorpay.Client(auth=("rzp_test_67e1H1DVG3Sv7m", "yFPsF97IaKMomZX6RG4IFLko"))


@app.route('/')
def app_create():
    # print(request)
    print(dict(request.args))
    args = dict(request.args)
    post_data = {
        'product_name': args.get('product_name'),
        'amount': args.get('amount'),
        'description': args.get('description'),
        'email': args.get('email'),
        'contact': args.get('contact'),
        'username': args.get('username'),
        'shopping_order_id': args.get('shopping_order_id')
    }
    return render_template('app.html', post_data=post_data)


@app.route('/charge', methods=['POST'])
def app_charge():
    payment_id = request.form['razorpay_payment_id']
    return render_template('process.html', post_data=razorpay_client.payment.fetch(payment_id))

if __name__ == '__main__':
    app.run()
