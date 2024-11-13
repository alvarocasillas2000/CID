class SimpleLinearRegression:
    # Constructor de la clase SimpleLinearRegression
    def __init__(self, advertising, sales):
        self.advertising = advertising
        self.sales = sales
        self.beta_0 = 0
        self.beta_1 = 0
        self.calculate_betas()

    # Método para calcular los valores de beta_0 y beta_1
    def calculate_betas(self):
        n = len(self.advertising)
        # Calcular la media de los valores de Advertising y Sales
        mean_x = sum(self.advertising) / n
        mean_y = sum(self.sales) / n

        # Calcular los valores de beta_0 y beta_1
        numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(self.advertising, self.sales))
        denominator = sum((x - mean_x) ** 2 for x in self.advertising)

        self.beta_1 = numerator / denominator
        self.beta_0 = mean_y - self.beta_1 * mean_x

    # Método para imprimir la ecuación de la regresión lineal
    def print_equation(self):
        print(f"Sales = {self.beta_0} + {self.beta_1} * Advertising")

    # Método para predecir el valor de Sales
    def predict(self, advertising_value):
        return self.beta_0 + self.beta_1 * advertising_value




if __name__ == "__main__":
    # Solicitar al usuario los datos de Advertising
    advertising_data = input("Ingrese los valores de Advertising separados por comas: ")
    advertising_data = [float(x.strip()) for x in advertising_data.split(",")] #se separan los valores por comas, y se almacen en una lista 

    # Solicitar al usuario los datos de Sales
    sales_data = input("Ingrese los valores de Sales separados por comas: ")
    sales_data = [float(y.strip()) for y in sales_data.split(",")] #se separan los valores por comas, y se almacen en una lista

    # Crear el modelo con los datos ingresados
    model = SimpleLinearRegression(advertising_data, sales_data) #se crea el objeto model de la clase SimpleLinearRegression
    model.print_equation() #se imprime la ecuación de la regresión lineal

    # Solicitar un valor de Advertising para realizar una predicción
    advertising_value = float(input("Ingrese un valor de Advertising para predecir Sales: ")) #se solicita un valor de advertising para predecir las ventas
    predicted_sales = model.predict(advertising_value) #se realiza la predicción de las ventas
    print(f"Predicted Sales: {predicted_sales}") #se imprime el valor de las ventas predichas
