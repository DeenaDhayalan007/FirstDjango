from django.db.models import base
import matplotlib.pyplot as plt
import seaborn  as sns
import base64
from io import BytesIO
from django.contrib.auth.models import User 

def get_salesman_from_id(val):
    salesman = User.objects.get(id=val)
    return salesman

def get_image():
    # create a bytes buffer for the image to save
    buffer = BytesIO()
    # create the plot with the use of BytesIO object as its file
    plt.savefig(buffer , format="png")
    # set the cursor beg of the stream
    buffer.seek(0)
    # retrive the entire content of the 'file'
    image_png = buffer.getvalue()
    # encoding decoding
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    # free the memory of buffer
    buffer.close()

    return graph

def get_simple_plot(chart_type , *args , **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')

    if chart_type == 'Barplot':
        title = "Total price by day (bar)"
        plt.title = title
        plt.bar(x,y)
    elif chart_type == 'Lineplot':
        plt.title = "Title"
        plt.plot(x,y)
    else:
        plt.title = "Title"
        sns.countplot('name',data=data)
    plt.tight_layout()
    plt.xticks(rotation = 45)

    graph = get_image()
    return graph
