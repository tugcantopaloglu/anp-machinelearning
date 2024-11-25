#Modülerlik sağlanması amacıyla tüm işlemler farklı class'larda yapılıp burada bulunan main classında çağrılmıştır
import DataHandler
import ModelTrainer 
import numpy as np
def main():
    ### verileri alıyoruz burada data içerisinde bölünmüş halde veriler zaten bulunuyorsa işlem yapmıyoruz ###
    data = DataHandler.DataHandler("./data/prepared_anomaly_data_no_label.csv")
    data.DataScrapper()
    data.DataSplitter()
    #data.DataVisualazation()
    data.OneHotEncoding()
    data.OneHotEncodingTestData()
    train_data = data.EncodedTrainDataGet()
    x_train = train_data.filter(regex='^(?!anomaly)', axis=1)
    y_train = train_data.filter(regex='^anomaly.*$', axis=1)
    
    model = ModelTrainer.ModelTrainer("RandomForest Model")
    model.RandomForest(x_train, y_train)
    model.CalculateMetricsOnTestData(test_data=data.EncodedTestDataGet())
    
    
    
def CalculateBestThreshold(model, precision = 0.01):
    thresholds = np.arange(0.1,1.0,precision)
    best_f1= 0
    best_threshold = 0
    for i in thresholds:
        value = model.CalculateMetricsOnTestData(threshold=i,check_threshold=True)
        if value > best_f1:
            best_threshold = i
            best_f1 = value
    print("Best Threshold For " + model.model_name + ":" + str(best_threshold))
    return best_threshold
    
if __name__ == "__main__":
    main()
