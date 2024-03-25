from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)
empty_space = "MISSING"
global plz, box

@app.route("/t")
def test():
    return render_template("test2.html")

@app.route("/", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        box = request.form["nm"]
        import make_sqaure
        import plain_to_encrypt
        plz = make_sqaure.make_square(box)
        # Prints Square to Python Terminal
        make_sqaure.print_square(plz)
        print(f"This is the phrase: {plain_to_encrypt.phrase}")
        encrypted = plain_to_encrypt.final_encrpyt()
        pre_encrypt = plain_to_encrypt.my_di
        print(pre_encrypt)
        print(encrypted)
        return render_template("test.html", plz=plz, pre=pre_encrypt, enc=encrypted)
    else:
        return render_template("base.html", empty=empty_space)



if __name__ == "__main__":
    app.run(debug=False)
