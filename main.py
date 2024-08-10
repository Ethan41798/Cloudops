from flask import Flask, render_template, request, flash, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bigcloudopstestkey'
Bootstrap(app)
csrf = CSRFProtect(app)


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@app.route('/test', methods=['GET'])
def tiles():
    return render_template("tiles.html")


@app.route('/boot', methods=['GET'])
def bootstrap():
    return render_template("bootst.html")


@app.route('/profile', methods=['GET'])
def profile():
    return "This Website is in testing phase"


@app.route('/image', methods=['GET'])
def image():
    return render_template("devsecops.html")


@app.route('/home',  methods=['GET'])
def base_home():
    return render_template("base.html")


@app.route('/blogs/devsecops', methods=['GET'])
def blog_devsecops():
    return render_template("blog-devsecops.html")


@app.route('/blogs/data', methods=['GET'])
def blog_datascience():
    return render_template("blog-data.html")


@app.route('/blogs/sre', methods=['GET'])
def blog_sre():
    return render_template("blog-sre.html")


@app.route('/blogs/cloudservices', methods=['GET'])
def blog_cloud_services():
    return render_template("blog-cloud-services.html")


@app.route('/blogs/automation', methods=['GET'])
def blog_automation():
    return render_template("blog-automation.html")


@app.route('/tiles', methods=['GET'])
def service_tiles():
    return render_template("blogtiles.html")


@app.route('/blogs', methods=['GET'])
def blogs_tiles():
    return render_template("blogs.html")


@app.route('/slider', methods=['GET'])
def test_slider():
    return render_template('slider.html')


@app.route('/slide-show', methods=['GET'])
def test_slide_show():
    return render_template('slideshow.html')


@app.route('/services', methods=['GET'])
def services():
    return render_template('srv-ai-ml.html')


@app.route('/services/ai-ml', methods=['GET'])
def services_ai_ml():
    return render_template('srv-ai-ml.html')


@app.route('/services/bigdata', methods=['GET'])
def services_big_data():
    return render_template('srv-big-data.html')


@app.route('/services/devsecops', methods=['GET'])
def services_devsecops():
    return render_template('srv-devsecops.html')


@app.route('/services/sre', methods=['GET'])
def services_sre():
    return render_template('srv-sre.html')


@app.route('/services/automation', methods=['GET'])
def services_automation():
    return render_template('srv-automation.html')


@app.route('/services/cloud-services', methods=['GET'])
def services_cloud_services():
    return render_template('srv-cloud-services.html')


@app.route('/about-us', methods=['GET'])
def about_us():
    return render_template('aboutus.html')


@app.route('/contact-us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        #data = request.form
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        contact_num = request.form.get('contactnum', '')
        subject = request.form.get('subject', '')
        print({"Full Name": name, "Email": email, "Contact Number": contact_num, "Subject": subject})
    return render_template('contactus.html')


if __name__ == '__main__':
    app.run(debug=True)