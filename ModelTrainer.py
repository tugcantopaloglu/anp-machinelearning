import matplotlib.pyplot as plt
import pandas as pd
import DataHandler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class ModelTrainer():
    
    def __init__(self,model_name) -> None:
        self.model_name = model_name
    
    #binary classification yapan random forest modeli eğitiyoruz ve modeli kaydediyoruz
    def RandomForest(self, x_train, y_train):
        rf_model = RandomForestClassifier(random_state=42, n_estimators=100, class_weight="balanced")
        rf_model.fit(x_train, y_train)
        self.rf_model = rf_model
        #self.rf_model.save_model("./models/random_forest_model")
        self.feature_names = x_train.columns.tolist()
        with open("./models/feature_names.txt", "w") as f:
            f.write("\n".join(self.feature_names))
        print("Multi-Class Random Forest Model Trained Successfully...")
    
    
    
    #test ile deneme yaparak skorları hesaplıyoruz
    def CalculateMetricsOnTestData(self,test_data,threshold = 0.5,check_threshold=False):
        x_test = test_data.filter(regex='^(?!anomaly)', axis=1)
        y_test = test_data.filter(regex='^anomaly.*$', axis=1)
        print(x_test)
        # Özellikleri yükle ve eksik olanları tamamla
        with open("./models/feature_names.txt", "r") as f:
            feature_names = f.read().splitlines()

        missing_features = set(feature_names) - set(x_test.columns)
        for feature in missing_features:
            x_test[feature] = 0
        
        x_test = x_test[feature_names]  # Sıralamayı düzelt
        y_pred = self.rf_model.predict(x_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred,average='macro')
        recall = recall_score(y_test, y_pred,average='macro')
        f1 = f1_score(y_test, y_pred,average='macro')
        
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
            print(f"F1-Score: {f1:.4f}")
            print("###")
            print("")
            print("Percentage Calculation:")
            print(f"Accuracy: %{accuracy*100:.2f}")
            print(f"Precision: %{precision*100:.2f}")
            print(f"Recall: %{recall*100:.2f}")
            print(f"F1-Score: %{f1*100:.2f}")
            
            with open("./results/scores.txt", 'a+') as f:
                if threshold != 0.5:
                    f.write("MODEL THRESHOLD CHANGED TO OPTIMUM CALCULATING AGAIN\n")
                f.write("###\n")
                f.write(self.model_name + " Scores:\n")
                f.write("Model Evaluation on Test Set:\n")
                f.write(f"Accuracy: {accuracy:.4f}\n")
                f.write(f"Precision: {precision:.4f}\n")
                f.write(f"Recall: {recall:.4f}\n")
                f.write(f"F1-Score: {f1:.4f}\n")
                f.write("###\n")
                f.write(f"Accuracy: %{accuracy*100:.2f}\n")
                f.write(f"Precision: %{precision*100:.2f}\n")
                f.write(f"Recall: %{recall*100:.2f}\n")
                f.write(f"F1-Score: %{f1*100:.2f}\n")
                f.write("###\n")
            
        
        return f1_score
    

        


