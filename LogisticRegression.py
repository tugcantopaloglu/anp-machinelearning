#burada her şeyi kendim yazmaya çalıştım hesaplamaları derste öğrendiğimiz fonksiyonlardan aldığım notlardan oluşturdum aşağıdaki kütüphaneleri sadece matematik işlemleri ve görselleştirme için ekledim
import math
import matplotlib.pyplot as plt
import pandas as pd
import DataHandler
class LogisticRegression():
    
    def __init__(self,model_name) -> None:
        self.model_name = model_name
    
    
    #test ile deneme yaparak skorları hesaplıyoruz
    def CalculateMetricsOnTestData(self,threshold = 0.5,check_threshold=False):
        data_handler = DataHandler.DataHandler("./data/hw1Data.txt")
        data_handler.DataSplitter()
        x_test = data_handler.TestDataGet()[["Exam1", "Exam2"]].to_numpy()
        y_test = data_handler.TestDataGet()["Admitted"].to_numpy()
        y_prediction = []
        for i in range(len(y_test)):
            lineer_combination = sum(self.weights[j] * x_test[i][j] for j in range(len(self.weights)))
            y_prediction.append(1 if self.Sigmoid(lineer_combination) >= threshold else 0)

        # Metrikleri hesapla
        accuracy, precision, recall, f1_score = self.Metrics(y_test, y_prediction)
        
        #optimum thresholdu bulurken bu çıktıları vermesini istemiyoruz bundan dolayı böyle bir kontrol yapıyoruz
        if (check_threshold == False):
            if threshold != 0.5:
                print("MODEL THRESHOLD CHANGED TO OPTIMUM CALCULATING AGAIN")
            print("")
            print("###")
            print(self.model_name + " Scores:")
            print("Model Evaluation on Test Set:")
            print(f"Accuracy: {accuracy:.4f}")
            print(f"Precision: {precision:.4f}")
            print(f"Recall: {recall:.4f}")
            print(f"F1-Score: {f1_score:.4f}")
            print("###")
            print("")
            print("Percentage Calculation:")
            print(f"Accuracy: %{accuracy*100:.2f}")
            print(f"Precision: %{precision*100:.2f}")
            print(f"Recall: %{recall*100:.2f}")
            print(f"F1-Score: %{f1_score*100:.2f}")
            
            with open("./results/scores.txt", 'a+') as f:
                if threshold != 0.5:
                    f.write("MODEL THRESHOLD CHANGED TO OPTIMUM CALCULATING AGAIN\n")
                f.write("###\n")
                f.write(self.model_name + " Scores:\n")
                f.write("Model Evaluation on Test Set:\n")
                f.write(f"Accuracy: {accuracy:.4f}\n")
                f.write(f"Precision: {precision:.4f}\n")
                f.write(f"Recall: {recall:.4f}\n")
                f.write(f"F1-Score: {f1_score:.4f}\n")
                f.write("###\n")
                f.write(f"Accuracy: %{accuracy*100:.2f}\n")
                f.write(f"Precision: %{precision*100:.2f}\n")
                f.write(f"Recall: %{recall*100:.2f}\n")
                f.write(f"F1-Score: %{f1_score*100:.2f}\n")
                f.write("###\n")
            
        
        return f1_score
    

        


