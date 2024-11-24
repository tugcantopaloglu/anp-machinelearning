import pandas as pd
#import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
from sklearn.preprocessing import MinMaxScaler


class DataHandler():
    #standart const
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        
    #Dosyadan okuma işlemleri    
    def DataScrapper(self):
        self.csv_data = pd.read_csv(self.data_file_path, header=None, names=["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","is_anomaly","anomaly_type"])
        print("Data has been parsed succesfully...")
        
    #Veriyi eğitim için bölme (başka class'ta kullanırsak diye veriyi getter ile de alacağız)
    #tekrar tekrar bölmemek için dosyalara kaydedelim eğer dosyada yoksa bölsün
    def DataSplitter(self):
        if os.path.exists("./data/train_data.txt") and os.path.exists("./data/validate_data.txt") and os.path.exists("./data/test_data.txt"):
            self.train_data = pd.read_csv("./data/train_data.txt")
            self.validate_data = pd.read_csv("./data/validate_data.txt")
            self.test_data = pd.read_csv("./data/test_data.txt")
        else:
            self.train_data, self.temp_data = train_test_split(self.csv_data, test_size=0.4, random_state=42)
            self.validate_data, self.test_data = train_test_split(self.temp_data, test_size=0.5, random_state=42)
            self.train_data.to_csv("./data/train_data.txt", index=False)
            self.validate_data.to_csv("./data/validate_data.txt", index=False)
            self.test_data.to_csv("./data/test_data.txt", index=False)
            print("Data has been sliced to %60 train (train_data), %20 (validate_data) and %20 (test_data) succesfully...")
            print("Data saved into files...")

    
    def DataVisualazation(self):
        #TSNE ile veriyi 2 boyuta indirgeyip görselleştirme işlemi bu işlemi yapmazsak veriyi görselleştiremeyiz
        features = self.train_data.drop(columns=['is_anomaly', 'anomaly_type'])
        features = pd.get_dummies(features)
        tsne = TSNE(n_components=2, random_state=42, perplexity=30,learning_rate=200, n_iter=1000)
        tsne_results = tsne.fit_transform(features)
        train_data_tsne = self.train_data.copy()
        train_data_tsne['tsne-2d-one'] = tsne_results[:,0]
        train_data_tsne['tsne-2d-two'] = tsne_results[:,1]
        
        plt.figure(figsize=(10, 10))
        for label, color in zip([0, 1], ['red', 'green']):
            subset = self.train_data_tsne[self.train_data_tsne['is_anomaly'] == label]
            plt.scatter(subset['tsne-2d-one'], subset['tsne-2d-two'], c=color, label=f"Anomaly={label}", alpha=0.7) 
        plt.title("TSNE Scatter Plot of Training Data")
        plt.xlabel("TSNE Component 1")
        plt.ylabel("TSNE Component 2") 
        plt.legend()
        plt.grid(alpha=0.5)
        plt.show()
        print("Data visualized successfully...")
        
    def OneHotEncoding(self, categorical_columns = ['protocol_type','service','flag','anomaly_type'], numerical_columns = ['duration','src_bytes', 'dst_bytes', 'land', 'wrong_fragment','urgent','hot', 'num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations','num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login',
    'count','srv_count','serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count','dst_host_srv_count','dst_host_same_srv_rate',
    'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate', 'dst_host_serror_rate','dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate']):
        self.encoded_train_data = pd.get_dummies(self.train_data, columns=categorical_columns, drop_first=True)
        scaler = MinMaxScaler()
        scaled_numerical_features = scaler.fit_transform(self.encoded_train_data[numerical_columns])
        scaled_train_data = self.encoded_train_data.copy()
        scaled_train_data[numerical_columns] = scaled_numerical_features
        self.encoded_train_data = scaled_train_data
        
        
    def TrainDataGet(self):
        return self.train_data
    
    def ValidateDataGet(self):
        return self.validate_data
    
    def TestDataGet(self):
        return self.test_data
    
    def EncodedTrainDataGet(self):
        return self.encoded_train_data
    