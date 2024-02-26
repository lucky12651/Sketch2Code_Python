from resize_for_detection import crop
import json

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "F:/Bino/Tensorflow/models/research/object_detection/static/uploads/"
app.secret_key = 'secret123'

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'image' in request.files:
            image = request.files["image"]
            filename = secure_filename(image.filename)
            filepath = os.path.join(app.config['IMAGE_UPLOADS'], filename)
            image.save(filepath)
            image = cv2.imread(filepath)
            flash('Generated Successfully!', 'success')
def sort_detection_list(detection_list, filename, filenames):
    size = len(detection_list)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if detection_list[min_index]["ymin"] > detection_list[j]["ymin"] and detection_list[min_index]["xmin"] > detection_list[j]["xmin"]:
                min_index = j
    detection_list[i], detection_list[min_index] = detection_list[min_index], detection_list[i]
