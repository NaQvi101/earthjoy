from model import EarthJoyModel
from flask import Flask,render_template

app = Flask(__name__)
app.config.from_object("config")
def getModel():
    return EarthJoyModel(app.config["HOST"],app.config["USER"],app.config["PASSWORD"], app.config["DATABASE"])

MODEL = getModel() 
@app.route('/')
def mainAdmin():
    return render_template('admin/adminMain.html')


@app.route('/newSellers')
def newSellers():
    return render_template('admin/newSellers.html')


@app.route('/existingSellers')
def existingSellers():  
    sellers = MODEL.getSellers(1)
    return render_template('admin/existingSellers.html',sellers=sellers)


@app.route('/newProducts')
def newProducts():
    products = MODEL.getProducts(0)
    return render_template('admin/newProducts.html',products=products)


@app.route('/existingProducts')
def existingProducts():
    products = MODEL.getProducts(1)
    return render_template('admin/existingProducts.html',products=products)


@app.route('/addNewCategory')
def addNewCategory():
    return render_template('admin/addNewCategory.html')

@app.route('/addNewSubCategory')
def addNewSubCategory():
    return render_template('admin/addNewSubCategory.html')
    

@app.route('/deleteCategory')
def addDeleteCategory():
    return render_template('admin/deleteCategory.html')
    

@app.route('/deleteSubCategory')
def addDeleteSubCategory():
    return render_template('admin/deleteSubCategory.html')

    
@app.route('/logOut')
def logOut():
    pass


if __name__=="__main__":
    app.run(debug=True)
